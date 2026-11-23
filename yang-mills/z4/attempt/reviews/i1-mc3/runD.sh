#!/bin/bash
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
set -e
python3 mc3.py 3 1024 84 32 1500 6000 23 results/d3_b1024_r2 > /dev/null
python3 mc3.py 3 4096 134 32 1500 5000 24 results/d3_b4096_r2 > /dev/null
