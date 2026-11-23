#!/bin/bash
# predicates: E0 no '!' lines; U0 no undefined refs/cites in final log; O15 no overfull >15pt (brief); T1 'Theorem 1.1' on p.1
cd "$1" && for i in 1 2 3; do pdflatex -interaction=nonstopmode main.tex >/dev/null 2>&1; done
echo "errors $(grep -c '^!' main.log)"; echo "undefined $(grep -ci 'undefined' main.log)"
grep -o 'Overfull \\hbox ([0-9.]*pt too wide) in paragraph at lines [0-9-]*' main.log
echo "pages $(pdfinfo main.pdf | awk '/Pages/{print $2}')"
pdftotext -f 1 -l 1 main.pdf - | grep -c "Theorem 1.1"
