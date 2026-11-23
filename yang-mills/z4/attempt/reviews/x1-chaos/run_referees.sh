#!/bin/bash
# run_referees.sh -- launch referee children two at a time, each admitted under T188 and recorded in pcp/.
cd /home/user/z4-workers/x1-chaos
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
run_one () {
  k=$1
  out=$($R task-admit $G --by principal --label x1-chaos-child-$k --parent T188 2>&1); echo "$out" > reports/admit_$k.log
  tid=$(echo "$out" | grep -o 'T[0-9]\+' | head -1)
  echo "$k $tid $(date -u +%FT%TZ) start" >> reports/timeline.txt
  $P check --ws pcp --name child-run-$k --cwd planted/$k --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' --output-format stream-json --verbose < ../../prompts/$k.txt > ../../reports/$k.jsonl 2> ../../reports/$k.err" > reports/check_$k.log 2>&1
  echo "$k $tid $(date -u +%FT%TZ) end" >> reports/timeline.txt
  if [ -n "$tid" ]; then $R task-release $G --by principal --id $tid > reports/release_$k.log 2>&1; fi
}
for pair in "1 2" "3 4" "5 6" "7 8" "c1 c2"; do
  set -- $pair
  run_one $1 &
  sleep 45
  run_one $2 &
  wait
done
echo ALLDONE >> reports/timeline.txt
