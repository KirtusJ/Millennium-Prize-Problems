#!/bin/bash
# stream B: SU(2) at beta 16, 64, 256
set -e
for spec in "su2 16" "su2 64" "su2 256"; do set -- $spec
  python3 cyl.py $1 $2 64 32 500 2000 $(( ${2%.*} + 1000 )) res/$1_b$2.json; done
