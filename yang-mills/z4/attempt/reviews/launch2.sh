#!/usr/bin/env bash
# Director Z4: start one headless PCP worker, admitted as a task under the director (T1) in the
# Rust-native task graph, recorded as a check in the director's register, released when it ends.
# usage: launch2.sh <worker> <model> <timeout seconds>
set -u
w="$1"; model="$2"; to="${3:-3000}"
W=/home/user/z4-workers; G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
export PATH="$HOME/.elan/bin:$PATH"
tid=$($R task-admit "$G" --by principal --label "$w" --parent T1 2>&1 | tee "$W/$w/admit.log" | grep -o 'T[0-9]\+' | tail -1)
[ -z "$tid" ] && tid=$($R status "$G" | awk -v l="$w" '$2==l{print $1}' | tail -1)
echo "$tid" > "$W/$w/task_id.txt"
{ cat "$W/common2.txt"; echo; echo "YOUR TASK ID in the task graph is $tid (register $G)."; echo; cat "$W/$w/brief.txt"; } > "$W/$w/PROMPT.txt"
date -u +%Y-%m-%dT%H:%M:%SZ > "$W/$w/started.txt"
python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py check --ws /home/user/z4-work/pcp --as director-z4 --name "worker-$w-run1" \
  --cwd "$W/$w" --timeout "$to" --tail 5 -- \
  bash -c "claude -p --model $model --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task,WebFetch,WebSearch' < PROMPT.txt" \
  > "$W/$w/parent_check.log" 2>&1
echo "EXIT $?" > "$W/$w/finished.txt"
date -u +%Y-%m-%dT%H:%M:%SZ >> "$W/$w/finished.txt"
# release the worker and any descendants it left admitted
for t in $($R status "$G" | awk '/reservation depth/{print $1}' | sort -r); do
  p=$($R status "$G" | awk -v t="$t" '$1==t{print $NF}')
  :
done
$R task-release "$G" --by principal --id "$tid" >> "$W/$w/admit.log" 2>&1
