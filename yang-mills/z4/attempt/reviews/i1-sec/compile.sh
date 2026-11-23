#!/bin/bash
# compile.sh BUILD_DIR : copy paper/ to BUILD_DIR, apply main_patch items 1-2, pdflatex x3, report warnings.
# Predicate: exit 0 iff all three passes exit 0, no "undefined" in final log, no Overfull > 5pt.
set -u; B="$1"; rm -rf "$B"; mkdir -p "$B"; cp -r paper/* "$B"/; cd "$B"
python3 -c "
s=open('main.tex').read()
s=s.replace('\\\\input{sec_negative}\n','\\\\input{sec_negative}\n\\\\input{sec_smallbox}\n').replace('\\\\input{refs}\n','\\\\input{refs}\n\\\\input{refs_add}\n')
open('main.tex','w').write(s)"
grep -c "sec_smallbox\|refs_add" main.tex
for i in 1 2 3; do pdflatex -interaction=nonstopmode main.tex >/dev/null 2>&1 || { echo "pass $i failed"; exit 1; }; done
grep -n "Warning" main.log; U=$(grep -ci "undefined" main.log)
O=$(grep -o "Overfull \\\\hbox ([0-9.]*pt" main.log | grep -o "[0-9.]*" | awk '$1>5' | wc -l)
echo "undefined=$U overfull_gt5pt=$O"; grep "Overfull" main.log
[ "$U" = 0 ] && [ "$O" = 0 ]
