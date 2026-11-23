# G5 audit: lane B4 (input/b4/*.md)

Control: -ln(tanh 1) = **0.272341** (child/control.txt).

## Headline finding
B4 contains **no strong-coupling statement at all**. The words "strong coupling", "tube", "small beta", "character/cluster expansion of a correlator", "area/perimeter law" and "plaquette correlator" never occur (grep; the only "strong" is "stronger", README:41; the only "square" meaning a plaquette is README:15). B4 is **not** about two Wilson loops at times 0 and t. It is about a conditional one-link bound: you fix ("condition on") every link outside a set of marked links in **one spatial time slice**. "Positive time" enters only because any other slice is part of that conditioning exterior X. The small parameter is $s=r^m$, where $r=I_2(J)/I_1(J)$, $J=4\beta_s+2\beta_t$, and $m$ is the number of marked links per path. For every finite $J$ we have $r<1$, so $s\to0$ can come from long paths (large $m$) at **any** coupling. Strong coupling is never assumed. B4's own numerical example uses $\beta=1$, where $r=0.7627$, which is not small.

## Table

| # | file:location | verbatim quote (short) | classification | regime |
|---|---|---|---|---|
| 1 | README:11 | "Fix a compact connected Lie group ... Couplings are nonnegative ... $B=1+4\beta_s+2\beta_t$" | setup | any compact connected G; fixed finite periodic 4D lattice; any $\beta_s,\beta_t\ge0$ |
| 2 | README:13 | "The free variables are therefore independent given $X$" | PROVED (each face holds at most one marked link, README:13–15; Lean `faceFactorization`) | fixed lattice, one spatial slice, conditioned on the exterior |
| 3 | README:23 | "Thus $\chi^2(Q\Vert P_x)\le K$" | PROVED (one-line argument plus tensorization; Lean `productSecondMoment`, `reverseBias`) | any coupling; $\epsilon_e$ given |
| 4 | README:29 | "$\|\mathbb E[f\mid X]\|_2^2\le K\|f\|_2^2$" | PROVED (Cauchy–Schwarz) | **Hilbert/unit-variance** normalization; any coupling |
| 5 | README:31 | "In the defining SU(2) theory take $r=I_2(4\beta_s+2\beta_t)/I_1(\cdot)$ ... $M r^{2m}\to0$ suffices" | PROVED given rows 4 and 9 | SU(2) defining rep.; contour length $m$ in **lattice links**; any $\beta$ |
| 6 | README:35–41 | "$(D/A)^{-1}\le \mathbb E[fg]/(\mathbb E f\,\mathbb E g)\le D/A$ ... independent of the separation and temporal period" | PROVED (pointwise density bounds; Lean `positiveInsertion`) | **mean** normalization; nonnegative f, g; any slice separation (lattice steps); bound does **not** decay in t |
| 7 | README:41 | "its unit-mean fixed-time covariance remains open" | open problem, stated as open | charged heat trace |
| 8 | README:47–49 | "$\mu_f([0,E])\le e^{2aE}K$" | PROVED (duality with the transfer matrix $S=e^{-a\mathcal H}$; vacuum limit argued at README:45) | fixed finite spatial lattice, zero-temperature limit; time spacing $a$ |
| 9 | binary-experiment:5–7 | "$r_n(u)\le r^n$ ... $\|p_{e,x}-1\|_\infty\le s(4-3s+s^2)/(1-s)^3$" | PROVED (Turán inequality cited from Baricz, then Peter–Weyl); also CONTROL: my check P2, P3 | SU(2); any $J$; $s=r^m$ |
| 10 | compact-groups:24 | "$\|p_{e,x}-1\|_\infty\le C e^{-c m_e/B}$ ($m_e\ge C_0B$)" | PROVED in writing (heat-kernel and Fisher argument); constants not explicit | general compact G; large $m$ relative to $B$ (long paths), not small $\beta$ |
| 11 | binary-experiment:18–30 | table: error $1/2$, $\Phi(-2\sqrt\lambda)$, $0$ | PROVED in writing (log-likelihood expansion plus triangular-array CLT); Lean covers only `scoreMoments`, `centerParity` | SU(2); $s\to0$ "uniform in how $J$ and $m$ realize $s$" |
| 12 | binary-experiment:32 | "$\beta=1$, $J=6$ ... $m=18$ ... $M=4292$ ... error $0.158636$" vs $\Phi(-1)\simeq0.158655$ | CONTROL (numerical; controls.py is not in the inputs). I reproduced $M=4292$ and $\Phi(-1)$. | isotropic $\beta=1$: **intermediate coupling** ($r=0.7627$) |
| 13 | binary-experiment:36–39 | "$\log P_+(A^M)/P_-(A^M)=(32/(3\pi)+O(s^2))Ms$" | PROVED in writing | mean normalization, rare event; SU(2) |
| 14 | execution:21 | "2,520 plaquettes of a four-dimensional SU(2) torus ... reverses the two gauge-invariant traces" | CONTROL (numerical) | fixed small torus |
| 15 | README:55 | "$m\asymp h/b$ ... $\mu_f([0,E_b])\to0$ uniformly for $E_b=o(h/(b^2B))$" | CLAIM / derived scaling. It assumes $B=O(\log(1/b))$, an assumption with no justification. | **physical units**: fixed physical pitch $h$, spacing $b\to0$ |
| 16 | README:55, execution:13, binary:41 | "supplies neither an interacting continuum construction nor a positive lower edge"; "no construction of a continuum theory or its mass gap" | disclaimer | — |

## (a) Strong coupling
No statement is a strong-coupling statement. Coupling enters only through $r(J)<1$ for SU(2) or $B=1+4\beta_s+2\beta_t$ for a general group, and every result holds at any fixed coupling.
- Observable: bare path holonomies, or functions of them, on marked links inside one spatial slice. Contour size is $m$ = number of marked **lattice links** (README:31). Physical units appear only in the heuristic at README:55.
- Normalization: unit variance (Hilbert), README:29 and :47; and unit mean, README:35–41 and :53.
- Time separation: any number of lattice steps, including the next slice. The bounds are uniform in the separation, so there is **no decay in t** and nothing like $u^{4t}$.

## (b) The binary experiment
There are two exteriors of the actual SU(2) Wilson theory on a finite lattice, each with $M$ disjoint rectangles and $m$ marked links per rectangle. Exterior (+) sets every unmarked link to $I$. Exterior (−) puts $-I$ on one link of each return side. You observe the rectangle holonomies (equivalently their traces) and must decide which exterior holds, with equal priors.

- **Proved (written proof):**
  - The limiting optimal error as $s\to0$ is $1/2$, $\Phi(-2\sqrt\lambda)$, or $0$, according as $Ms^2\to0$, $\lambda$, or $\infty$. This shows the $Ms^2$ scale is sharp for **this two-exterior experiment**.
  - The rare-event log-ratio is of order $Ms$, which shows the first-power scale is sharp for mean normalization.
- **Lean:** only algebraic pieces, namely the score moments and parity cancellation (execution:13).
- **Control:** the numbers in binary:32 ($M=4292$, error 0.158636 vs 0.158655) and execution:21. B4 itself says the exteriors "may be very rare" and gives no lower bound for typical vacuum correlations (binary:41).

## (c) Joining tube vs disconnected squares
**There is no such statement anywhere in B4.** No tube, connected surface, or two-loop-at-times-0-and-t decomposition appears, whether for strong coupling or beyond. The nearest statements are:
- "This includes any distinct time slice, with a bound independent of the separation and temporal period" (README:41).
- "At finite temporal period the preceding bound applies at every different slice, even the next one" (README:45).

Both are conditional-density bounds valid at any coupling. Neither is a surface expansion.

## (d) Summary sentences stronger than what is proved
1. README:5: "For defining SU(2) the estimate has a sharp uniform threshold." Sharpness is shown only for an equal-prior experiment between two specially chosen, possibly very rare exteriors (binary:41). It is not sharpness of the covariance bound for typical Wilson configurations, so the summary should say "for the uniform two-exterior experiment".
2. README:31: "The exact power of $M$ is realized in two original Wilson conditional laws." This is the same caveat. "Original Wilson" is true but invites a reading about vacuum correlations.
3. README:41: "On an interacting Wilson trajectory with $\sum\epsilon_e\to0$, the connected correlation ... tends to zero." This is true given the hypothesis. But for SU(2) at fixed coupling, $\sum\epsilon_e\to0$ requires $Ms\to0$ with $m\to\infty$, i.e. very long thin paths. "Trajectory" is never defined.
4. README:55: the claim "$\mu_f([0,E_b])\to0$ uniformly" rests on the unjustified assumption $B=O(\log(1/b))$. The actual continuum scaling of $\beta(b)$ is $\sim\log(1/b)$ only perturbatively, and that is not proved. The disclaimer that follows is adequate.
5. README:7 says D4 "independently derived" the results, and execution:17 describes a "measured native kernel". These are provenance claims that cannot be checked from the inputs (controls.py, the Lean file and readback.txt are not supplied).

## Program check
`child/check_b4.py`. Its predicates were fixed in the docstring before the run, and it ran under the PCP register `check_b4` with exit 0. Results are in `child/result_check_b4.txt` (append-only):
- $r_1(6)=0.762726$ and $s=r^{18}=7.632\times10^{-3}$, giving $M=4292$ (matches B4).
- The closed form for the Peter–Weyl series matches.
- $r_n\le r^n$ holds for n ≤ 12 and u ∈ {0.5, 2, 6, 15}.
- $\Phi(-1)=0.158655$.

No tube coefficient was checked, because B4 states none. The suggested $u^{4t}$ check would test a claim B4 does not make.

PCP verify last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
