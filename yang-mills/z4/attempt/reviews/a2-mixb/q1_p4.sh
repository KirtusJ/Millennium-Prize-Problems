#!/bin/bash
# P4: a2m and z1m6 at the same args give identical first ten columns (beta 3.276133577, d0, seed 6100001 cold and 6107920 hot, 100 burn, 30 meas).
set -e; cd /home/user/z4-workers/a2-mixb; mkdir results_p4
for h in 0 1; do s=$((6100001+7919*h))
 build/z1m6 fixed 3.276133577 $s $h 100 30 6 6 12 skeletons/d0.txt results_p4/z$h
 build/a2m  fixed 3.276133577 $s $h 100 30 6 6 12 skeletons/d0.txt results_p4/a$h
 cmp <(cut -d, -f1-10 results_p4/z$h.csv) <(cut -d, -f1-10 results_p4/a$h.csv) && echo "P4 stream $h identical"
 cmp results_p4/z$h.colours.csv results_p4/a$h.colours.csv && echo "P4 colours $h identical"
done
