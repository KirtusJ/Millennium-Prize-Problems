#!/bin/bash
# Runs both Lean files from /home/user/z4-lean (read-only use), prints axioms.
set -e
cd /home/user/z4-lean
for f in /home/user/z4-workers/g2-fid/lean/Inheritance.lean /home/user/z4-workers/g2-fid/lean/haar.lean; do
  echo "== $f"; PATH=$HOME/.elan/bin:$PATH lake env lean "$f"
done
