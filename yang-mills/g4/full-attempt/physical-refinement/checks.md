# Reproducing the refinement attempt

The observation archive holds **70 trajectory files**. The independent streams comprise 7,936 open-slab configurations and 12,800 SF configurations. Sixteen additional files replay 192-configuration prefixes with smoothed or momentum insertions. Every archived Fourier or smoothed prefix has a matching unsmeared production stream. The reductions contain 10,198 tensor, scalar, paired and scale readings and 90 momentum rows. Z4’s one-site control streams are in the shared comparison archive. [G4 observations](samples.zip) · [Reductions, source digests and PCP records](evidence.zip) · [Joint control archive](../../../joint-refinement/z4-controls.zip)

### Replay

From this directory, with Python and NumPy installed, run

~~~sh
python -B verify.py
rustc --edition=2021 -O matched.rs -o matched
python -B verify.py --sampler ./matched
~~~

The verifier checks the archive inventories, per-trajectory SHA-256 digests, shape, paired plaquette fingerprints, recomputed reductions, cutoff fits, electric calculations and discrete gauge control. With the sampler it also checks four regenerated fixed-seed prefixes and the common winding tensors in the actual G4 and Z4 implementations. The displayed error estimates require reanalysis of whole streams. To extract the spectral or momentum table directly, run

~~~sh
python -B analysis.py samples.zip --output readings.csv
python -B momenta.py samples.zip > momenta.csv
python -B fits.py readings.csv
~~~

Each filename encodes mode, spatial side, number of temporal intervals, bare coupling, seed, start (0 cold, 1 hot), discarded cycles, number saved and stride. Pass these nine fields in order followed by a new output filename to the sampler to repeat that trajectory. Arrays are little-endian. SF files hold one float64 derivative per configuration. Open and smoothed files hold 14 float32 values per time slice, ordered as plaquette, scalar adjoint, three cyclic $E$ winding, three $E$ clover, three $T_2$ winding and three $T_2$ clover readings. Momentum files store two 13-component scalar readings per slice: the zero mode followed by axial cosine/sine pairs in $x,y,z$ for each of the two momentum shells. [Rust instrument](matched.rs) · [Shared one-link update](../two-site-gap/wilson_mc.rs)

### PCP and Lean

The Enterprise method read-back verified all 58 files at release fingerprint 7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707. Recursive hosted PCP supervisors commissioned six builder/challenger pairs and scoped manuscript reviews. The models share a provider. Their exact delivered prompts, replies, process receipts and registers are in the evidence archive. The packet retains the review that required explicitly removing the entire ground space in the collective trial. Add `--runtime PATH --method PATH` to `verify.py` to replay the archived PCP registers against the local host and canonical method.

The native kernel booted three source-emitting workers in sequence. Their read-back reassembled the exact Lean file; separate controls tested changed, missing, appended, truncated and denied method inputs. The hosted recursive checker compiled eight declarations with Lean 4.19 and mathlib, checked the axiom inventory, and rejected five deliberate mutations. The declarations establish the scalar scaling identities and the quadratic-form comparisons. The gauge integrals, spin-network spectra, variational compactness arguments, and experimental interpretation are mathematical or numerical work outside those Lean declarations. A development run first tried an unavailable aggregate mathlib import; the final source uses the individual modules present in the pinned toolchain. [Lean source](Refinement.lean) · [Mutation controls](mutations.json) · [Evidence archive](evidence.zip)
