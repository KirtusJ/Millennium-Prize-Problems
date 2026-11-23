# What the same retraction proves at the matched SU(2) coupling

Let a closed fine path traverse $m$ nonskeleton edges, counting repetitions, with any number of additional skeleton edges. Let $W$ be its fundamental half-trace and $W_c$ that of the closed retracted coarse path. Both are measured on the same configuration, with straight two-link coarse holonomies. In the fixed-regulator isotropic Wilson vacuum at $\beta\ge1$,
$$
 \|W-\mathbb E[W\mid\mathcal C]\|_2^2
 \le\|W-W_c\|_2^2
 \le {32m^2\sqrt K\over\beta},
 \qquad K=14\,905\,840.64 .
$$
This applies to winding paths with a bounded number of departures from the skeleton, including when their skeleton portions grow. For a fixed finite product of such half-traces the same bound uses the total number of nonskeleton traversals. It is an absolute error before normalizing an observable by its variance.

Equip unit quaternions with the Euclidean chord distance, invariant under left and right multiplication. Interchanging two adjacent distinct positive steps changes the path holonomy by distance $\sqrt{2X_p/\beta}$, since after stripping common factors their relative product is a conjugated plaquette or its inverse. For each fine edge compare $U(a(x))U_eU(a(y))^{-1}$ to the associated coarse transport. The finite word sorting in the [retraction](gaussian.md) uses at most four swaps per nonskeleton edge and zero on skeleton edges. Reverse traversals use inverse products, which preserve distance. Concatenate the adjusted transports around the closed path. Interior vertex factors telescope, and the base conjugation drops out of the trace. The trace difference is bounded in absolute value by the sum of at most $4m$ chord distances. Each has $L^2$ norm at most $\sqrt{2\sqrt K/\beta}$ by the [uniform single-plaquette bound](../low-spin/plaquette.md). The triangle inequality gives the displayed estimate, without independence, gauge fixing or a change of ensemble. Products of half-traces obey the same telescoping bound since their moduli are at most one.

For $m=o(\sqrt\beta)$ the approximation error vanishes along refinement. A generic macroscopic path can have order $N$ such edges. The estimate then supplies no small error on the prescribed trajectory. It also supplies no comparison for unit-variance rescalings of small differences, arbitrary representation labels, or arbitrary nonlinear functions of many loops. The conditional predictor that matters for the full-complement inequality must retain those cases.
