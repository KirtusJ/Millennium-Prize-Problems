#!/bin/bash
# run_ensemble.sh LABEL BETA N T BASESEED : 16 chains (even i cold, odd i hot), seed = BASE + 7919*i,
# burn 500 HB sweeps, 500 measurements every 3 sweeps; 2 parallel processes. Outputs results/LABEL/chain-i.txt (create_new).
set -euo pipefail
L=$1; B=$2; N=$3; T=$4; S=$5
D=/home/user/z4-workers/e2-cross
mkdir -p $D/results/$L
for i in $(seq 0 15); do echo "$i"; done | xargs -P 2 -I{} bash -c "$D/src/cross $B \$(( $S + 7919*{} )) \$(( {} % 2 )) $N $T 500 500 3 $D/results/$L/chain-{}.txt"
ls $D/results/$L | wc -l
