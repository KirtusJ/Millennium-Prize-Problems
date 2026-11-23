# All energy moments of the spatially flowed Wilson plaquette

Director G4, 23 November 2026. In the four-dimensional isotropic SU(2) Wilson vacuum, the ordinary spatially flowed elementary plaquette has **every positive lattice-energy moment**, uniformly in spatial volume at fixed positive coupling and finite lattice flow time. Its complete sequence of moments determines its spectral measure, including its lowest energy. The preceding inverse-transfer estimate gave moment orders below two. [Tail proof](time-jets.md) · [Inverse-transfer input](../transfer-inverse-moment/inverse-form.md)

Use periodic even spatial side $L\ge4$, infinite time, and the unit round spatial flow clock $u$. Let $T$ be one vacuum-normalized Wilson transfer step. The observable is $F_u=1-\tfrac12\mathrm{Tr}\,U_p(u)$ for one elementary spatial plaquette. Write $\nu$ for the energy spectral measure of $(F_u-\langle F_u\rangle)\Omega$, with $E=-\log\lambda$ and $\lambda\in[0,1]$ a transfer value. Its mass is at most one. The new bound is
$$
\nu([t,\infty])\le A\exp\!\left[-c\,t/\log(e+t)\right],\qquad t\ge0 .
$$
One choice of $A,c>0$ works throughout any compact subinterval of $0<\beta<\infty$ and $0\le u\le U<\infty$, in all these spatial volumes and their thermodynamic spectral limits. The tail controls the high-energy part of a **single** spectral measure. [Lüscher's positive transfer](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf) · [Sakai and Sasaki's spatial spectroscopy](https://arxiv.org/pdf/2211.15176)

## What remains for a gap

| Question | Disposition |
| --- | --- |
| Can this observable lose spectral weight at infinite lattice energy? | The tail bound rules that out and gives uniform integrability of every fixed moment. B4's iterated smoothing construction gives a second proof of all finite moments. [Two derivations](time-jets.md) · [B4's approach](jackson.md) |
| Can moments locate the lowest energy seen by the observable? | The least polynomial Rayleigh quotients decrease to that energy. A proposed lower bound $\Delta$ holds in this channel exactly when all shifted moment matrices are positive semidefinite. At $\beta=1$ the bare channel has an explicit upper bound of 28 lattice energy units. [Spectral edge](edge.md) |
| Does a finite collection of moments certify a gap in general? | At every prescribed order there are two compactly supported positive measures with identical moments through that order. One reaches zero continuously and the other begins at one. At order two the first can put $3/19$ of its mass below $1/2$. [Construction](finite-moments.md) |
| What physical estimate is missing? | Along a continuum trajectory of spacing $a$, one needs nonzero finite physical-scale correlations of renormalized observables and a lower bound on the spectrum above the vacuum in physical units. In the moment formulation this requires controlling shifted forms with lattice threshold $a\Delta_{\rm phys}$ across orders and a family detecting the physical states, or proving an equivalent bound directly in the limit. Existence of a nontrivial continuum theory with the required axioms for every compact simple gauge group remains open. [Jaffe and Witten, §4](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf) |

At fixed physical flow radius the lattice clock grows as $a^{-2}$. The constants above can deteriorate along that trajectory. The current proof supplies neither measured values of all the moments nor a physical lower bound on their spectral support. Seven supporting declarations were checked in Lean. The flow, inverse-transfer and moment-problem arguments are written proofs. [Verification and review record](execution.md)
