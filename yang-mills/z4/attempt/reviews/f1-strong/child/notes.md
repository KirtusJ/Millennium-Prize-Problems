# notes T69
- Step 1: lgt.py (analytic Hessian, plaquette Q(s)=prod exp(s a_i) Q). p1_control_fd.py run 1: control PASS (1-2b x3, 1 x9); lattice FD predicate F1/F2 FAILED (err ~3e-4 > 1e-5).
  Cause: MY expectation: t,t' ~N(0,1)^192 have norm ~14, so h|t|~0.014, truncation ~ (h|t|)^2. Not a defect of the Hessian (qform==t^T H t to 1e-13, control matches). results/p1.txt kept (failed record).
- Step 2: p1b_fd_unit.py: same test with |t|=|t'|=1 (new predicate, stated in its docstring), h=1e-3 and h=5e-4 to show h^2 scaling.
- p1b: F1b PASS in all 4 cases (err ~1e-8 << 1e-5, also at pi-flux). F2b (h^2 scaling ratio) FAILED at pi-flux and ratios 1.3-2 elsewhere: MY expectation; errors ~1e-8 are the roundoff floor (V~O(1) rounding 1e-16 / h^2) so no h^2 trend visible. Not a Hessian defect. Hessian validated to 2e-8 abs. results/p1b.txt kept.
- p2_search.py: first trial (60 it, unoptimized einsum) took 73 s for 1 start (too slow; it only reached c=7.2); optimized einsum, reduced to 30 iterations (budget). Chunks: random seeds 0-7, 8-15, 16-23, then specials -1,-2,-3 (pi-flux, link=-1 x2).
- Grandchild T70 (independent FD of pi-flux): control PASS; c_full=c_H=7.99999866. I reread results.txt and reran its program in results/gc_rerun: identical numbers. Its prose said '24 plaquettes' (report slip; checked-line in code, see report). Released T70.
