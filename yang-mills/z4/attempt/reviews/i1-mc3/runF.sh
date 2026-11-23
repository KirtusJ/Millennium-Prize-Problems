#!/bin/bash
# recorded reruns: child's program at beta=2 (exact args from child report, own output name), then v1 controls with identical seeds
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
set -e
(cd xcheck && python3 child_mc3.py 2 128 300 9000 child_rerun_b2.json > /dev/null)
python3 mc3.py 3 1 20 32 500 8000 11 rerun/d3_b1 > /dev/null
python3 mc3.py 3 2 20 32 500 8000 12 rerun/d3_b2 > /dev/null
python3 mc3.py 3 4 24 32 500 7000 13 rerun/d3_b4 > /dev/null
