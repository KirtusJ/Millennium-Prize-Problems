# Clear-field mixing and cross-lattice transfer at matched coupling

At every coarse background of the four-dimensional Wilson theory, G4 obtained a volume-independent inverse-polynomial mixing bound for tests of bounded link degree on a specified set of fine links. Under logarithmically growing bare coupling the resulting refinement loss is summable even for supports growing more slowly than log N / log log N. This includes both local marks in Z4's sampler. The constant for the four-face average is very small. [Local mixing theorem and colour checks](local.md)

A complete forward and reverse sweep of the actual 24 Wilson colours defines a positive operator on a single frozen-skeleton slice. If the centered singular norm of the forward sweep is at most $q$, every gauge-invariant slice test loses at least $(1-q)/[24(1+q)]$ of its conditional variance on average over the colours. The argument redraws the off-slice environment conditional on the incoming slice. An explicit finite cover of the strictly clear coarse fields and a fine-link partition reduce a proposed lower bound to finitely many positive cell matrices at a fixed regulator. Bounding those matrix norms at the rate needed under refinement remains open. [Sweep and converse](sweep.md) · [Clear-field cover](clear-net.md)

At equal physical time, fine and coarse operators can be compared through cyclic integrals with their own stationary marginals. Alternatively, partitioning **all** observed straight links gives a rigorous Wilson upper bound on the contribution of missing eigenfunctions. One can choose a mesh to make this approximation error summable; the actual cross-regulator differences still require quantitative control. There is also an explicit finite-period correction, far too large to certify the Monte Carlo preparations here. [All-mode Wilson enclosure](partition.md) · [Cycle formula and counterexamples](cycles.md) · [Vacuum and integration errors](vacuum.md)

In a four-dimensional test at lag $\ell/5$, the largest centered eigenvalue for four bins of a straight center-neutral winding fell from .06197(257) on side five to .00408(72) on side ten. At twice the temporal period the two values were .06157(68) and .00169(47). These are restricted observables in periodic time. An exactly solvable two-dimensional compact Wilson cylinder also tests the sign of the *full* neutral comparison: naive bare scaling and fundamental matching give opposite signs at weak coupling. Eighth power sums enclose the latter sign at three finite pairs. [Matched four-dimensional ensembles](measurements.md) · [Exact cylinder analysis and controls](cylinder.md)

Z4 verified the earlier exceptional-field return and inheritance argument within its stated review scope, and deposited the two requested tunnelling-note wording repairs. G4 checked them at eb02a66. Z4 confirmed the side-six and side-eight mixing runs at the agreed couplings and periods. Our 5→10 comparison is a distinct dyadic measurement. G4 also independently integrated Auditor3’s optimized three-mark disk test, which improves the falsification probe available to the directors. [Director and auditor checks](director-review.md) · [Z4's task acknowledgment](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7117372007)

## Reproduction

Run the following Python programs from this directory with NumPy. The interval certificate uses only the standard library. The two stream archives contain the full Wilson measurement counts. The verifier checks the recursive PCP records, source pins, native source-emission readbacks and compiler controls.

```sh
python -B local.py
python -B checks.py
python -B partition.py
python -B cylinder.py
python -B intervals.py
python -B winding.py
python -B disk_marks.py
python -B verify.py
```

Supply `--runtime PATH_TO_PCP_OS_PYTHON --method PATH_TO_PCP_METHOD` to replay the registers. `lake env lean Checks.lean` with mathlib and Lean 4.19.0 checks six auxiliary real inequalities or identities, including the real-power inequality used by the gated inheritance proof. The Wilson operator arguments are manuscript proofs.
