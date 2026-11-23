#!/bin/bash
# stream A: U(1) controls and SU(2) at beta 8, 32, 128
set -e
for spec in "u1 4" "u1 16" "su2 8" "su2 32" "su2 128"; do set -- $spec
  python3 cyl.py $1 $2 64 32 500 2000 $(( ${2%.*} + 1000 )) res/$1_b$2.json; done
