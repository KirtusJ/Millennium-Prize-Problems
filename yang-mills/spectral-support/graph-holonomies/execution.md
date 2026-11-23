# Execution and independent checks

Director D4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

The first PCP OS guest enumerated the composition table of permutations of three letters by their action on each letter. Its child computed inverses from that table and counted all shared commutator words. The third guest combined the generated entries with D4's analytic Lean text. Each stage booted a fresh measured kernel. The native worker hierarchy reached depths zero, one and two, and the supervisor read back the resulting file and serial receipts after the workers exited. The Linux host ran Lean 4.19.0 with Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b. The complete 9,242-byte module and its guest ELF were independently rebuilt byte for byte. All five earlier generator modes reproduced their published source. [Native guest](guest.h) · [Producer serial receipts](evidence/assemble.serial.txt) · [Checks, hashes and register disposition](evidence/checks.txt) · [Register](evidence/register.jsonl)

Lean checks twenty declarations. They cover the density secant and its integral, finite Cauchy–Schwarz and total-variance accounting, product bounds, a spectral-mass implication, summation of the Casimir loss, the staple clock and its cutoff, iterated reflection powers, the second-order product estimate, the dispersion identities and the limiting bias arithmetic. The two finite-group certificates compute without axioms. Other axiom reports contain only the standard Lean axioms shown in the checks. The Fourier contraction's group inputs, geometry, infinite-dimensional limiting law, conditional Brownian convergence, and the transfer and mean-normalization arguments are proved in the mathematical notes. Five false modifications failed at the intended declarations. [Lean source](GraphHolonomies.lean) · [Mutations](check_mutations.py)

The independent checks enumerated all action-face orientations for winding-line selections, both odd and even periods, and the multiplicities in two full four-dimensional reflection constructions. They tested normalized correlation on finite product channels, including a rare copied bit, and compared noncommuting shared words by direct permutation composition. [Finite checks](check_graph.py)

On a 4⁴ Wilson field the code verified the change in the full action under a single-link replacement, performed conditional Gibbs sweeps, then resampled a whole spatial string 16,000 times at fixed exterior. The fundamental and adjoint conditional readings agreed with their Bessel-product predictions within one empirical standard error each. This test uses the interacting action for the conditional distributions; four sweeps do not establish equilibrium. The code also verified the endpoint orbit for a nonlinear two-detour transporter and the exact affine quaternion dependence of the conditional action. Independent Fourier projections, quaternion pair sums, Bessel ratios and a shared-exterior counterexample tested the subleading mean and its second scale. The prescribed bias-control exteriors are numerical tests of formulas. They are not equilibrium samples. [Wilson checks](check_wilson.py) · [Bias checks](check_bias.py)

D4 separately rebuilt C4's tangent-curvature Lean module at 32e17b1 and ran both of its Python controls. Its 22 declaration reports and the signed Haar, projection and reflection results are in the evidence. The second-scale proof uses C4's written finite-cell Gaussian and moment results, whose full gauge-theory derivation is outside both Lean modules. The independent finite-circle results in this lane do not require those inputs. [C4's proof and scope](../../central-quotients/tangent-curvature/) · [Reproduction output](evidence/checks.txt)

## Reproduction

Set LANE to the absolute spectral-support directory and MATHLIB to the pinned Mathlib checkout. Put the matching Lean toolchain on PATH. KERNEL and PCP_SRC use the pinned PCP OS kernel and source in the original execution record. The numerical checks need NumPy and SciPy. The optional QEMU executable, firmware, register and dispatcher settings are documented by the shared driver. [Kernel and ISO identities](../execution.md) · [Driver](../positive-time/replay.py)

```sh
python -I "$LANE/positive-time/replay.py" --graph-holonomies --kernel "$KERNEL" --pcp-source "$PCP_SRC"
(cd "$MATHLIB" && lake env lean "$LANE/graph-holonomies/GraphHolonomies.lean")
python -I "$LANE/graph-holonomies/check_graph.py"
python -I "$LANE/graph-holonomies/check_wilson.py"
python -I "$LANE/graph-holonomies/check_bias.py"
python -I "$LANE/graph-holonomies/check_mutations.py" --mathlib "$MATHLIB"
```
