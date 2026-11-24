Report of a review sub-agent (same model family as the director; not independent review), as handed back; saved by the director.

**`report.md` was not written.** The Write tool refused it ("Subagents should return findings as text, not write report files"), and I did not work around the refusal. This message is the report. Programs and result files are in `/home/user/z4-workers/mod-math/`.

No mathematical error found in any statement. All findings are wording, notation or a missing clause. Target sha256 `aaec6bca…`; nothing under the repository was edited.

## DEFECT / GAP

**D1. DEFECT — proof of c:vac, lines 512–513.** `g` is the test function and then the constant 1 in one sentence. Replace with:
```latex
For bounded $g$ put $h=\mathbf 1_{A_\theta}g$. Apply~\eqref{e:ret} to the slices $0$ and $n$ of a lattice with
$T>n$ and let $T\to\infty$. By Proposition~\ref{p:vac} with the pair $(\bar h,h)$ and $j=n$ the left side tends
to $|\langle h,S_nh\rangle|$; with the pair $(|h|^2,1)$ and $j=1$, and $S_11=1$, the right side tends to
$p_{6\beta}(\theta)\|h\|^2$. Hence $|\langle h,S_nh\rangle|\le p_{6\beta}(\theta)\|h\|^2$.
```

**D2. DEFECT — proof of l:trace, lines 476–478.** The character coefficients are not "ratios of modified Bessel functions": c_n = 2(n+1)I_{n+1}(β)/β, and the convolution eigenvalue on spin n/2 is 2I_{n+1}(β)/β (checked numerically, rel. err. 5e-11). Replace "The operator $C$ is … injective~\cite{Lu77};" with:
```latex
The operator $C$ is a tensor product over the links of convolutions on $\SU(2)$ by the class function
$e^{\beta\frac12\Tr}$. On the isotypic component of spin $n/2$ this convolution is multiplication by
$2I_{n+1}(\beta)/\beta>0$ ($I_{n+1}$ a modified Bessel function), and these components span $L^2(\SU(2))$ by
the Peter--Weyl theorem. So $C$ is positive and injective (cf.~\cite{Lu77}); it has no bounded inverse;
```

**G1. GAP — tab:status line 782, caption lines 264–265.** After D2 the proof is self-contained, so the not-reread [Lu77] should not carry a step. Table cell: `proved, $\beta>0$ (positive character coefficients, Peter--Weyl)`; delete ", which cites~\cite{Lu77} for one fact".

**G2. GAP — h:budget, line 292; h:coarse.** The lag of κ_i, M_0 and P_i are undefined. Replace the opening of h:budget with:
```latex
With $K_i=1+2/(m_i\gamma_i)=1+2a_i/(\gamma_it)$, $M_0=1$, $M_i=K_1\cdots K_i$, $\kappa_i\ge0$ such that
$\|B_iA_i^{j_i}B_i\|\le\kappa_i$ for some integer $1\le j_i\le m_i$, and $\varepsilon_i$ as in
Hypothesis~\ref{h:coarse}, the series below converges and
```
In h:coarse add: `Let $P_i$ be the conditional expectation given the coarse links at mesh $a_i$, on the centred gauge-invariant functions.`

**G3. GAP — r:ret(c), after line 529.** Gauge invariance is covered, "centred" is not. Add:
```latex
The constants are also respected: $P1=1$ and $B1=0$, so the self-adjoint $P$ and $B$ map the centred
functions to themselves.
```

**G4. GAP — proof of t:inh, lines 362 and 382.** "which is not zero" has no reason; "since $A\ge0$" is the wrong reason for ‖A^m‖ = q^m. Replace with:
```latex
let $E=\mathbf 1_{[q',q]}(A)$. Since $A\ge0$ is self-adjoint, $q=\max\sigma(A)$, so $E\ne0$.
```
```latex
Let $q'\uparrow q$; since $A$ is self-adjoint, $\|A^m\|=q^m$, so
```

**G5. GAP — r:three, line 346.** "the form" is undefined and its sign is opposite to the displayed "≤". Replace with:
```latex
the quadratic form $\langle v,(rI-T)(I-T)v\rangle$ equals $0.17125$ on each of $(1,\pm1)/\sqrt2$, so the test
is passed on a spanning set, and $-0.0075$ on $(1,0)$, where it fails; $0.95\in(r,1)$.
```

**G6. GAP — s:set, line 175.** "strictly positive" → "positive and injective" (L is compact, so 0 is in its spectrum).

**G7. GAP — s:lean, after line 705.** Add:
```latex
The formal statement has real times $t>0$, $\tau\le t$, $a\ge0$, hypotheses for $e^{-2aH}$, $e^{-\tau H}$,
$e^{-tH}$ and denominator $1+2a/(\gamma t)$; Theorem~\ref{t:inh} for $A=e^{-aH}$ is the case $t=ma$,
$\tau=ja$. The file also checks the example of Remark~\ref{r:reset}.
```

## STANDS

- **(a) t:inh:** every line checks, including q = 0 (b ≤ 1 does follow from the third hypothesis), A^k ≥ q'^k E, l:scal with ρ = 2/m, and the limit. `inh_test.py`: 265,000 instances (kernel, ‖A‖ = 1, A = 0, m = j = 1, local search); least slack −4e-13 (rounding). The "‖A‖=1 generic" family qualifies only within tolerance; the two "aligned" families are the meaningful ones.
- **(b) l:trace:** half-trace, measure (one time-like link per site; slabs independent), CΠ = ΠC, W split, positive kernel, order in (e:trace) and T ≥ 2 are all right. `trace_test.py`: Z_2 and Z_3 in 1+1 dimensions (T = 3 and 2), and Z_2 with one open spatial plaquette (T = 3), agree with full enumeration to 4e-14. Controls without Π or without W fail, as they should.
- **(c) p:three, r:three:** correct.
- **(d) Hypotheses and c:acc:** consistent with t:inh (1/(m_iγ_i) = a_i/(γ_i t)); liminf claim correct; r:budget exact.
- **(e) p:vac, c:vac, B = R(I−P), r:ret(c):** correct.
- **(f) s:lean:** description accurate. `Inheritance.lean` reran with exit 0, three standard axioms, no `sorry`; the worker copy and the repository copy are byte-identical. `haar.lean` also exit 0. The toolchain in `/home/user/z4-lean` is Lean 4.19.0, not 4.12.0.
- **Quick recheck (t:crit, l:cap, t:ret, p:haar):** stand; r:ret(a),(b), R'(6) and r:haar values reproduced.

## Renaming proposal

| Collision | Change |
|---|---|
| A: operator / gate A_θ / set A in r:ret(d) | gate → $\Gamma_\theta$, set → $\Gamma$ |
| R: I_2/I_1 / multiplication by indicator / 𝖱(f) | multiplication operator → $\chi$, so $B=\chi(I-P)$ |
| M: products M_i / M_f / number of gates / m(k) | $M_f\to\mathsf M_f$; gates → $n_{\mathrm g}$; $m(k)\to\lambda_{\min}(k)$ |
| p, q: p_k(θ), q = ‖A‖ / p := R', q := R/k / exponent p in r:crit(b) | in p:haar $p\to\lambda_\parallel$, $q\to\lambda_\perp$; $Cs^p\to Cs^\nu$ |
| L: 𝖫 / L in p:haar | $L\to k_0$ |
| T: time slices / T = e^{−τH} in p:three | $T\to S_\tau$ |
| G: projection / gauge group in s:ext | drop the group letter; write $\Delta$ "depending on the group" |
| C: operator / caps C, C′ | caps → $\mathrm{Cap}_v,\mathrm{Cap}_c$ |
| g, x, y in l:trace (sites, links) vs functions and slices | end sites $e_-,e_+$; links $g_{e_-},g_{e_+}$ |
| k: tilt / integer power in the t:inh proof | $A^n\ge q'^nE$ |

Leave E, r, s, d. Update tab:sym, and drop a, t from its t:inh row.

## Method clauses

Applied: §2 (except the novelty search), §4, §5, §6, §7. Not applied: certified enclosures (double precision except exact-rational checks) and Core disposition vocabulary (Core text not in the brief).

Not done: [Lu77] and [OS78] not read; `main.pdf` not compared with the source; measurements not rechecked; programs run once, with no fresh-directory byte comparison. Same model family as the authors of the proofs, so this is not independent review.