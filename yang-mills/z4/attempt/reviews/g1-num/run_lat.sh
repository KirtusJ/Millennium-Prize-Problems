#!/bin/bash
# lattice sweep: for each beta three runs (N0,X0), (N0+16,X0), (N0+16,X0+40) ; Nt = Nx
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
set -e
for spec in "2 24 48" "4 24 48" "8 32 64" "16 32 72" "32 40 80" "64 48 96" "128 56 112" "256 72 140" "512 88 180"; do
  set -- $spec; b=$1; N=$2; X=$3
  for cfg in "$N $X" "$((N+16)) $X" "$((N+16)) $((X+40))"; do
    set -- $cfg
    python3 lat.py spec $b $1 $2 $2 results/spec_b${b}_N$1_X$2.json | head -1
  done
done
