# Builder report (Z4, positive arc)

Control: `control.txt` = 0.272341 (−ln tanh 1).
**Chosen: B1**, the general finite level set. It is stronger than B2, because Z_3 is the case n = 3, and the proof is elementary: split off the maximizer, bound the rest by K·e^{−bd}, then use log x ≤ x − 1. It fit the budget. B3 was delegated to the sub-agent and recompiled here.

## Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| B1 `levels_gap_le` (0 < lam1 ≤ lam0, −log(lam1/lam0) ≤ 4K e^{−bd}) | STANDS | `LevelsControl.lean`, register K2 exit 0, axioms propext/Classical.choice/Quot.sound |
| B1 `levels_physical_gap_le` (b·gap ≤ 4K·b e^{−bd}) | STANDS | same compile, K2 |
| B1 `levels_physical_gap_tendsto_zero` (b = (N+1)², gap → 0) | STANDS | same compile, K2 |
| Numerical cross-check on Z_2..Z_8 (P1) | STANDS | K1: 102 of 112 cases qualify, bound holds in all of them |
| README §3 table reproduced (P2) | STANDS | K1: every entry within 2.3e−3 relative |
| README §3 asymptote N²·k·δ·e^{−N²δ} | STANDS (measured) | K1 P3: effective constant = kδ = 2, 3, 2, 1.382, 1, 0.753, 0.586 for n = 2..8 |
| B3 (A) two-sided bounds ⇒ limit points in [c, C] | STANDS | `child/TwoSided.lean`, recompiled here as K3 exit 0, 3 standard axioms |
| B3 (A') same with bounds only eventually | STANDS | K3 |
| B3 (B) m/a → M > 0 ⇒ eventually (M/2)a ≤ m ≤ 2Ma | STANDS | K3 |
| README §1 wording "must control m_n from both sides … c·a_n ≤ m_n ≤ C·a_n" | DEFECT (wording, minor) | (B) gives the bounds only *eventually*, not for every n. The two-sided bounds are necessary for a convergent positive physical gap, but they are not sufficient: they give only limit points in [c, C], not a limit. The README text can be read as claiming more. |
| Identification of the transfer eigenvalue ratio with lam1/lam0 | NOT CHECKED | not formalized (as in the input) |

Counts: **met 4, failed 0, measured only 2**. Met: P1, P2, the B1 Lean compile (K2) and the B3 Lean compile (K3). Measured only: H, the hypothesis count, and P3, the effective constant. The README §1 wording defect is a reading, not a predicate.

## Hypotheses used (all stated in the theorem signatures of `LevelsControl.lean`)
- ι is a finite type with decidable equality. K = card ι. Real c, χ : ι → ℝ.
- `hgap`: c j ≤ c i0 − d for all j ≠ i0. This makes i0 the unique maximizer with spacing d. `d > 0` is needed only in the limit theorem (`hd`). The bound itself holds for any d, and it is vacuous or false-hypothesis unless d > 0 makes `hsmall` attainable.
- `hχ`: |χ j| ≤ 1. `hχ0`: χ i0 = 1. χ is **real-valued**, which covers the real part of a character. For Z_n with the even weight exp(b cos θ), the coefficient equals the sum with χ_j = cos(2πj/n). This identification is in the docstring, not proved.
- `hb`: b ≥ 0. `hsmall`: 2K·e^{−bd} ≤ 1, i.e. b ≥ ln(2K)/d. That is the explicit meaning of "b large". In the limit theorem it is shown to hold eventually, not assumed.
- Explicit constant C = 4K. It is loose: the sharp asymptotic constant is the sum over the next level of (1 − χ_j), e.g. 3 for Z_3 against the proved 12.
- B3: a_n > 0 for all n. In (A) the hypotheses 0 < c and c ≤ C are **unused** (Lean warns), so the limit-point statement holds without them. (B) needs M > 0 only for the interval (M/2, 2M) to be non-degenerate around M.

## Failed predicates
- None of the fixed predicates failed.
- Failed run: the first compile of `LevelsControl.lean` exited 1 with three errors (a cast of K, a `ring` after `field_simp` that had no goals left, a `neg`/`comp` congruence). These were defects of my proof script, not of the target. They were fixed, and the second compile exited 0. The failed compile was run outside the register. The register records only the passing compile K2.

## Not checked
- That the transfer eigenvalues are c_r^N, and that lam1/lam0 is the relevant ratio (character expansion). This is not formalized.
- Complex characters with lam1 complex. Several levels sharing the maximum (degenerate maximizer). The bound fails as stated there.
- No mutation test of the Lean files.
- README §2 (U(1), SU(2)) and the rest of the README were not rechecked.

## Delegated question (rule 7)
Question: prove B3 (A), (A') and (B) in Lean as stated above. Control question: 1/2 + 1/3 + 1/6, with known answer 1.
Returned: control `1` (correct). `child/TwoSided.lean` with three theorems, child register verify PASS. I reread the file: no sorry, statements as asked, and hc, hcC, hφ are unused. I recompiled it in my own register (K3, exit 0, standard axioms only). The child's "pass" is now confirmed by my own rerun, though from the same model family.

## Suggestion (not a result): a 4D analogue of the finite-group collapse
A four-dimensional analogue would have to say the following. For the Wilson action of a finite subgroup G ⊂ SU(N) on the asymptotic-freedom trajectory β(a) → ∞, the lattice-unit gap m(β) decays faster than any a(β) ~ e^{−β/(2b₀N)}. The natural mechanism is that the gap is driven by the spacing d_G > 0 between the top plaquette level and the next, so m ≲ e^{−β d_G}. Since the 4D finite-group theory is expected to freeze (a first-order transition to an ordered, Z_N-like phase at finite β), m/a → 0 or the continuum limit simply does not exist along that trajectory. The statement to aim at is therefore conditional: "any bound m ≥ c·a(β) whose proof uses only positivity, reflection positivity and a gap at each cutoff also holds for G, hence is false". This would turn the 2D collapse into a no-go test for 4D arguments. Nothing of this is proved here.

## Rerun commands
```
cd C:/Users/donke/z4-workers/builder
python -c "import math;print('%.6f'%(-math.log(math.tanh(1))))"
# levels_check.py refuses to overwrite results/levels_run1.txt; move it aside or run in a copy
PYTHONUTF8=1 python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name levels_check --expect-exit 0 -- python -I levels_check.py
PYTHONUTF8=1 python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name lean_levels --expect-exit 0 -- bash -c "cd C:/Users/donke/z4-lean && PATH=\$HOME/.elan/bin:\$PATH lake env lean C:/Users/donke/z4-workers/builder/LevelsControl.lean"
PYTHONUTF8=1 python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name lean_child_twosided --expect-exit 0 -- bash -c "cd C:/Users/donke/z4-lean && PATH=\$HOME/.elan/bin:\$PATH lake env lean C:/Users/donke/z4-workers/builder/child/TwoSided.lean"
PYTHONUTF8=1 python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```
`verify` last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

The builder, the child and the director share one model family. This is not independent review.
