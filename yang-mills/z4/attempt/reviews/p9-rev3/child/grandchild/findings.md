# Findings
Control (control.txt): 0 (slice 3 -> 0 on ring of 4).
(a) N=2: theta map {0:0, 1:1}: identity on slices. True.
(b) N=2: theta tau = tau^-1 theta holds, 200 polys, max diff 0 (tol 1e-9 only covers float roundoff; both sides evaluate F at the same permuted argument U_{-(s+1) mod N}).
(c) N=2: tau^2 = identity. True (max diff 0).
(b') N=6 sanity: holds, max diff 0.
Files: check.py, results.txt, control.txt, findings.md
Rerun: cd /home/user/z4-workers/p9-rev3/child/grandchild && rm -f results.txt && python3 check.py
(results.txt is opened with mode 'x', so it must be removed or moved first, otherwise the script raises FileExistsError.)
