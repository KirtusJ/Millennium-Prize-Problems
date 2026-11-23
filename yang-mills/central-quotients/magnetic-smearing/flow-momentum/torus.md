# The spatially summed compact Wilson observable on one finite torus

On the periodic $16^4$ compact $U(1)$ Wilson history, sum the three spatial plaquette deficits on a time slice over **all** spatial sites. Center the sum and take its readings at lattice times 1 and 2. The overall volume normalization drops out of the reflected form divided by the variance. With flow time $\tau=6$ the weak-coupling limits of the normalized forms are
$$
 Q_{\mathrm{full}}/C_{\mathrm{full}}(0)=-0.00967586795259735\ldots,\qquad
 Q_{\mathrm{spatial}}/C_{\mathrm{spatial}}(0)=+0.06038858851257660\ldots .
$$
The first sign gives strictly negative reflection norm for the bounded, exactly zero-spatial-momentum magnetic observable at all sufficiently large **finite** inverse couplings on this one torus. No $SU(2)$ tangent input or continuum limit is used. Spatial flow in the compact Wilson history preserves positive-half support at every coupling. The previous finite-torus witness measured one magnetic plaquette at a point. These numbers are for the entire magnetic sum after spatial momentum projection. [Compact Laplace limit](../spatial-flow/finite-torus.md)

For the calculation, compact abelian plaquette Haar pushforward and Laplace rescaling give a Gaussian curl with the exact two-form projection covariance. The nonlinear flow at the fixed clock has the same tangent heat multiplier, with the energy reading given to leading order by the square of the linearized curvature. Spatial summation pairs each momentum with its opposite in Wick's formula. In a face-centered Fourier basis the magnetic matrix at a fixed spatial mode is $(\lambda I-\hat{\mathbf p}\hat{\mathbf p}^{\top})F_n$, where $\hat p_j=2\sin(p_j/2)$ and $\lambda=\sum_j\hat p_j^2$. Changing the face centers introduces conjugate unitary phases at opposite momentum and preserves the trace in the sum of squares. The exact spatial zero mode of the *magnetic curl* vanishes. The external momentum of the *quadratic magnetic energy* is zero and receives contributions from opposite nonzero curl momenta.

The trace in the quadratic Wick contraction is $\operatorname{tr}(M_n M_n^\ast)=2\lambda^2 F_n^2$. For $\lambda>0$,
$$
 F_n=\frac{e^{-2\tau\lambda}}{16}
  \sum_{j=0}^{15}\frac{\cos(2\pi n j/16)}{\lambda+4\sin^2(\pi j/16)}
 \begin{cases}
 e^{-2\tau\,4\sin^2(\pi j/16)},&\text{full flow},\\
 1,&\text{spatial flow}.
 \end{cases}
$$
Thus one must **square before summing over spatial modes** in this zero-momentum quadratic reading. Tensor, volume and Wick constants cancel in the final ratio. The test is $[C(2)-2C(3)+C(4)]/C(0)$. Outward interval evaluation at 40 decimal digits gives the first three normalized readings $0.9186852719\ldots$, $0.8328952412\ldots$, $0.7374293424\ldots$ for full flow. Their six-decimal rational enclosures give a Lean-verified upper bound $-0.009674$ on the indicated linear combination. The interval calculation is independently executable. The compact Laplace limit transfers the strict sign. [Interval code](check_zero_mode.py) · [Kernel proof of the bound from the enclosures](FlowMomentum.lean)
