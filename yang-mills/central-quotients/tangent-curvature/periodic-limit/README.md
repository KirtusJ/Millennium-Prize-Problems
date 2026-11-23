# The weak-coupling lattice gap in isotropic periodic limit states

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Take the original pure four-dimensional $SU(2)$ Wilson law. At each fixed $\beta$, send all four sides of an even periodic cube to infinity together and choose any subsequential state. The transfer gap above its vacuum, **measured in lattice steps**, tends to zero as $\beta\to\infty$, uniformly over these choices. This is a written proof of condition (B) in Z4's reduction, submitted for independent review. [Spectral proof](spectral.md) · [Z4's reduction](../../../z4/attempt/A1_REDUCTION.md)

The shortest proof uses a bounded observable on one spatial slice. Transport two parallel plaquettes into the same frame, subtract their scaled imaginary parts, and measure a Gaussian function of their squared difference. The local Haar variation identifies a Gaussian curvature plus a constant field. The difference cancels that constant. The limiting centered correlation has positive weight at arbitrarily small lattice energies. This contradicts any fixed positive lower bound on the gap along a weak-coupling subsequence.

| Question in the directors' review | Result in the isotropic order |
| --- | --- |
| Which finite-size pressure bound survives? | The upper error in the per-site pressure difference is $6\log(\beta)/L$ beyond an absolute constant. Jensen then bounds the mean scaled face action in every periodic limit. [Pressure and temporal seam](pressure.md) |
| Does the stronger S3a tail hold? | Reflection of a block of unit cells bounds $\mathbb E\,e^{\beta(1-\operatorname{Re}U_p)/8}$ by an absolute constant in every periodic limit. Shared geometric faces have multiplicity at most four. [Moment bound](pressure.md#consequences-in-every-periodic-limit-state) |
| Does the proposed conditional Gaussian expansion have to be proved? | The original-link variation passes to each periodic state at fixed $\beta$. Its local score and a first moment of the face action suffice for the dipole. The suggested uniform expansion of a gauge-fixed conditional kernel remains a separate question. [Rooted identity](spectral.md#why-the-rooted-variation-applies-in-this-order) |
| What about Z4's original single-face reading? | The exponential moment and odd site-reflection test yield limiting variance $3/8$ and the stated squared Maxwell ratio at every fixed lag. [Single-plaquette proof](spectral.md#the-original-single-plaquette-claim) |

The conclusion permits a zero gap at some or all finite couplings. A fixed three-plaquette reading gives $m=O(\beta^{-1/32}[\log(2+\beta)]^{1/16})$. Enlarging the spatial support with the lag gives $m=O(\beta^{-1/8})$ and arbitrarily many orthogonal positive-energy vectors below $C_M\beta^{-1/8}$ for each fixed multiplicity $M$. Conditions (A) and (C), and the continuum existence and mass-gap problem, remain open. [Fixed-stencil estimate](rate/README.md) · [Growing spatial block](block/README.md) · [Jaffe and Witten](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

The energy and three spatial momenta of a single bounded packet can also be resolved together. Every prescribed open neighborhood with $\varepsilon>|P|$ carries positive joint weight at $R\sim c\beta^{1/8}$ for a sufficiently small window-dependent $c$. Below that scale the full limiting measure has the closed forward cone as support and zero mass on its boundary. [Joint energy and spatial momentum](joint-momentum/README.md)

At growing time separation before one correlation length, the exponentially tilted packet has a joint energy and momentum limit. Its momentum-to-energy ratio is independent of the scaled energy and has an explicit degree-19 distribution function. [Tilted joint law](fourier-decay/README.md) · [Exact ratio law and the gap-scale test](momentum-ratio/README.md)

For large scaled momenta in the untilted packet, the in-plane tail falls with the sixth power and the normal component with the eighth. An exact tail comparison also identifies the joint energy and direction for growing thresholds. [Directional tail theorem](directional-tail/README.md)

A four-dimensional nearest-neighbor Gaussian control separates three requirements for a fixed local reading: a bounded midpoint ratio, control at every fixed dyadic clock, and a uniform polynomial short-distance bound. The latter can fail for a bounded hypercubic site scalar even when all fixed dyadic ratios stay finite. [Light-mode overlap and Theorem S](local-overlap/README.md)

Free-field controls for the interaction hypothesis exhibit a nonzero raw two-particle shift in a cubic symmetry channel and calculate the full Wick-square susceptibility ratio under two length normalizations. [Interaction criteria and matching](interaction-controls/README.md)

A regular tetrahedron distinguishes the Maxwell action from quadratic observables in finitely many scalar generalized free fields. The same calculation gives the perturbative trace coefficient and gapped free controls for lower-order ultraviolet tests. [Four-point shape test and short-distance matching](short-distance-controls/README.md)

Two positive transfer measures can have the same gap and exactly matching early moments while their midpoint ratios have opposite limits. This gives a lower bound on the time extent required by a worst-case moment test. [Exact early moments on a common clock](exact-clock-moments/README.md)

For a variable last time index, a strided moment certificate and two indistinguishable positive transfer measures give matching orders for the required absolute precision. [Time extent and precision](clock-precision/README.md)

Near product Haar measure the raw odd-clover covariance has a negative quadratic contact correction, with a quartic remainder uniform over every finite smearing. [Strong-coupling susceptibility coefficient](haar-clover-curvature/README.md)

## Verification

Two three-generation PCP OS deployments returned identical Lean source. The parent counted live links and temporal faces, the child counted distinct reflected faces and their multiplicities, and the grandchild computed a geometric crossing and emitted the general spectral implication. Hosted Lean 4.19.0 verified ten supporting declarations. In particular, fixed-lag convergence of moment arrays with the stated exponential lower bounds forces the contraction norms to tend to one. Each run rejected an invalid guest request and four changed mathematical statements. The identification of the Wilson field, reflection estimates and application of the transfer construction remain analytic proofs. [Lean source](PeriodicCriticality.lean) · [Guest source](worker.c) · [Receipts](receipts.zip)

The separate numerical checks enumerate 54 reflected blocks, compare five Haar integrals to the exact Bessel normalization, differentiate 64 original quaternion words with both link orientations, and evaluate 36 discrete temporal Fourier coefficients against the positive image sum. These checks exercise specific steps of the proof. [Checks](check.py) · [Native replay](verify.py) · [Toolchain](../../clustering/execution.md)

~~~sh
OPENBLAS_NUM_THREADS=1 python check.py
python verify.py --pcp-os "$PCP_OS" --kernel "$KERNEL" --desk "$DESK" \
  --delegate "$DELEGATE" --qemu "$QEMU" --firmware "$FIRMWARE" \
  --lake "$LAKE" --mathlib "$MATHLIB" --out "$FRESH_OUT"
~~~
