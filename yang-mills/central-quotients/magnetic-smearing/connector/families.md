# Necessary cost for a linear family of thin connectors

At each regulator let $h_i$ be any finite family of the angular observables with the [private-segment property](slow.md). The shapes, endpoints and orientations may vary with $i$ and with the cutoff, and their marked segments may overlap. Each packet must be exterior-measurable at its own segment and nonzero almost surely. Write $m_i$ for the number of its private links and $\delta_i=e^{-\kappa m_i/(1+\beta)}$ for the same fixed group and action. In the vacuum slice Hilbert space set $u_i=h_i-\mathbb E h_i$. The Markov or transfer norm satisfies $\|Pu_i\|_2^2=C_i(2)\le\delta_i^2$. For deterministic real coefficients let $F=\sum_i c_i u_i$. The triangle inequality gives
$$
 \|P F\|_2\le\sum_i |c_i|\delta_i,\qquad
 \nu_{F,\mathrm{phys}}([0,E_*])
 \le e^{2E_*/r}\Big(\sum_i|c_i|\delta_i\Big)^2 .
$$
The second step uses the two-step spectral moment on the physical scale. For every $n\ge2$ the connected transfer reading is also bounded by the squared sum, by contraction. No pair of distinct family members needs a common exterior on which its two trunks factor.

In particular, if $m_i\ge m_*$ and there is raw weight at least $q>0$ below a fixed $E_*$, the coefficients must satisfy
$$
 \sum_i |c_i|\ \ge \sqrt q\,\exp\!\left(\frac{\kappa m_*}{1+\beta}-\frac{E_*}{r}\right).
$$
If additionally $\sum_i c_i^2\le1$, the number of terms is at least $q\exp[2\kappa m_* /(1+\beta)-2E_*/r]$. Equal-weight averages retain total absolute coefficient one however many paths they include. These estimates cover linear combinations of already normalized angles. A ratio formed by normalizing a vector **after** a sum over paths has an extra random denominator and requires a separate argument.

For one angle, a fixed lower bound $C_r(\lfloor rt\rfloor)\ge c_0$ with $0<c_0<1$ at positive time implies $1+\beta\ge2\kappa m/\log(1/c_0)$ for sufficiently fine cutoffs. Linear growth in $r$ is thus a necessary scale for this raw positive-time assertion when $m\asymp r$. The available estimates do not locate a crossover at $\beta\asymp r$ or establish sufficiency there.
