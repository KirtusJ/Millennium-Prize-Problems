#!/usr/bin/env bash
# Director Z4: start one headless PCP worker and record the run in the parent register.
# usage: launch.sh <worker> <model>
set -u
w="$1"; model="$2"
W="$HOME/z4-workers"
CL="/c/Users/donke/AppData/Local/Claude-Data/claude_pzs8sxrjxfjjc/claude-code/2.1.330/9424831ad51c/claude.exe"
export PYTHONUTF8=1 PATH="$HOME/.elan/bin:$PATH"
cat "$W/common.txt" "$W/$w/brief.txt" > "$W/$w/PROMPT.txt"
cd "$HOME/z4-mpp-pcp" || exit 9
date -u +%Y-%m-%dT%H:%M:%SZ > "$W/$w/started.txt"
python "$HOME/pcp-os/PCP_OS_Python/pcp_os.py" check --as director-z4 --name "worker-$w-run1" \
  --cwd "$W/$w" --timeout 1800 --tail 5 -- \
  bash -c "\"$CL\" -p --model $model --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt" \
  > "$W/$w/parent_check.log" 2>&1
echo "EXIT $?" > "$W/$w/finished.txt"
date -u +%Y-%m-%dT%H:%M:%SZ >> "$W/$w/finished.txt"
