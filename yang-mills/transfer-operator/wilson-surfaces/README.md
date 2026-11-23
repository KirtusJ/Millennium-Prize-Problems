# Ordinary Wilson rectangles at positive time in strong coupling

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00) · Millennium Prize Problems, Yang–Mills

On the original isotropic four-dimensional SU(2) Wilson lattice, the ordinary signed rectangle trace divided by its mean can have a **diverging connected correlation at fixed positive physical time**. In the same ensemble the positive charged spatial heat trace divided by its mean has **vanishing connected correlation** at every fixed positive separation. Both statements hold in an explicit strong-coupling region. They answer parts of the normalization question raised by Z4. Small inverse bare coupling is essential here. The weak-bare-coupling trajectory relevant to the asymptotically free theory remains open. [Positive heat-trace result](positive-probes.md) · [Z4’s Maxwell comparison](../../z4/fixed-size/WILSON_LOOP.md)

Use the infinite-volume translation-invariant Wilson state with normalized real fundamental trace in the action and lattice spacing $b$ on every axis. Take the spatial and temporal couplings equal to $\beta>0$. Draw a planar $n\times m$ rectangle at time zero and translate it by $k\ge1$ time steps without a spatial displacement. Write $A=nm$, $P=2(n+m)$, $W_t=\operatorname{Tr}U_{C_t}$, $w=\mathbb E W_0$, and $J_k=\mathbb E W_0W_k$. The fundamental trace is real and can change sign. All normalized ratios below are identical for the trace divided by two.

Define
$$
p=1-e^{-2\beta},\quad H=384,\quad u=2Hp,\quad
r=I_2(\beta)/I_1(\beta),\quad D_{\rm link}=e^\beta/(2I_1(\beta)/\beta),
\quad q=r e^{-20\beta}/D_{\rm link}.
$$
For $Hp\le1/4$, let $d_k=\min(2A,Pk)$. Uniformly in the side lengths and separation,
$$
 2q^A\le w\le168 u^A,\qquad
 \max\{w^2,4^{1-k}q^{Pk}\}\le J_k\le336 u^{d_k}.
$$
The area upper bound comes from random active plaquettes after conditioning on the quotient by the center. A cubical slicing argument gives the exact minimum number of faces. For the lower bounds, positivity of the transfer and one known eigenline of the product of electric kernels suffice. In particular $w$ is strictly positive at every finite rectangle. [Center and geometry](center-surfaces.md) · [Transfer and charged open line](transfer-floor.md)

## A fixed positive separation

Choose integers depending on $b$ such that $nb\to X>0$, $mb\to Y>0$ and $kb\to T>0$. Write $A_*=XY$, $P_*=2(X+Y)$. Hold any admissible $\beta>0$ fixed. The estimates give
$$
 \liminf_{b\downarrow0} b^2\log\frac{J_k}{w^2}
 \ \ge\ 2A_*\log(1/u)-P_*T\log(1/q).
$$
Thus the mean-normalized connected correlation $J_k/w^2-1$ diverges whenever $0<T<(2A_*/P_*)\log(1/u)/\log(1/q)$. The constants are conservative; this is a sufficient interval at fixed bare coupling. In this region the full centered transfer also has norm at most $1/3$ per lattice step. Its physical excitation energies grow at least as $\log(3)/b$. A small vacuum mean and a diverging equal-time norm permit the positive-time divergence under mean normalization. [Uniform interacting transfer bound](../strong-coupling/)

The small mean of this signed trace comes from cancellation. Mark the interior links on the four sides and apply the uniform coarse-holonomy estimate. Their joint law converges to four independent Haar links, so the loop product converges in total variation to Haar. Both signs have limiting probability $1/2$, $\mathbb E|W|\to8/(3\pi)$, and $\mathbb E W^2\to1$. In particular unit-variance and unit-mean normalization probe different matrix elements even though this equal-time distribution stays nondegenerate. [Full graph law and the single-path error](../coarse-holonomies/)

## Exact rate as the inverse bare coupling tends to zero

Now let $\beta=\beta(b)\downarrow0$ at any rate and write $L_b=|\log\beta(b)|$. The small-argument Bessel expansion gives $q\sim\beta/4$ and $u\sim1536\beta$. Consequently
$$
\begin{aligned}
 \frac{b^2}{L_b}\log w &\longrightarrow -A_*,\\
 \frac{b^2}{L_b}\log J_k &\longrightarrow -\min(2A_*,P_* T),\\
 \frac{b^2}{L_b}\log(J_k/w^2)&\longrightarrow (2A_*-P_* T)_+ .
\end{aligned}
$$
Indeed the two lower bounds furnish the two competitors, and the upper bound charges their minimum. The $k\log4$ penalty is $o(L_b/b^2)$. A square of physical side $X$ has crossover $T=X/2$ on this logarithmic scale. Below it the tube outweighs the disconnected contribution. Above it the leading area exponent of $J_k$ agrees with that of $w^2$. Its subleading behavior depends on information beyond this bound.

When $|\log\beta|\gg b^{-2}\log(1/b)$, the first nonzero Haar coefficients also control the **full four-dimensional** answer. With $z=\beta/4$, the ratio is asymptotic to $z^{Pk-2A}/4$ below the integer area crossover; it tends to $5/4$ at exact equality and to $1$ above. Thus at exact equality the mean-normalized connected reading tends to $1/4$. For $|\log\beta|b^2\to\infty$, subtracting the vacuum identifies a narrower tube with $A$ possible locations and fixes the relative connected asymptotic. The fixed-coupling long-separation relative limit remains open here. [Connected rectangles](../connected-rectangles/) [Four-dimensional prefactor proof](prefactors.md) · [Controls and formal coverage](execution.md)

## Which energies contribute after propagation?

Let $S$ be the vacuum-normalized transfer and $E_\ell=-\log S$ its energy in lattice-time units. The spectral measure of $W\Omega$, including the vacuum atom $w^2$, is positive. At separation $k$, reweight it by $e^{-kE_\ell}/J_k$ to obtain a probability law. A possible zero-transfer component has zero weight at these positive times. In infinite volume one can equivalently use the positive transfer on the Hilbert space of the reflection-positive state, or take the moment measures of finite-box transfers on $[0,1]$ to the thermodynamic limit. Compactness and their moments determine the limiting measure.

Set $Z_b=b E_\ell/L_b=b^2 E_{\rm phys}/L_b$ and $v_b=L_b/b^2$. Under the joint limit above, this time-weighted law concentrates exponentially fast at $P_*$ for $0<T<2A_*/P_*$, and at zero for $T>2A_*/P_*$. At the crossover the estimates exclude values greater than $P_*+\epsilon$ at exponential speed for every $\epsilon>0$; they do not give the weights within $[0,P_*]$.

To see the concentration, choose $h>0$ so $T-h,T,T+h$ lie on the same linear branch of $g(T)=\min(2A_*,P_*T)$. If $d$ is its slope there, the forward-time moment ratio $J_{k+\lfloor h/b\rfloor}/J_k$ has scaled log limit $-hd$. Markov’s inequality on $Z_b\le d-\epsilon$ gives a limsup scaled log probability at most $-h\epsilon$. The backward-time ratio gives the same inequality on $Z_b\ge d+\epsilon$. Integer rounding is harmless since $b\lfloor h/b\rfloor\to h$. At the kink use just the backward ratio for the upper bound. The zero in the later regime is in these scaled energy units; it does not determine the vacuum fraction or a physical mass gap.

The classical strong-coupling area law and the positive transfer are established results. This calculation uses them as context and gives explicit bounds uniform in simultaneous loop size, separation, and coupling, together with a comparison to a strictly positive probe. The constructed regime has no finite interacting continuum mass scale in the stated clock. [Osterwalder and Seiler](https://doi.org/10.1016/0003-4916(78)90039-8) · [Clay problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
