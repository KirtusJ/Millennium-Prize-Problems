#!/bin/bash
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
set -e
for c in "16 24 1.0" "20 32 1.0" "24 40 1.0" "24 40 1.5"; do set -- $c; python3 cont.py $1 $2 $3 results/cont_K$1_L$2_w$3.json; done
