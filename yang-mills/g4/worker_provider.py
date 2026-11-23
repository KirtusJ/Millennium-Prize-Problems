"""Text-only Codex CLI provider for a PCP-hosted mathematical commission.

No apps, browser, agent tools, shell tools, or persistent chat are enabled.
The parent owns execution of returned proof source and records its outcome.
"""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

request = json.load(sys.stdin)
out = Path(os.environ['G4_ATTEMPT'])
prompt = (request.get('system') or '') + '\n\n' + '\n\n'.join(
    m['content'] for m in request['messages'])
(out / 'delivered_prompt.txt').write_text(prompt, encoding='utf8')
executable = shutil.which('codex')
if not executable:
    raise RuntimeError('Codex CLI unavailable')
argv = [executable, 'exec', '--ephemeral', '--ignore-user-config',
        '--skip-git-repo-check', '--sandbox', 'read-only', '--json',
        '--color', 'never', '--disable', 'shell_tool', '--disable',
        'unified_exec', '--disable', 'apps', '--disable', 'multi_agent',
        '-c', 'web_search="disabled"', '-C', str(out), '-']
started = time.time_ns()
with subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE,
                      creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0)) as p:
    pid = p.pid
    try:
        stdout, stderr = p.communicate(prompt.encode(), timeout=240)
    except subprocess.TimeoutExpired:
        subprocess.run(['taskkill', '/PID', str(pid), '/T', '/F'],
                       capture_output=True, timeout=20,
                       creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
        stdout, stderr = p.communicate(timeout=15)
    exited = time.time_ns()
events = []
for line in stdout.decode('utf8', errors='replace').splitlines():
    try:
        events.append(json.loads(line))
    except ValueError:
        pass
items = [e.get('item', {}) for e in events if e.get('type') == 'item.completed']
answers = [i.get('text', '') for i in items if i.get('type') == 'agent_message']
unexpected = [i.get('type') for i in items if i.get('type') not in {'agent_message', 'reasoning'}]
receipt = {'pid': pid, 'start_ns': started, 'exit_observed_ns': exited,
           'returncode': p.returncode, 'prompt_sha256': hashlib.sha256(prompt.encode()).hexdigest(),
           'unexpected_item_types': unexpected,
           'event_types': [e.get('type') for e in events]}
if p.returncode or not answers or unexpected:
    receipt['error_events'] = [e for e in events if e.get('type') in {'error', 'turn.failed'}]
    # The only persisted diagnostics are structured errors, never the raw credential environment.
    (out / 'model_process.json').write_text(json.dumps(receipt, indent=2), encoding='utf8')
    raise SystemExit(p.returncode or 1)
answer = answers[-1].strip()
receipt.update(output_sha256=hashlib.sha256(answer.encode()).hexdigest(),
               post_exit_readback_ns=time.time_ns())
(out / 'model_process.json').write_text(json.dumps(receipt, indent=2), encoding='utf8')
(out / 'model_reply.txt').write_text(answer, encoding='utf8')
usage = next((e.get('usage') for e in reversed(events) if e.get('type') == 'turn.completed'), None)
print(json.dumps({'text': answer, 'model': 'Codex CLI host default', 'usage': usage}))
