#!/bin/bash
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
set -e
python3 transfer2.py 512 104 224 results/t2_b512_N104_M224.json
python3 transfer2.py 512 120 256 results/t2_b512_N120_M256.json
python3 transfer2.py 1024 128 272 results/t2_b1024_N128_M272.json - 110
