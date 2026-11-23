# The influence obstruction also occurs near a flat Wilson field

One might discard the nearly cancelling staples in the [worst-exterior example](influence.md) and apply the single-link total-variation argument only to exteriors admitting a weak-field completion. Even a fixed upper bound of two on **every scaled plaquette cost** in that completion does not make the uniform row contraction hold as $\beta\to\infty$.

Set every link to identity. For one of the six opposite parallel links $f$ of a given link $e$, change $f$ alone to $\cos\theta+i\sin\theta$, $\theta=2/\sqrt\beta$. Both exteriors admit the completion $u_e=1$. Each affected face then has scaled cost $\beta(1-\cos\theta)\le 2$, independently of the side. With the convention in the [one-link integration](README.md), the staples for $e$ sum respectively to $6$ and $5+\cos\theta+i\sin\theta$ (either sign of the imaginary direction gives the same distance). Neither conditional staple norm is small.

More generally set $\theta=c/\sqrt\beta$ with fixed $c>0$. Under the unmodified Wilson one-link conditional, let $w=\sqrt{6\beta}\operatorname{Im}u$. Its limiting laws under the two exteriors are three-dimensional unit-covariance Gaussians with means $0$ and $(c/\sqrt6,0,0)$. On the northern patch $u_0>1/2$ Haar measure has a density proportional to $(1-|w|^2/(6\beta))^{-1/2}$ on the rescaled ball. After subtracting the constant at $w=0$, the modified log weight is
$$
 \beta(5+\cos\theta)(u_0-1)+\beta\sin\theta\,w_1/\sqrt{6\beta}
 \ \longrightarrow\ -|w|^2/2+(c/\sqrt6)w_1 .
$$
For large $\beta$ both patch densities are dominated before normalization by $2\exp[-|w|^2/3+c|w|/\sqrt6]$ using $1-u_0\ge |w|^2/(12\beta)$. The complementary cap has exponentially small mass after normalization: its exponent loses a constant times $\beta$ relative to the identity, whereas a ball of radius $\beta^{-1/2}$ about the identity has Haar volume of order $\beta^{-3/2}$ and bounded relative exponent. Dominated convergence gives convergence in total variation on the common patch and vanishing mass elsewhere.

The separating half-space at the midpoint of the means gives the limiting distance $2\Phi(c/(2\sqrt6))-1$, where $\Phi$ is the standard normal distribution function. By symmetry the six opposite links each contribute at least this much in the supremum over such exteriors. At $c=2$ the sum of these six lower bounds tends to about 1.90. Thus a uniform worst-exterior proof of this type still fails on perturbatively scaled changes around the flat field. This tests the original Wilson conditional on the stated exteriors; changing the law by imposing a hard cutoff on the updated link is a different operation.

For an independent finite-$\beta$ test integrate the transverse angle on $S^3$. The projection onto $(u_0,u_1)$ has uniform measure on the unit disk. The density depends only on that pair, so its total-variation distance is the exact disk integral of half the absolute difference of the two normalized weights. The [numerical check](controls.py) instead uses the probability of the separating half-space. It supplies a lower bound at each finite coupling and approaches the same Gaussian limit.
