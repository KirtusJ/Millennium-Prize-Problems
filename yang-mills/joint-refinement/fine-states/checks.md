# Reproducing the refinement checks

The local Wilson cutoff uses exact rational arithmetic with a factorial upper bound and a geometric bound on the exponential tail. The compact plaquette and transverse alias matrices use floating-point linear algebra. The latter enumerates every coarse momentum including inversion-fixed modes. Its all-chaos extension and the matching lower bounds are mathematical arguments. [Interacting cutoff and compact control](wilson.py) · [Quadratic model](gaussian.py) · [Sharpness from one polarization](sharpness.md)

With Python, NumPy, SciPy and Rust available, run these commands from this folder.

~~~sh
python -B verify.py
python -B wilson.py
python -B gaussian.py
python -B box_operators.py
python -B anchor_readback.py
rustc --edition=2021 -O anchors.rs -o anchors
python -B block_check.py ./anchors
~~~

The signed operator comparison compiles the repository’s Rust measurement with a temporary reader and calls Z4’s Python box operators on the same links. It checks single components, their products and invariance under vertex gauges. The anchor analysis compares the full spatial mean on each recorded slice to the archived, independently generated G4 float32 readings. See the separate readout for the boundary preparation, stream grouping and physical separation. [Normalization](winding.md) · [Matched anchor readings](matched-anchors.md)

To regenerate an anchor trajectory, compile `rustc --edition=2021 -O anchors.rs -o anchors`. The arguments are side, bare coupling, archived seed, hot-start indicator, discarded cycles, retained configurations and a new output filename. For example, `./anchors 6 3.276133577 202833 0 384 320 6_202833.bin`. The open temporal extent is six spatial sides, the stride is three heat-bath/overrelaxation cycles per saved configuration, and the output is little-endian binary64 in configuration, time, parity-origin and cyclic-component order. The original archive names encode the corresponding parameters. [Sampler](anchors.rs) · [Raw paired data](anchors.zip)

### Formal and PCP scope

Enterprise calibration checked the 58-file method at fingerprint `7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707`. Recursive PCP coordinators dispatched builder and challenger workers on spectral projection, Gaussian aliasing and scalar formalization. Further workers checked the exact manuscripts and the link-local comparison. These workers share a provider lineage. The angle and Gaussian builders’ initial suggestions required the whole low band and a uniform all-particle argument; the proof uses fixed physical time to control particle number. The low-spin cutoff grows along the interacting trajectory.

Three measured native PCP guests emitted the three source sections. The hosted PCP compiler supervisor and its checker compiled the reassembled mathematics with Lean 4.19 and mathlib. The first scalar lemma uses the PCP formalizer’s proof. The other two check a quadratic inequality and the affine angle bound. Two deliberately false mutations failed compilation. The preflight first rejected the labels of the negative controls; the rerun used the verifier’s required label format. The operator comparison, the Gaussian model and the spectral interpretation are outside those three Lean statements. [Lean source](FineTail.lean) · [Mutation controls](mutations.json)

The evidence archive holds the worker requests, exact replies, process receipts, method registers, compiler logs, native serial outputs and input digests. Add `--runtime /path/to/PCP_OS_Python --method /path/to/Method` to the verifier to replay registered objects and hash chains. Chain verification checks the archived bytes. It supplies no independent mathematical endorsement. [Archived evidence](evidence.zip) · [Verifier](verify.py)
