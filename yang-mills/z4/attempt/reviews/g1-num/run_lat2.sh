#!/bin/bash
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
set -e
b=1024; N=112; X=220
for cfg in "$N $X" "$((N+16)) $X" "$((N+16)) $((X+40))"; do set -- $cfg; python3 lat.py spec $b $1 $2 $2 results/spec_b${b}_N$1_X$2.json | head -1; done
