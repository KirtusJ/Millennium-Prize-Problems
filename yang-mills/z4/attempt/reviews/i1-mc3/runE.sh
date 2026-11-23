#!/bin/bash
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
set -e
python3 mc3.py 3 4 48 32 500 4000 15 results/d3_b4_T48 > /dev/null
python3 mc3.py 2 256 72 32 1000 5000 14 results/d2_b256_r2 > /dev/null
python3 mc3.py 3 16 22 32 1000 6000 31 results/d3_b16 > /dev/null
