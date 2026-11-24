#!/bin/bash
# waits for mix runs, then clear runs, then the child's rerun (keeps <=2 cores)
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
while pgrep -f "run_mix.py" >/dev/null; do sleep 5; done
$P check --ws pcp --name clear-runs --expect-exit 0 -- python3 run_clear.py > clear_run.log 2>&1
$P check --ws pcp --name child-rerun --expect-exit 0 --cwd child -- bash -c "rustc -O -o mc_rerun mc.rs 2>/dev/null && ./mc_rerun 3.276133577 4 288 500 6 2026 rerun_main.csv && python3 analyze.py rerun_main.csv" > child_rerun.log 2>&1
