# notes T8
- control: K_c=ln(1+sqrt2)/2 -> 0.440687 (control.txt written)
- delegated T9 (exact 4x4). My own slip: I ran 'mv result.txt /dev/null', which deleted grandchild/result.txt and replaced /dev/null by a regular file; restored /dev/null (mknod c 1 3) and regenerated result.txt by rerunning ising4.py (rerun = the required reread/rerun). Exact: U4(4)=0.6171993184 <M2>=194.9078806 <M4>=43626.73935
- wolff.c written with predicates P1-P4 in header (before first run)
- MC runs L=4..64 done (res/L*.txt); P1-P3 met; P4 slope 1.7518+-0.0006 (L8-64), 1.759 (L4-64)
