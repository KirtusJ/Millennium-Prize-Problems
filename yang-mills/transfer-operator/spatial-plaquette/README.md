# The SU(2) spatial Wilson factor is extensive in global operator norm

Director B4 · 22 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

On a periodic cubic spatial slice of even side length $L\ge2$, the Wilson plaquette potential attains both its pointwise bounds on legal link configurations. This gives an exact obstruction to treating its multiplication factor as a small global perturbation, including after optimizing a scalar normalization. It concerns the spatial factor in the finite regulator. [Lüscher, construction of the lattice transfer matrix](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf)

## Simultaneous plaquette extrema

Use one $SU(2)$ matrix on each positively oriented link and its inverse for the reverse link. There are $N_p=3L^3$ positively oriented plaquettes. With the unnormalized fundamental trace, write

$$V(U)=\sum_p \big(1-\tfrac12\operatorname{ReTr}U_p\big).$$

Each term is in $[0,2]$. Identity links give $V=0$. For the opposite extreme, take the central links at site $x$ to be

$$U_0(x)=I,\qquad U_1(x)=(-I)^{x_0},\qquad U_2(x)=(-I)^{x_0+x_1}.$$

These signs are periodic because $L$ is even. For every $i<j$, translating the exponent on link $j$ by one step in direction $i$ adds one modulo two. Translating the exponent on link $i$ in direction $j$ leaves it unchanged. Thus every oriented plaquette product is $-I$ simultaneously, and $V=2N_p$. The Lean theorem checks the four oriented edges at every site for every even $L$, including wrapped edges, using the ring homomorphism from $\mathbb Z/L$ to $\mathbb Z/2$. The identification of the exponents with central $SU(2)$ matrices is elementary group algebra. [Lean source](WilsonSlice.lean)

## Consequence for a transfer estimate

Let $B_\kappa$ multiply by $\exp(-\kappa V/2)$ on the product Haar space of links, with $\kappa>0$ the coefficient of the spatial action in this normalization. Put $b=\exp(-\kappa N_p)$. The multiplier lies in $[b,1]$. Continuity and full support of product Haar measure make both endpoints essential extrema. The two neighborhoods selected by a condition on $V$ are gauge invariant. Their indicator functions therefore also test the norm on the gauge-invariant subspace. For $c>0$,

$$\|I-cB_\kappa\|=\max\{|1-c|,|1-cb|\},\qquad
\inf_{c>0}\|I-cB_\kappa\|=\frac{1-b}{1+b}.$$

The minimizing scalar is $2/(1+b)$, where the two endpoint deviations are equal and opposite. The unrescaled norm is $1-b$. Both errors tend to one as $\kappa N_p\to\infty$. Even a multiplicative scalar chosen separately for each volume cannot keep this factor close to the identity in that regime.

This rules out one proposed route from the independent-link model to the interacting transfer estimate. A bound comparing the entire multiplication factor to a scalar times the identity in global norm loses control with volume. No conclusion follows here about the gap of a normalized full transfer operator, a compression to a selected low-energy subspace, or local connected matrix elements in its true vacuum. Those quantities use additional structure. This construction uses the fundamental $SU(2)$ plaquette trace. Both center elements project to the identity in $SO(3)$. [Two-sector estimate](../README.md) · [Global gauge-group lane](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/fa3b65d022743b1e11dc4863c19a735585b88804/yang-mills/central-quotients)

## Execution

The hosted PCP search tested binary linear link exponents in lexicographic order until it obtained masks $(0,1,3)$. A separate PCP worker evaluated the four edges explicitly with modular wraparound. The two workers occupied depth two under the generation worker and root. After their exits the generation worker supplied their outputs and the fixed Lean statement to the measured PCP OS assembly guest. It emitted all 1,209 bytes of the checked Lean source. The root compared those bytes with the committed source and ran Linux-hosted Lean 4.19.0 against mathlib at the revision in the parent execution record. All four desk nodes closed at revision 8, and the guest exited zero. [Toolchain, public kernel and guest program](../execution.md) · [Replay](replay.py)

| Side length | Plaquettes with product $-I$ | Total inspected |
|---:|---:|---:|
| 2 | 24 | 24 |
| 3 | 54 | 81 |
| 4 | 192 | 192 |
| 5 | 300 | 375 |
| 6 | 648 | 648 |

The odd-side rows use canonical representatives as a deliberately out-of-scope control. They show where this assignment fails at a periodic seam and make no claim about all possible configurations on odd tori. The formal validation printed only the three standard axioms for the universal even-side theorem. Removing $x_1$ from the third link failed on the $(1,2)$ face. The norm formula above is a separate analytic argument.

The Lean source SHA-256 is `d74dab49a0245c5cfdc1e397aa382b4dc4c8da39b7daf4588a5952504af6278c`. The assembly serial SHA-256 for this run is `7d8b54f71358d712b0e80d0047a3b1edc659f7e175e3b6edfe09dec3769dae15`. To repeat, first run the parent transfer proof. From the pinned mathlib checkout, obtain the caches for `Mathlib/Data/ZMod/Basic.lean`, `Mathlib/Tactic/FinCases.lean` and `Mathlib/Tactic/NormNum.lean`. From this directory run `python3 replay.py /path/to/completed-transfer-run new-output-directory`.

