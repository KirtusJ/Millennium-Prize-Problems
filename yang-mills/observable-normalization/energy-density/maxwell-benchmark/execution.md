# Maxwell benchmark checks

Three measured PCP OS guests formed a root, child and grandchild hierarchy. The host supervisor dispatched each child after the parent request. Their deterministic payloads emitted the authored Lean source, and a second complete run reproduced it. The pinned host Lean 4.19.0 and Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked ten declarations with only the three standard axioms. [Kernel, QEMU wrapper and admission procedure](../../smeared-plaquettes/action-curvature/execution.md)

From this directory run

```sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof MaxwellEnergy.lean --qemu /path/to/qemu-wrapper
OPENBLAS_NUM_THREADS=1 python check_maxwell.py
```

Run `lake env lean /absolute/path/to/MaxwellEnergy.lean` in the pinned Mathlib checkout. The second guest run returned

```text
w0.elf 746be7b8b33476f8c4977db314fe722e0dee9af464ebb0c40507b7cbcfd523be kernel register: 47 events, head c8b8567926946b95d39c20aabaecf253cd9dfc2aed6a70b0c98efc02a637b6f2
w1.elf 47c2499b10dc3d8cc6a5518cde04672c9a022a12ff62fc73ef1846506128bef0 kernel register: 47 events, head bb2755c1d0008ce67cc9ff747d637666d7abac0681734f8659998ebba53fdff8
w2.elf a8ac39939f5121fb7314400fcb59298508b552b9245cbd2bf6ed219a96baa28f kernel register: 47 events, head 38983a5ffebfac54617a1e919128cba291182f93f15e3062327aba91cccd9425
generated source SHA-256 106ba6e0e14d341b1e3f152cb122b77766f6647c8fcbb4d5cd388315ae72b785
```

Lean verifies the polarization identity and momentum factors, the integral over the photon energy difference and both density constants, the threshold Laplace integral, the scalar expansion, the detector fraction, and the uniqueness and clock ordering of the mixing algebra. The Maxwell vacuum calculation, sampling phases and convergence arguments are analytic. Two mutations failed. Reversing just one polarization’s magnetic sign violates the mixing identity for $a=b=c=1$. Replacing 120 by 60 in the conserved spectral density fails the integrated identity at $q=1$.

## Independent computations

The continuum control works in the original radial and angular photon variables, builds both transverse polarization bases and evaluates all four matrix elements. A separate oscillatory spatial Fourier integral uses the position-space stress correlator. The lattice controls integrate the sine-dispersion formulas on the infinite-volume Brillouin zone. The short-time coefficient check uses the full cube. At positive time the Cartesian quadrature extends to the lesser of the zone edge and $42/t$ per coordinate. These are numerical checks of the formulas; limits follow from the estimates in the notes.

```text
photons 1.0 1.0 0.00031061650412804714 0.03261473286567739 9.390462138986918e-20 position-space 0.00031061650347608726
photons 2.0 0.7 0.004759142146941748 0.17021713112541248 1.0575237524435778e-18 position-space 0.004759142146508722
photons 0.8 1.4 8.060112465231109e-05 0.005850540053966303 1.95997182727217e-20 position-space 8.06011245469912e-05
positive time 0.4 0.0008098028863096371 0.0370380269494249 relative errors 0.012419365534279692 0.29465596526111026
positive time 0.2 0.0008024765860866735 0.030121375762908336 relative errors 0.0032599906433752324 0.05288596680839719
positive time 0.1 0.000801480506263104 0.028962024955492473 relative errors 0.002014686977447999 0.012361118098157098
positive time 0.05 0.0008010944413682122 0.02869749447600993 relative errors 0.0015320268356415756 0.003114514230108112
sharp time 0.2 0.01935719001015991 5.980449536404112 predicted 0.020265756440223465 6.0
sharp time 0.1 0.019812021165377797 5.9951031419036545 predicted 0.020265756440223465 6.0
sharp time 0.05 0.02003922528262549 5.998775197795181 predicted 0.020265756440223465 6.0
sharp time 0.025 0.020152316123204398 5.999693762406472 predicted 0.020265756440223465 6.0
recovered squared amplitudes 2.8899999999999997 0.09
```
