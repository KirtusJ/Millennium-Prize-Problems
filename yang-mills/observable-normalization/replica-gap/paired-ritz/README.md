# Relative errors on the leading transfer ratios from paired spatial slices

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

A histogram of two complete spatial slices half a period apart can bound a finite-volume excitation ratio even when the thermal probability of the vacuum tends to zero. For a resolved mode the systematic error from binning is quadratic in the within-cell kernel oscillation. The bound uses the operator norm of the observed square-root table to set the scale. It requires control of the oscillation inside each cell. The stored averages of flowed plaquettes do not provide that control.

## Quantities obtained from the histogram

Use G4's finite Wilson setup with $2n$ time steps. The normalized half-period kernel $U=T^n/\sqrt{Z_{2n}}$ is positive as an operator, has a positive integral kernel, and has Hilbert–Schmidt norm one. Its eigenvalues are ordered $s_1\ge s_2\ge\cdots$, and $s_1^2$ is the vacuum probability. Let $B_{ij}=\sqrt{p_{ij}}$ for the joint law of opposite cell labels, and $b=\|B\|_{\rm op}$. The entries are square-rooted separately. For orbit diameters $\delta_i$, use $h_{ij}=\operatorname{sech}(\beta_t(\delta_i+\delta_j)/2)$, or any valid sharp mean-to-root-mean-square lower bounds by cell pair. All matrix products marked $\circ$ below are entrywise. In the following three norms the matrices are symmetric and entrywise nonnegative:
$$
 v=\|h\circ B\|_{\rm op}/b,\quad
 d=\|(1-h)\circ B\|_{\rm op}/b,\quad
 w=\|\sqrt{1-h^2}\circ B\|_{\rm op}/b .
$$
Write $\xi_i=\sigma_i(B)/b$ for the ordered singular values, and $c=\xi_i+d$. For every index up to the number of non-null cells define
$$
 L_i=(\xi_i-d)_+,\qquad
 H_i=\min\left\{1,c+w,\frac{c+w+\sqrt{(c-w)^2+4w^2}}{2}\right\}.
$$
Then $L_i\le s_i/b\le H_i$, and $v\le s_1/b\le1$. In particular the **vacuum-normalized half-period ratio** obeys
$$
 L_2\le (\lambda_2/\lambda_1)^n\le \min(1,H_2/v).
$$
At uniform half-oscillation $y=\beta_t\delta$, $w\le\tanh y$, $d\le1-\operatorname{sech}y$, $v\ge\operatorname{sech}y$. At any $\xi_i\ge\epsilon>0$, for small $y$ the third upper bound is at most $c+w^2/(c-w)$. Thus both ends for $s_i/s_1$ approach $\xi_i$ with absolute error $O_\epsilon(y^2)$, uniformly in the vacuum probability. The exponent $1/n$ must still be applied for a one-step ratio. [G4's kernel and orbit oscillation proof](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/2ff7170981b40856891c0c620449608a2a4e7e99/yang-mills/g4/paired-slice-spectrum/spectrum.md)

## Why the error is quadratic

Use G4's orthonormal basis $\phi_i$ given by the magnetic half-weight on each cell, normalized in spatial Haar measure. Let $P$ project onto these functions, $Q=I-P$, and $C$ be the matrix of $PUP$. The positive cell means satisfy $h_{ij}B_{ij}\le C_{ij}\le B_{ij}$. On a single cell pair the kernel of $PUP$ is precisely the orthogonal projection of the restricted kernel of $U$ onto $\phi_i\otimes\phi_j$. Consequently the Hilbert–Schmidt norm of the residual on that pair is $\sqrt{B_{ij}^2-C_{ij}^2}\le B_{ij}\sqrt{1-h_{ij}^2}$. For any test vector split into its cell restrictions, apply Cauchy–Schwarz on each pair and sum against the vector of restriction norms. This proves
$$
 \|U-PUP\|_{\rm op}\le bw,\qquad \|C-B\|_{\rm op}\le bd.
$$
The same comparison applied to $U$ gives $s_1\le b$. Testing the positive compression against a nonnegative norm-maximizing vector of $h\circ B$ gives $s_1\ge bv$. Singular-value perturbation bounds the $i$th eigenvalue of the positive matrix $C$ between $bL_i$ and $bc$, even when $B$ has a negative eigenvalue. Compression and the min–max principle give the lower bound for $U$ and the residual norm gives $s_i/b\le c+w$.

For the remaining upper estimate restrict trial vectors to the orthogonal complement of the first $i-1$ compression eigenvectors in the full Hilbert space. Their $P$ part then has Rayleigh numerator at most $bc\|Pf\|^2$. Both $QUP$ and $QUQ$ have norm at most $bw$, by the residual estimate. The resulting numerator divided by $b$ is bounded by the quadratic form of the two-by-two matrix with rows $(c,w)$ and $(w,w)$ on $(\|Pf\|,\|Qf\|)$. Its largest eigenvalue is the third expression above. Equivalently any $u>w$ with $(u-c)(u-w)\ge w^2$ is a valid upper bound. Only the unresolved complement pays the linear diagonal error. A resolved trial direction couples to that complement twice in this estimate; no separation from adjacent resolved levels is required.

For uncertain inputs, if simultaneous nonnegative entrywise bounds $B^-\le B\le B^+$ are known, use $\|B^+-B^-\|_{\rm op}$ for the singular-value error of $B^-$ and the norms of the upper tables for the two residual budgets in **unnormalized** units. Divide a lower estimate of $s_2$ by $\|B^+\|$ and an upper estimate by $\|h\circ B^-\|$ when positive. The result concerns systematic resolution and propagated input uncertainty. It gives no bound on the number of histories needed to determine a large table to this accuracy.

## Small-vacuum and sharpness controls

Take four states in two cells of two states. With counting measure use the block $J(a,g)=\tfrac12\left(\begin{smallmatrix}a+g&a-g\\a-g&a+g\end{smallmatrix}\right)$ on each pair. Put $J(2,g)$ on the diagonal blocks and $J(1,0)$ off-diagonal, $0<g<1$. Normalize the entire half-kernel by its Hilbert–Schmidt norm at the end. The constant-on-cell subspace has eigenvalues 3 and 1, and the two orthogonal modes have eigenvalue $g$. Apart from the same normalization, the root table has diagonal $z=\sqrt{4+g^2}$ and off-diagonal one. Its observed second ratio exceeds the exact $1/3$ by
$$
 \frac{z-1}{z+1}-\frac13=\frac{2g^2}{3(z+1)(z+2)}.
$$
Thus the uncorrected root-table ratio can have a genuine quadratic bias.

At $g=1/32$, taking the log range of each diagonal block gives $h=\sqrt{1-(g/2)^2}$ there and $h=1$ elsewhere. Uniformly $w\le1/64$, $d\le1/4096$, $v\ge1-1/4096$ and $1/3\le\xi_2\le1/3+1/16000$. The last upper bound follows from $z\le2+g^2/4$. Using $u=669/2000$ in the two-by-two test gives the rational enclosure $[333/1000,335/1000]$ for the half-period ratio.

Now tensor this system with the positive $M$-state kernel $I/8+7\mathbf1\mathbf1^T/(8M)$ and resolve each extra index as part of the cell label. The physical and measured leading ratios remain those of the first system, since the added nontrivial ratio is $1/8$. The three budget matrices tensor with the same nonnegative factor, up to common normalization, so the certified interval is unchanged for all $M$. The vacuum probability is divided by $1+(M-1)/64$ and tends to zero. This is a finite transfer control; the number of labels grows with $M$. A second extreme is one unresolved cell containing a two-state block $J(1,g)$: it hides a genuine ratio $g$ despite an arbitrarily small oscillation as $g\downarrow0$. Quadratic accuracy for resolved ratios does not extend uniformly to hidden modes at zero.

The [host controls](check.py) checked sixty positive kernels with nonconstant magnetic endpoint factors and the tensor example. The three [PCP OS guests](worker.c) checked the cell residual arithmetic, measured-ratio upper bound and Schur test; a second [three-guest replay](../../transfer-increments/replay-guests.py) reproduced [PairedRitz.lean](PairedRitz.lean) with SHA-256 `9bac99e08514ea39d1aa37f3b6ed374a338a9bb963a4286ec3050b6fa73f4282`. Lean 4.19.0 with pinned Mathlib checked four supporting declarations, including the scalar quadratic-form bound. I also recompiled G4's eight declarations and reproduced the original 32-bin rotor enclosure $[0.403514,0.503054]$ at the cited revision. The general Wilson kernel construction, compression and variational arguments are in the mathematical text. A four-dimensional continuum construction and physical gap remain open.
