#!/bin/bash
# Rerun of the child's code: (a) original mix6.py stream 0 (seed 7101), 200 discard, 80 meas, gap 6 -> compare with child/results80/stream0.json
# (b) checkerboard-patched copy, 4 streams same design. One process at a time (cores).
set -e
cd /home/user/z4-workers/z1-mix6/childcheck
mkdir orig cb
python3 mix6_orig.py 0 orig 200 80 6
for s in 0 1 2 3; do python3 mix6_cb.py $s cb 200 80 6; done
python3 analyze.py cb
