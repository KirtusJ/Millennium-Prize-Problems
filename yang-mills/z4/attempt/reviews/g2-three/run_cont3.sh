#!/bin/bash
# recorded continuum runs (1 thread each, sequential)
set -e
export OMP_NUM_THREADS=1
python3 cont3.py ctrl 10 2.0 results/cont3_ctrl.json
for N in 12 16 20 24; do python3 cont3.py h3 $N 2.0 results/cont3_N${N}_w2.json; done
python3 cont3.py h3 24 1.5 results/cont3_N24_w1.5.json
