#!/bin/bash
# rerun corrected reducer on every archived z1-mix6 run (read-only input), outputs results_fixed/old-<tag>.json (mode x)
set -e
mkdir -p results_fixed
for t in d0 d0.5 d1 d2 clear0 clear2 clear4 L-d0 L-d0.5 L-d1 L-d2 L-d4; do
  python3 reduce_fixed.py stream /home/user/z4-workers/z1-mix6/results/$t results_fixed/old-$t.json
done
python3 reduce_fixed.py ratio results_fixed/old-L-d2.json results_fixed/old-L-d0.json results_fixed/old-ratio-Ld2-Ld0.json
