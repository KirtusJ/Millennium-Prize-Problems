#!/bin/bash
# run_4d_v2.sh: 4D Ising grid with ising_wolff v2. Fixed seeds 2000+index. 2 parallel jobs. results/ never overwritten.
cd "$(dirname "$0")"
i=0
{
for L_K in "6 0.1415" "6 0.1425" "6 0.1435" "8 0.1445" "8 0.1455" "8 0.1465" "12 0.147" "12 0.1478" "12 0.1485" \
           "16 0.1484" "16 0.1490" "6 0.129" "6 0.133" "8 0.138" "8 0.141" "12 0.1435" "12 0.1455"; do
  set -- $L_K; i=$((i+1)); echo "4 $1 $2 1000 15000 $((2000+i)) results/d4v2_L$1_K$2.txt"
done
} | xargs -P2 -L1 ./ising_wolff
ls results/d4v2_* | wc -l
