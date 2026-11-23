#!/bin/bash
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
rc=0
for a in "192 100 225 224" "192 108 241 240" "256 120 265 264" "256 132 289 288"; do
  set -- $a; python3 ddmeas.py $1 $2 $3 $4 results/dd_b$1_N$2_M$3.json || rc=1
done
exit $rc
