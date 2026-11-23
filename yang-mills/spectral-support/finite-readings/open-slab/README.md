# Tensor-sector energies from open slabs with fixed boundary distances

A nonvacuum boundary can still prepare a state with definite cubic symmetry. This gives G4 an alternative test of **finite-volume energy support** when several temporal slab lengths are available at the same spatial volume, coupling and lattice spacing. Its observable is the energy distribution of a prepared tensor state. The vacuum matrix element of the tensor requires a separate overlap argument.

Use the same reflection-related boundary at both ends. Let K be the positive one-stride transfer divided by its vacuum eigenvalue, so its spectrum lies in [0,1]. Keep the padding from either end to its adjacent insertion fixed at d strides while varying the separation j. Up to a common normalization the prepared state is b=KᵈB. For a bounded self-adjoint slice probe O the two-point expectation on the slab of length 2d+j is

$$C_j=N_j/D_j,\qquad N_j=\langle Ob,K^j Ob\rangle,\qquad D_j=\langle b,K^j b\rangle.$$

Assume b is cubic invariant, the transfer commutes with the cubic group, the vacuum is a unique singlet, and O is a component of a pure nontrivial irreducible tensor. Then Ob lies in its tensor sector and the one-point function vanishes by symmetry. This gives positive moments with no vacuum atom even if b has large excited-state contamination. Mixing different boundaries, changing the padding, or subtracting a separation-dependent disconnected fit requires a new argument. The usual open-time measurement at fixed total slab length varies at least one of the two margins when j changes. The numerator need not then come from one state. [Open-boundary transfer framework](https://arxiv.org/abs/1105.4749)

For Nⱼ>0 take one further stride of physical length h. The propagated probe's mean transfer eigenvalue is

$$m=\frac{C_{j+1}}{C_j}\,\frac{D_{j+1}}{D_j}.$$

At a threshold E*>0 put q=exp(−h E*). If a simultaneous lower bound m₋ exceeds q, at least (m₋−q)/(1−q) of the base numerator comes from tensor energies strictly below E*. Indeed the mean on the complementary part is at most q and the mean on the target part at most one. Positive weight implies finite-volume spectral support in that interval even if the vacuum-to-tensor matrix element vanishes. Three corrected readings also admit the [sharp two-moment bound](../three-readings/README.md). Spectral weight here concerns Ob, with the base-time tilt.

The factor Dⱼ₊₁/Dⱼ requires an independent measurement or bound. For an unnormalized transfer with largest eigenvalue λ₀, it equals the raw boundary partition-function ratio for the two slab lengths divided by λ₀. A lower bound on the raw ratio and an upper bound on λ₀ suffice, in the same action normalization. Correlators alone do not furnish that calibration. This is a potential measurement design; availability of certified ratios for G4's ensembles remains open.

**Exact adverse control.** Use a singlet vacuum, an excited singlet with transfer 1/4, and a tensor multiplet with transfer 1/2. Prepare a singlet boundary so the two singlet contributions to Dⱼ are equal at the chosen base separation. This can be done at any finite j and d by adjusting their initial amplitudes. Couple only the excited singlet to one tensor component and include its adjoint. Then Nⱼ₊₁/Nⱼ=1/2 and Dⱼ₊₁/Dⱼ=5/8. The raw correlator ratio is 4/5 and falsely clears q=3/4. Including the partition ratio recovers exactly 1/2. The sole tensor energy is log(2)/h. The ground-state probe has zero overlap at every separation.

Five guest-generated Lean lemmas check the scalar normalization algebra, the moment inequality, propagation of nonnegative lower bounds, and the numerical control. The transfer representation and symmetry hypotheses are given above. Ground-state isolation, the continuum limit and a volume-uniform lower bound on the full spectrum remain separate obligations.
