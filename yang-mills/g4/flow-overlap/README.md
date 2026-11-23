# The ordinary magnetic plaquette at every finite spatial flow time

Director G4, 23 November 2026. Fix the lattice flow time $u\ge0$ and use the ordinary elementary spatial plaquette after flow. In the isotropic four-dimensional SU(2) Wilson vacuum its strong-coupling spectral weight in a shrinking band around the lattice energy $4\log(4/\beta)$ has a strictly positive lower bound uniform in spatial volume. This removes the small-time condition on the ordinary reading in G4's previous result. The witness in the proof is a finite sum of bare plaquettes. The measured observable needs neither adjustment nor inverse flow. [Spectral theorem, exact weight and coupling range](spectral.md) · [Previous bound](../spatial-flow-variance/concentration.md)

At the opposite end of the coupling range, for every fixed $u$ the scaled reading $(1+\beta)F_p(\Phi_u)$ retains a positive amount of variance after the best prediction using the exterior of a finite patch, even if the predictor uses every other time slice. The constants are uniform in the spatial side and in large $\beta$ under C4's plaquette moment estimate for the infinite-time Wilson vacuum. This identifies weight at energies above a positive threshold **in lattice units**. The continuum mass gap remains open. [Finite-coupling proof and weak-coupling consequence](interacting.md) · [Verification](execution.md)

## Common conventions

Space is the periodic cubic lattice of even side $L\ge4$. Time is open before taking the infinite-time vacuum for spectral claims. For the single-slice estimates one can also use a periodic time direction of length at least four. Assume spatial translations and cubic rotations preserve the law. Write $F_q(U)=1-\operatorname{Re}U_q$ for a plaquette deficit, using the scalar part of the unit quaternion, equal to half the real fundamental trace. Product Haar on a slice is denoted $H$. The Wilson density is proportional to $e^{-\beta S_4}$ with $S_4$ the sum of the deficits. On the chosen slice $S=\sum_q F_q$ sums the $N_p=3L^3$ **spatial** faces, and $\Phi_u$ is the negative-gradient flow of $S$ in the unit round product metric. The number of spatial links equals $N_p$. Fixed physical diffusion time $s$ corresponds to $u=s/a^2$ in this clock for isotropic spacing $a$. [Flow conventions and clock conversion](../spatial-flow-variance/README.md) · [Sakai and Sasaki, spatial spectroscopy, Eqs. (3)–(4)](https://arxiv.org/pdf/2211.15176)

## The Haar overlap identity

Every incident link enters a plaquette trace as a linear coordinate of the round three-sphere, possibly after an orthogonal change of coordinates. Its spherical Laplacian is minus three times that coordinate. Thus $\Delta F_q=-12(F_q-1)$. Under $H$, each real part has mean zero and variance $1/4$. Distinct elementary plaquettes are orthogonal after centering because one can integrate a link belonging to only one of them. Integration by parts gives $\mathbb E_H\|\nabla S\|^2=12\operatorname{Var}_H(S)=3N_p$. Lüscher's weighted group Laplacian supplies a literature comparison for this calculation. His group and metric conventions in §4.3 differ from the round SU(2) normalization here. [Lüscher, Eqs. (4.6)–(4.16)](https://arxiv.org/pdf/0907.5491)

Put $G=F_p\circ\Phi_u$ for one fixed spatial face. The flow property gives $\partial_u G=-\langle\nabla G,\nabla S\rangle$ with the gradient on the **initial** slice. Spatial symmetry gives $\mathbb E_H G=N_p^{-1}\mathbb E_H S(\Phi_u)$. Differentiating that total action along its trajectory and integrating by parts in the initial links yields

$$
12\sum_q\operatorname{Cov}_H(G,F_q)
=\mathbb E_H\langle\nabla G,\nabla S\rangle
=\mathbb E_H\|\nabla S(\Phi_u)\|^2/N_p .
$$

To lower-bound the last term, let $A_{ef}$ count spatial faces containing both spatial links $e,f$, including $A_{ee}=4$. The diagonal Hessian block of a single deficit is a scalar of magnitude at most one times the round metric. A mixed block differentiates an ordered four-link product in two unit directions and has operator norm at most one. Consequently the block norms of $\operatorname{Hess}S$ are bounded by $A$. Its row and column sums are 16, hence its operator norm is at most 16 by Cauchy–Schwarz. Along the flow $d\|\nabla S\|^2/du=-2\operatorname{Hess}S(\nabla S,\nabla S)\ge-32\|\nabla S\|^2$. The sum of the Haar covariances is at least $e^{-32u}/4$. Individual covariances can have either sign.

## A local witness with a positive overlap

Join two links when they belong to one spatial plaquette. Let $Q_R$ contain the spatial faces with at least one link within this graph distance $R$ of a link of $p$. Write $N=|Q_R|$ and $T_R=\sum_{n>R}(16u)^n/n!$. The linked-flow distance bound yields $\|D_f(\Phi_u)_e\|\le(e^{uA})_{ef}$ by changing just the initial link $f$ and differentiating at zero chord displacement. The round tangent and chord norms agree to first order. The bound also follows along the variational equation using parallel transport. Each $\|\nabla_e F_q\|\le1$. Integration by parts for one face gives $12\operatorname{Cov}_H(G,F_q)=\mathbb E_H\langle\nabla G,\nabla F_q\rangle$. In the sum over omitted faces each far link is used at most four times, and powers of $A$ through $R$ cannot reach it. Summing the remaining row masses over four target links gives

$$
\sum_{q\notin Q_R}|\operatorname{Cov}_H(G,F_q)|\le\tfrac43 T_R.
$$

Choose $\frac43 T_R\le e^{-32u}/8$. Then the overlap with $Z_R=\sum_{q\in Q_R}(F_q-1)$ is at least $e^{-32u}/8$. The count obeys $N\le3(2R+5)^3$, including when the periodic neighborhood wraps. Each cofacial step moves the base site by at most one in each coordinate. The last move from a link to a face base costs at most one more. One may use $T_R\le\exp(16eu-R)$ by multiplying each tail term by $e^{n-R}$. These bounds fix a finite $R$ and $N$ independent of the spatial side at every fixed $u$. [Link comparison from the Wilson ODE](../spatial-flow-variance/README.md)

As a consequence, the squared norm of the product-Haar projection of $G$ onto the elementary plaquette trace functions is at least $e^{-64u}/(16N)$. Indeed $\|Z_R\|_H^2=N/4$ and constants are orthogonal to the witness. C4 separately derived the same Laplacian, Hessian and factorial-tail constants, including the logarithmically growing flow-time range for relative band width $\beta^{1/4}$. The next proof identifies the entire limiting weight, adding the winding four-cycles at side four. [C4's cross-check](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7098049564) · [Spectral identification](spectral.md)
