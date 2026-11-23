#!/bin/bash
# reruns the HP grid (needs fresh dir or removal of res_*.txt: files opened with "x")
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
for spec in "64 102" "64 204" "64 408" "256 202" "256 404" "256 808" "1024 404" "1024 808" "1024 1616" "4096 806" "4096 1612"; do
  set -- $spec
  [ -f res_$1_$2.txt ] || $P check --ws pcp --name hp_$1_$2 --expect-exit 0 -- python3 hp.py $1 $2 > log_$1_$2.txt 2>&1
done
