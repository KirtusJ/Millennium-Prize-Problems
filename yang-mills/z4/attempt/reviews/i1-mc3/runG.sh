#!/bin/bash
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
set -e
python3 mc3.py 3 16384 212 32 1500 3000 32 results/d3_b16384 > /dev/null
python3 mc3.py 3 64 34 32 1000 6000 21 rerun/d3_b64 > /dev/null
python3 mc3.py 3 256 54 32 1000 6000 22 rerun/d3_b256 > /dev/null
