# Exact gamma coordinates on Wilson histories

With the link mask and quaternion conventions of the [main calculation](README.md), center the sum of the **six** scaled actions incident to each selected link given the exterior. This radial innovation is $W_e=R(m-z)$. Let $D_R=R(1-z)$. At $R>0$ its density relative to a unit-rate gamma variable $G$ of shape $3/2$ is $l_R/\mathbb E l_R(G)$, where $l_R(y)=\sqrt{(1-y/(2R))_+}$. This follows by changing variables in $e^{Rz}\sqrt{1-z^2}\,dz$. The decreasing tilt implies stochastic domination: the covariance of the increasing indicator of an upper tail with $l_R$ is nonpositive, as is seen by integrating their signed differences over two independent copies.

Set $G_e=F_\Gamma^{-1}(F_R(D_R))$ using the conditional CDF of the deficit. The CDF is continuous. For zero staple use the continuous Haar CDF of $1-U_e\cdot v_{1+}$ using any fixed incident exterior transporter. This is gauge invariant at either endpoint. The conditional joint law of these gamma variables is the same product measure for every exterior. They are exactly independent of the exterior and of one another. Working on a coupled copy or introducing additional randomness is unnecessary.

In the monotone coupling $0\le D_R\le G_e$. The conditional squared error of the centered coordinates is at most
$$
 \mathbb E(G_e-D_R)^2\le \mathbb E(G_e^2-D_R^2)
 \le \min(15/4,105/(16R)).
$$
Indeed the tilted second moment is at least $\mathbb E[G^2l_R(G)]$, $1-l_R(y)\le y/(2R)$, and $\mathbb E G^3=105/8$. At $R=0$ retain the first bound.

On periodic four-dimensional boxes with each extent at least three the [Wilson product-cap bound](../wilson-contact/conditional.md) gives $\mathbb E(6\beta-R)\le\mathbb E\sum Y_p=O(1+\log\beta)$, uniformly in the volume. Markov's inequality on $R<3\beta$ and the preceding bounds give $\mathbb E|W_e-(G_e-3/2)|^2=O((1+\log\beta)/\beta)$. These errors are centered and conditionally independent. Consequently the same estimate times $b^4\sum f_e^2$ bounds the squared error for the weighted sum with factor $b^2$. For a fixed-direction transverse checkerboard of density $1/2$, and Riemann sums on expanding tori, the weighted independent gamma variables have Gaussian limit with variance $(3/4)\int f^2$. The characteristic-function Taylor argument in the main note applies directly to the independent variables. This scalar, **link-center-weighted** result needs no microscopic tangent theorem and no rate relating $b$ to $\beta$. The orientation-resolved result for smooth face-center weights uses the stronger vacuum inputs given in the main note.
