#!/bin/sh
# Fetch the six permitted documents into ref/ (nothing else).
# Predicates fixed before first run:
#  P1 each URL returns a file whose first 4 bytes are "%PDF" (expectation; failure = fetch/site defect, not target).
#  P2 no existing file in ref/ is overwritten (skip if present).
# Exit code: 0 always; failures are recorded in ref_fetch_log.txt (never overwritten: appended with timestamp).
cd "$(dirname "$0")/.."
LOG=fetch_log.txt
date -u >> $LOG
f() { out="ref/$1"; url="$2"
  if [ -e "$out" ]; then echo "SKIP exists $out" >> $LOG; return; fi
  curl -sSL --max-time 90 -A "Mozilla/5.0 (literature-reader)" -o "$out" "$url"; rc=$?
  magic=$(head -c 4 "$out" 2>/dev/null)
  echo "$1 rc=$rc size=$(wc -c < "$out" 2>/dev/null) magic=$magic P1=$([ "$magic" = "%PDF" ] && echo met || echo FAILED)" >> $LOG; }
f jaffe_witten.pdf https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf
f chatterjee_1803.01950.pdf https://arxiv.org/pdf/1803.01950
f chatterjee_1602.01222.pdf https://arxiv.org/pdf/1602.01222
f chatterjee_2401.10507.pdf https://arxiv.org/pdf/2401.10507
f driver_1987.pdf "https://mathweb.ucsd.edu/~bdriver/DRIVER/Papers/Drivers_Papers/A1-U(1)_4-Lattice.pdf"
f dimock_1304.0705.pdf https://arxiv.org/pdf/1304.0705
exit 0
