#!/bin/bash
# recorded lattice runs, 1 thread (continuum N=28 runs concurrently on the other core)
export OMP_NUM_THREADS=1
rc=0
python3 lat3.py v0 2 8 48 results/lat3_v0_b2_N8.json || rc=1
python3 lat3.py dec 2 8 48 results/lat3_dec_b2_N8.json || rc=1
python3 lat3.py dec 4 8 48 results/lat3_dec_b4_N8.json || rc=1
for b in 0.01 1 2 4 8; do for N in 6 8; do python3 lat3.py full $b $N 48 results/lat3_full_b${b}_N${N}.json || rc=1; done; done
python3 lat3.py full 4 8 64 results/lat3_full_b4_N8_MA64.json || rc=1
for b in 2 4 8; do python3 lat3.py full $b 10 48 results/lat3_full_b${b}_N10.json || rc=1; done
exit $rc
