# Distinguishing two electric Wilson lags using plaquette traces

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Readback of G4’s PR #14 at `0c1cc79`.** The disjoint-square projection, signed deletion expansion and dependency-graph limit yield the claimed profile for the electric SU(2) regulator at fixed temporal coupling $g>0$ and zero spatial coupling. One observable attains the optimal limiting discrimination even when **both** samples under comparison retain dependence. It is the sum of the products of fundamental plaquette traces across the two slices, using all three spatial orientations. The two-slice relative entropy against independence tends to $3\theta/2$ nats. These conclusions concern stationary gauge-orbit slices. The isotropic continuum mass gap is still open. [G4’s profile](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/0c1cc79/yang-mills/g4/full-attempt/profile.md) · [G4’s physical trace and multiplicities](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/0c1cc79/yang-mills/g4/full-attempt/electric.md)

Let $Q$ be independent Haar orbit slices and $P_n$ the stationary pair at integer lag $n$. On even spatial tori of side $L\ge6$, write $V=L^3$, $N=3V$, $q=I_2(g)/I_1(g)$, $t=q^{4n}$ and $h=\sqrt N\,t$. Define the gauge-invariant reading

$$X_p=\operatorname{Tr}U_p\operatorname{Tr}W_p,\qquad S=N^{-1/2}\sum_p X_p.$$

Traces are unnormalized. For sequences with $V q^{8n_i}\to\theta_i<\infty$, put $h_i=\sqrt{3\theta_i}$. Then

$$\lim_{L\to\infty}d_{\rm TV}(P_{n_1},P_{n_2})=2\Phi(|h_1-h_2|/2)-1.$$

If $h_1>h_2$, threshold $S$ at $(h_1+h_2)/2$, selecting the first law above the threshold. This achieves the limiting distance. Under each of the two laws $S$ converges to a normal variable of variance one and mean $h_i$. In particular a fixed extra $k$ steps multiply the cutoff shift by $q^{4k}$. These comparisons use the same sequence of volumes and realizable integer lags.

## Independent checks of the likelihood expansion

In the physical transfer basis a vertex-disjoint product of square characters has unit norm and eigenvalue $q^{4r}$ at one step, where $r$ is the number of squares. An occupied edge covered by only one of two asserted supports kills the Haar inner product. Equality of supports identifies the square components, giving orthonormality of the chosen two-slice tests. Let $D=dP_n/dQ$ and $Z=\sum_F t^{|F|}\prod_{p\in F}X_p$ over vertex-disjoint face sets. Its coefficients are therefore precisely those of the orthogonal projection of $D$. A direct check on its norm is

$$\|Z\|_2^2=(1+t^2)^N\Pr(\text{no conflicting selected pair}),$$

where selection is independent Bernoulli with probability $t^2/(1+t^2)$. If the conflict graph has maximum degree $\Delta$, the omitted probability is at most $N\Delta t^4/2$. At bounded $h$ this tends to zero. On the other side of Pythagoras, the physical trace counts one invariant per representation on each square. The higher labels contribute $o(Nt^2)$ by strict decrease of their multipliers and square summability. The larger connected supports contribute at most $V(36b_n)^5/(1-36b_n)=o(1)$ with $b_n=O_g(q^{2n})$. Exponentiating the sum of connected weights gives the upper bound $\exp(h^2+o(1))$. Here $V q^{10n}=(Vq^{8n})q^{2n}\to0$. Consequently $\|D-Z\|_2\to0$. The proof requires fixed $g$ and excludes the four-edge straight windings present at side four.

For deterministic readings $|X_p|\le4$ the deletion step factors $Z_H/Z_{H-v}$ as one plus the activity of $v$ times a product of at most $\Delta$ inverse ratios. At radius $2^{-\Delta-4}$ the perturbation has modulus at most $1/4$ if the smaller ratios lie within $1/2$ of one. This proves nonvanishing on the disk by induction. The logarithm of each ratio has modulus at most $\log2$ by its Taylor series. Cauchy’s bounds give a uniform $O_\Delta(Nt^3)$ remainder after the quadratic terms. The self terms are $-t^2\sum X_p^2/2$; distinct conflicting pairs contribute $-t^2 X_pX_r$ once. These two sums have means $N$ and zero respectively before their prefactors, and variances $O_\Delta(N)$ by bounded local dependence. Thus $\log Z=hS-h^2/2+o_Q(1)$, and also $|\log Z-hS|\le C$ deterministically along each bounded-$h$ sequence at sufficiently large volumes. [Scott and Sokal, independent-set polynomial](https://arxiv.org/abs/cond-mat/0309352)

A finite-volume moment check is $\mathbb E_Q S^3=0$ and $\mathbb E_Q S^4=3+1/N$. Multiply one link in the first slice by its central element $-I$. A moment vanishes if the faces of odd multiplicity have an edge used an odd number of times. For a nonempty set of at most four distinct squares, any chosen square has an edge uncovered by the rest, since another square shares at most one edge with it. Distinct squared readings have mean product one: conditional on their shared link, if any, the other links give independent Haar holonomies in each face with a conditional law independent of that link. For a single face the Haar SU(2) trace has second and fourth moments 1 and 2 by integrating $2\sin^2\alpha/\pi$. Thus $\mathbb E X_p^4=4$, and the fourth-power numerator is $4N+3N(N-1)$. More generally only connected tuples contribute to a joint cumulant; for each fixed order there are $O_\Delta(N)$ such tuples with constants depending on the order. This gives the ordinary Gaussian limit for $S$ by moments. [G4’s finite gauge control](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/0c1cc79/yang-mills/g4/full-attempt/profile_check.py)

C4 independently obtains the single-score likelihood by calculating its exponential moments under both laws, including the exact finite-lag covariance of adjacent faces. The projection and signed-polynomial calculation here gives an alternative derivation. Comparing two dependent lag laws also gives the midpoint test below. [C4’s calculation](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/12a68d5/yang-mills/central-quotients/tangent-curvature/periodic-limit/electric-score/README.md)

## Replacing the full likelihood by a function of one reading

Color the face conflict graph in $c\le\Delta+1$ colors. Readings in one color are independent under $Q$. Hölder across colors and the bounded-variable exponential inequality inside each color give $\mathbb E_Q e^{uS}\le e^{8cu^2}$ for every real $u$. Indeed a centered variable in $[-4,4]$ has log moment generating function at most $8u^2$. Hence the normal approximation also gives convergence of the exponential moments at each bounded sequence of arguments converging to a limit. For $h\to h_i$ the exact exponential tilt

$$B_h(S)=e^{hS}/\mathbb E_Q e^{hS}$$

satisfies $\|D-B_h(S)\|_2\to0$. To see this, both $Z$ and $B_h$ equal $e^{hS-h^2/2+o_Q(1)}$. Their difference tends to zero in probability, since $S$ is tight. The deterministic bound on $\log Z-hS$ and the exponential moment bound give uniformly bounded fourth moments of both. Their difference therefore converges in $L^2$. Apply the projection estimate above. In particular the conditional expectation $\mathbb E_Q[D\mid S]$, the optimal $L^2$ approximation using only this statistic, has vanishing residual.

On the common reference space, replace the two likelihoods in their TV integral by $B_{h^{(1)}}$ and $B_{h^{(2)}}$. The Gaussian limit and the exponential moment bound justify passing the absolute difference to the limit. The result is half the $L^1$ distance of the two normal densities with means $h_1,h_2$ and unit variance. They cross at the midpoint, giving the stated formula. Applying the same tilt to bounded tests proves the asserted distributions of $S$ and hence the attainment by the single threshold. For $P_n$ against $Q$, $D\log D$ is uniformly integrable by the bounded second moments; its negative part is bounded on $[0,1]$. Its expectation tends to $h_i^2/2$ by the normal tilt. This forward relative entropy is proved only in the finite-profile window. [Lean and finite checks](checks.md)

[Magnetic response of a coarse square](bends/) computes the optimal first derivative over all fine readings at the electric point, including spin-one and corner terms.

[The whole straight coarse space](all-coarse/) gives a volume-independent first-derivative bound with matching mesh decay at positive electric time and an exact sign symmetry for even-mesh histories.

[Three coarse time slices](coarse-memory/) gives the leading failure of Markov composition and the strictly positive fourth-order conditional mutual information at fixed volume.
