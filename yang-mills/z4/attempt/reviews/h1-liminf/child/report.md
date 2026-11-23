# T90 report: numeric check of (A)-(D)

**Control:** I_1(1)/I_0(1) = 0.446390 (control.txt). Code validated on I0(1), I1(1), I0(10), I1(10) against known values (rel err < 1e-14), and on the continued-fraction ratio against the series.

**Method:** Decimal at precision 70. Ratios r_nu by backward continued fraction, started at two depths. A grid point counts only if the two agree to 1e-40 relative, and none were rejected. kappa_n is the product r_1..r_n. Tolerance 1e-25 absolute (far above the 1e-40 truncation error, far below any real slack). Program `bessel_check.py`; the predicates are fixed in its docstring. No randomness.

| Pred | cases qualifying (all evaluated) | result | smallest slack |
|---|---|---|---|
| A | 5614 / 5614 | met, 0 failures | abs 6.03e-13, rel 9.67e-10 at nu=400, x=0.5 |
| B | 5614 / 5614 | met, 0 failures | abs 2.50e-9, rel 2.50e-9 at nu=0, x=10000 |
| C | 5614 / 5614 | met, 0 failures | exactly 0 (equality) at n=0, every beta. Smallest positive: 3.0e-8 abs on the lower side (rel 1.5e-4 of the upper bound) at n=1, beta=10000 |
| D | 2984 / 2984 | met, 0 failures | exactly 0 (equality) at n1=n2=0 (M=0 cases included). Smallest positive: abs 9.9e-6, rel 2.8e-3 at m=0.05, beta=10000, M=5, n1=n2=5 |

- D covers beta in {100, 200, ..., 10000}, 4 values of m, and all 0<=n1,n2<=M. M stays at most 30, so it never touches the n<=400 limit.
- Failed predicates: none, so there is nothing to attribute to my expectations or to a defect in the target. The only exact-zero slacks are the trivial n=0 equalities.
- Caveat: this is a finite grid check, not a proof.
- Run history: a first run wrote results.json (outside the PCP check, before I added the argv output name and the positive-slack tracking). The checked run wrote results_checked.json, same counts.

**Grandchild:** task T92, label h1-liminf-grandchild, parent T90, released after it returned.
- Question: independently recompute -ln kappa_1 and -ln kappa_2 at beta=1000 and 10000 against (C), and the tightest case of (B).
- Control: it got 0.446390 for the control.
- Outcome: all met. At beta=10000, n=1: -ln kappa = 0.00015000750018744, lower bound 0.00014997750337449, slack 2.9996813e-8. For (B), nu=0, x=10000: slack 2.5001250e-9. Both match my numbers.
- I reread result.md and reran chk.py in a fresh scratch directory. The output was identical.
- Its stated limits: finite cases only, a single series method, no cross-check from a continued fraction.

**Rerun commands** (from this directory, with new output names because files are never overwritten):
- `python3 bessel_check.py results_rerun.json`
- `python3 grandchild/chk.py` in an empty directory
- `P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P check --ws pcp --name bessel_check --expect-exit 0 -- python3 bessel_check.py results_rerun2.json`

**PCP OS verify, last lines**
- `pcp_os.py verify --ws pcp`: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
- `pcpos verify pcp/register.jsonl`: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.

(`init` reported the method as not pinned, as expected. The task graph events were T92 admitted (event 181) and released (event 183).)
