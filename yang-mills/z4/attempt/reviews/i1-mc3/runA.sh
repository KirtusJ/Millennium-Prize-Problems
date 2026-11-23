#!/bin/bash
# controls: D=3 beta=1,2,4 ; D=2 beta=256
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
set -e
python3 mc3.py 3 1 20 32 500 8000 11 results/d3_b1 > /dev/null
python3 mc3.py 3 2 20 32 500 8000 12 results/d3_b2 > /dev/null
python3 mc3.py 3 4 24 32 500 7000 13 results/d3_b4 > /dev/null
python3 mc3.py 2 256 72 32 1000 5000 14 results/d2_b256 > /dev/null
