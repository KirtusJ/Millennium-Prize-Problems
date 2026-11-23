#!/bin/bash
# run_4d.sh: 4D Ising grid for P2a/P2a'/P2b/P2c. Fixed seeds = 1000+index. 2 parallel jobs. Results in results/ (never overwritten).
cd "$(dirname "$0")"
i=0
{
for L_K in "6 0.128" "6 0.131" "6 0.134" "8 0.137" "8 0.139" "8 0.141" "12 0.143" "12 0.1445" "12 0.146" \
           "6 0.141" "6 0.1425" "6 0.144" "8 0.1445" "8 0.1455" "8 0.1465" "12 0.147" "12 0.1478" "12 0.1485" \
           "16 0.1482" "16 0.1488" "16 0.1492"; do
  set -- $L_K; i=$((i+1)); echo "4 $1 $2 2000 40000 $((1000+i)) results/d4_L$1_K$2.txt"
done
} | xargs -P2 -L1 ./ising_wolff
ls results/d4_* | wc -l
