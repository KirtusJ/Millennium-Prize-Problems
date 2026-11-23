#!/usr/bin/env bash
# Director Z4: start one headless PCP worker and record the run in the director's register.
# usage: launch.sh <worker> <model> <timeout seconds>
set -u
w="$1"; model="$2"; to="${3:-2400}"
W=/home/user/z4-workers
export PATH="$HOME/.elan/bin:$PATH"
cat "$W/common.txt" "$W/$w/brief.txt" > "$W/$w/PROMPT.txt"
date -u +%Y-%m-%dT%H:%M:%SZ > "$W/$w/started.txt"
python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py check --ws /home/user/z4-work/pcp --as director-z4 --name "worker-$w-run1" \
  --cwd "$W/$w" --timeout "$to" --tail 5 -- \
  bash -c "claude -p --model $model --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task,WebFetch,WebSearch' < PROMPT.txt" \
  > "$W/$w/parent_check.log" 2>&1
echo "EXIT $?" > "$W/$w/finished.txt"
date -u +%Y-%m-%dT%H:%M:%SZ >> "$W/$w/finished.txt"
