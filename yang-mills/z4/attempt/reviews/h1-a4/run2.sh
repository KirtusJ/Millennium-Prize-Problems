#!/bin/bash
# sweep for item (d); one core
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
set -e
python3 transfer2.py 64 32 80 results/t2_v0_b64.json v0 60
for spec in "32 40 96" "32 56 128" "64 48 112" "64 64 144" "128 64 144" "128 80 176" "256 80 176" "256 96 208"; do
  set -- $spec
  python3 transfer2.py $1 $2 $3 results/t2_b$1_N$2_M$3.json 2>&1
done
