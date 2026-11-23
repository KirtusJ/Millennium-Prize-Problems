# Evidence, independent checks and replay

Two complete three-level native PCP hierarchies emitted the same [Lean source](MagneticSmearing.lean). At each step the hosted Rust desk delegated to a fresh measured PCP OS guest and the returning supervisor read and hashed the child's source. The parent enumerated the 16 lazy-step slots. The child independently counted the retained and absorbed endpoints of all 256 two-step paths. The grandchild computed the low-energy powers for the two differentiated profiles. Hosted Lean 4.19.0 with Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b accepted 21 named theorems per run. The axiom reports use only propext, Classical.choice and Quot.sound. The emitted source hashes to 7e201b7275b6bb4dc2ee90c650addda474923ce889cfaeb2d4ad163d4e43c643 and the worker ELF to 2261c963fa734bbfd56057066255e1cecf9bc7a4ac10155f2fb1afde4aa91797. [Native worker](worker.c) · [Execution archive](execution-logs.tar.gz) · [Kernel and Enterprise calibration pins](../clustering/execution.md)

Lean covers the stopped-walk telescoping identity with exit flux, a frame-commutator identity, the Duhamel integral bound, the moment absorption step, signed-block moment identities and scalar spectral constants. Each run rejects one wrong native task and six false Lean conclusions, including a frozen exit distribution and an incorrect reflection base. A draft exceeded default recursion in the finite count and had linter diagnostics. The final accepted source and adverse logs are preserved. The growing-volume Ward argument, full field tightness and continuum spectral identification have written proofs. End-to-end formalization and independent director review remain open.

Direct conditional $SU(2)$ Haar integration on a four-dimensional side-three Wilson torus varied a link used by several rooting paths. The two possible endpoint orientations gave full derivatives of $-0.1960184343$ and $-0.3029215642$, matching the Wilson action scores. Freezing the color frame gave $-0.0705327745$ and $-0.4708161747$. Two quadrature resolutions agreed. The stopped-kernel signed Hodge identity on a separate four-torus had maximum Fourier residual below $2\times10^{-14}$. Dropping the exited mass cost 0.04653 in $\ell^1$. The reflected second-difference test checks the actual one-cell base shift on a line. [Moving-frame Haar quadrature](check_ward.py) · [Kernel, reflection and scaling checks](check_scales.py)

The spectral quadrature uses a compact smooth profile, a tensor product of fourfold convolutions of a normalized one-dimensional bump. For ordinary smearing its continuum $C_0(0),C_0(1),C_0(2)$ were 0.01972957, 0.00455193 and 0.00136940. At $\sigma=1/(2C_0(0))$ the bounded mean-normalized connected reading was 0.02029847 at time one and 0.00180930 at time two. The ratio of the two positive-time connected readings was 0.0891348. Increasing the momentum resolution from 104 to 136 and including an additional spatial alias were checked at the tolerances in the script. These values evaluate the limiting covariance and its lattice Gaussian comparison; the passage from the nonlinear original Wilson measure uses the analytic estimates.

I also recompiled G4's periodic reflection source at commit 30885b4 against the previously replayed Wilson, integral and complex modules. Lean produced 27 axiom reports and five unused-section-variable warnings, with no errors or placeholder axioms. The two-bond-seam result and the site-reflection proof used here have distinct boundary laws. [G4's periodic module](../../g4/periodic/) · [Original site reflection](../tangent-curvature/reflection.md)

With the pinned kernel, tools and Mathlib and a fresh output directory, rerun the following.

~~~sh
python3 verify.py --pcp-os "$pcp_os" --kernel "$kernel" --qemu "$qemu" \
  --firmware "$firmware" --desk "$desk" --delegate "$delegate" \
  --lake "$lake" --mathlib "$mathlib" --out "$out"
OPENBLAS_NUM_THREADS=1 python3 check_ward.py
OPENBLAS_NUM_THREADS=1 python3 check_scales.py
~~~
