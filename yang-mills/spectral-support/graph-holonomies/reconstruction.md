# All normalized graph readings and the positive-time reflection form

In the original Wilson probability space let $X$ collect the segment holonomies and let $Y$ be the exterior of their private links. Their conditional law is $K_Y$, with density $w=\prod_i w_i$ relative to the common reference $H$, product Haar. Suppose $|w_i-1|\le\delta_i<1$. Define $P=\prod_i(1-\delta_i^2)$.

For any $w_i$ of mean one, $(1-\delta_i^2)/w_i\le 2-w_i$ follows from $(w_i-1)^2\le\delta_i^2$. Thus the reverse chi-square quantity is bounded by
$$1+\chi^2(H\Vert K_Y)=\int w^{-1}\,dH\le P^{-1}.$$
With $f$ any square-integrable complex reading, subtract its conditional mean and apply Cauchy–Schwarz in $K_Y$:
$$|K_Y f-H f|^2\le(P^{-1}-1)\operatorname{Var}_{K_Y} f.$$
All integrals exist because the conditional density at each finite cutoff is bounded above and below by positive constants. Variance around its mean minimizes squared error, so $D=\operatorname{Var}(K_Y f)\le (P^{-1}-1)\mathbb E\operatorname{Var}_{K_Y} f$. Total variance now gives
$$D\le (1-P)\operatorname{Var} f,\qquad
|\operatorname{Cov}(f,g(Y))|\le q\sqrt{\operatorname{Var} f\,\operatorname{Var} g},\quad
q=\sqrt{1-P}\le\sqrt{\sum_i\delta_i^2}.$$
B4 independently obtained the reverse chi-square tensorization, proved a related bound for exterior-dependent dressings, and tested the growing-family threshold on Wilson exteriors. [B4’s theorem and conditional sharpness tests](../../transfer-operator/coarse-holonomies/)

This controls the largest normalized correlation over **all** tests of the graph and the exterior, even when the tests select increasingly rare holonomies. A two-state symmetric channel with conditional densities $1\pm\delta$ attains $q=\delta$ in the single-channel inequality. A TV bound alone does not imply such correlation control: a rare exactly copied bit has correlation one with its copy, while the joint law approaches the product of its marginals in total variation. [Lean bounds](GraphHolonomies.lean) · [Channel checks](check_graph.py)

For a spatial graph any reading on a different time slice belongs to the exterior. Adjacent slices are allowed in this one-sided argument. For two graphs with jointly independent private links after conditioning on one common exterior, conditioning both functions gives the product bound $q_1q_2$ instead. Copies on two nonadjacent slices of a temporal circle satisfy this condition. Copies on neighboring slices can have retained bonds in the same temporal plaquette and only the one-sided argument is automatic. The bounds hold on the finite circle without any spectral assumption.

In the zero-temperature positive transfer representation at a fixed spatial regulator, for any centered graph reading of unit variance,
$$\mu\{aE\le R\}\le e^R C(a)\le e^R q,$$
where $a$ is the temporal spacing. The time-circle bound passes to the vacuum for bounded functions by transfer projection at fixed spatial box and coupling, then to $L^2$ functions by truncation. Equivalently one can assume the usual positive vacuum spectral representation and this Wilson-law limit. At two time steps the independent-copy bound gives $e^{2R}q^2$. On the isotropic trajectory of the graph theorem, a fixed graph therefore loses weight even in bands $aE\le R$ of fixed width **uniformly over the normalized observable chosen at each cutoff**. This is an upper bound for a probe sector, not a lower bound on the entire Hamiltonian.

## Reconstruction of the limiting cylinder process

Use bounded cylinder functions on finite graphs located entirely at **strictly positive times**, allowing temporally extended paths as long as the whole graph stays in the open positive half-space. The graph of a function $F$ and the reflected graph of $G$ then have no common links. On their common refinement the product-Haar law gives
$$\mathbb E_H[(\Theta F)G]=\overline{\mathbb E_H F}\,\mathbb E_H G.$$
Thus the reflection form on the linear span of these cylinder functions has an exactly one-dimensional completion after quotient by its null space. This holds at every fixed reflected separation. If the reflection plane itself is included in the algebra, nonconstant boundary cylinders can have positive equal-time norm. Their centered correlation with any fixed positive-time translate is zero. For a nonconstant spatial Wilson loop with normalized centered variance one, the $L^2$ distance to any nonzero temporal translate in the Euclidean history space is $\sqrt2$. The equal-time process consequently lacks strong time-translation continuity there. The distinction between the open and closed reflection domains is necessary. [Gauge-theory reflection positivity](https://www.sciencedirect.com/science/article/abs/pii/0003491678900398)

The quantitative estimates cover growing families only under the stated private-link and error budgets. A normalization imposed only on separated correlations can give a divergent sharp-time norm and evade an inference from unit-variance decorrelation. The graph limit does not settle observables defined by spatial flow, renormalized local fields, or dense combinations of small plaquettes. These alternatives are precisely where a nonzero fixed-physical-time sector could still occur. [Z4's positive-time benchmark](../../z4/fixed-size/STATEMENT.md) · [B4's separate heat-trace probe](../../transfer-operator/spatial-heat-trace/)
