# Contact fluctuations in the original four-dimensional Wilson measure

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For periodic isotropic SU(2) Wilson histories, a smooth spatial magnetic-energy insertion has time-slice variance at least of order $b^{-5}$ in the usual $\beta/b$ normalization. The estimate holds on the **interacting lattice**, along every $\beta\to\infty$ as $b\to0$, uniformly in the box for tests supported with padding. A computable part of that variance can be removed without changing any connected two-point reading at a separation of two or more lattice time steps. The same estimate applies to prediction from the entire exterior of the slice.

The [free magnetic benchmark](../maxwell-benchmark/) computes a sharp-time variance asymptotic. The interacting estimate here bounds a removable contribution to the sharp-to-separated difference from below. The [orientation-resolved calculation](../contact-law/) evaluates the mask-averaged conditional variance in the weak-coupling vacuum. The size of the interacting separated reading and the existence of a physical mass gap remain open.

## One spatial slice

Use the normalized trace $x_p=\operatorname{Tr}U_p/2$ and Boltzmann density proportional to $\exp(\beta\sum_p x_p)$ with respect to product Haar measure. The mesh is $b$, the spatial side is $L$ in sites and the temporal period is $T$. Take $L,T\ge3$. For smooth real tests $f_{ij}$ on spatial face centers put
$$
 O_b(t)=\frac{\beta}{b}\sum_{p\ {\rm spatial\ at}\ t} f_{ij}(x_p^{\rm center})(1-x_p).
$$
Here $i<j$ label the three spatial orientations. This equation fixes the normalization of all constants below. Subtract the ensemble mean when computing covariances. The distribution of an oriented spatial face is independent of its position and, on a cubic spatial box, its mean $m_{\rm sp}$ is the same in all spatial orientations.

There is an explicit averaged conditional estimator $\widetilde O_b$ on the slice and its two adjacent layers. For periodic separations $2\le n\le T-2$,
$$
 C_b(n)=\operatorname{Cov}(\widetilde O_b(t),\widetilde O_b(t+n))
       =\operatorname{Cov}(O_b(t),O_b(t+n)).
$$
Writing $w_p=f_{ij}(x_p^{\rm center})$, define
$$
 D_b(w)=\frac{\beta^2}{b^2}\,\eta_L k_\beta\,m_{\rm sp}^2
              \sum_{e\ {\rm spatial\ at}\ t}\left(\sum_{p\ni e,\ {\rm spatial}} w_p\right)^2 .
$$
Here $k_\beta$ is the smallest single-link covariance eigenvalue over staple lengths $0\le R\le6\beta$. The mean inclusion fraction $\eta_L$ is $1/6$ for even $L$ and $(1-1/L)^2/6$ for odd $L$. Both
$$
 \operatorname{Var}(O_b)-\operatorname{Var}(\widetilde O_b)\ \ge D_b(w),
 \qquad \operatorname{Var}(O_b)-|C_b(n)|\ \ge D_b(w)
$$
hold exactly at finite cutoff. Every square-integrable predictor using only links outside the spatial links of that slice has mean squared prediction error at least $D_b(w)$, even if it uses both the past and the future. [Conditional calculation and estimator](conditional.md)

As $\beta\to\infty$, $(6\beta)^2 k_\beta\to3/2$ and $m_{\rm sp}\to1$ uniformly in volume. Take a fixed physical spatial torus with periodic smooth tests, or compact tests in padded growing boxes. In the fine-mesh limit $L\to\infty$,
$$
 \lim b^5D_b(w)=\frac{1}{36}\int \sum_{i=1}^3
                  \left(\sum_{j\ne i}f_{\min(i,j),\max(i,j)}(x)\right)^2\,d^3x .
$$
The three row sums have squared norm $\sum_{i<j} f_{ij}^2+(f_{12}+f_{13}+f_{23})^2$. Thus **every** nonzero real triple of spatial tests has this obstruction, including sign-changing smearings. For one magnetic face orientation the coefficient is $\|f\|_2^2/18$. This coefficient bounds the removed contribution. The full variance can be larger. The finite-period bound permits $n$ to vary with the cutoff, in particular to follow a fixed positive physical time.

## Time-dependent tests

A choice of masks compatible across time yields an inequality for the whole covariance matrix in lattice time. It gives a $\tanh(bE/2)$ lower reading in the zero-temperature transfer spectrum. Smooth averaging in Euclidean time still leaves at least a $b^{-4}$ variance in an ordinary history random variable. The reflection-positive norm of a field supported away from the reflection plane uses separated histories and has no such conclusion. The same four-dimensional argument covers both electric and magnetic plaquettes with arbitrary relative sign. [Time covariance, transfer spectrum and spacetime mixing](time.md) · [Lean replay and Wilson heat-bath checks](execution.md)


A second integration-by-parts identity uses two opposite links of each face. It isolates that face from every other one and proves a positive, cutoff-uniform lower coefficient for the spacetime variance loss in **all six** orientation combinations. [Two-link identity and full-rank bound](dual.md)
