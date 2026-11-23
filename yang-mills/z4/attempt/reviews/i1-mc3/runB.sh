#!/bin/bash
# production: D=3, beta=64,256,1024,4096, T ~ 25 xi0 (xi0 = beta^(1/3)/3), even
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
set -e
python3 mc3.py 3 64 34 32 1000 6000 21 results/d3_b64 > /dev/null
python3 mc3.py 3 256 54 32 1000 6000 22 results/d3_b256 > /dev/null
python3 mc3.py 3 1024 84 32 1500 6000 23 results/d3_b1024 > /dev/null
python3 mc3.py 3 4096 134 32 1500 5000 24 results/d3_b4096 > /dev/null
