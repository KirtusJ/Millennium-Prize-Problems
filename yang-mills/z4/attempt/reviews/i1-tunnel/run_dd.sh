#!/bin/bash
# all runs of ddmeas.py; results never overwritten (mode "x"); exit 1 if any run failed a predicate
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
rc=0
for a in "8 24 61 60" "16 32 81 80" "32 40 101 100" "64 48 121 120" "64 56 141 140" \
         "96 60 145 144" "96 68 161 160" "128 68 161 160" "128 76 177 176" \
         "192 84 193 192" "192 92 209 208" "256 96 217 216" "256 104 233 232"; do
  set -- $a
  python3 ddmeas.py $1 $2 $3 $4 results/dd_b$1_N$2_M$3.json || rc=1
done
exit $rc
