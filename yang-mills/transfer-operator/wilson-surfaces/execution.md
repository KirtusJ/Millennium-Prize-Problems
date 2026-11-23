# Proof coverage and independent controls

The four-dimensional conclusions are written proofs for specified Wilson trajectories. The [Lean source](WilsonSurfaces.lean) checks 19 component declarations. They include a measure-theoretic spectral Jensen inequality for every integer lag and the eigenline lower bound for a symmetric positive operator on a real Hilbert space. The complex version in the transfer argument follows by the same orthogonal decomposition. The full cubical chain projection, identification of Wilson transfer insertions, Dobrushin comparison, Schur integration, and uniform thermodynamic Taylor remainder are analytic steps.

| Lean checks | Use in the argument |
|---|---|
| `centerCancellation`, `activeOdds`, `surfaceCount`, `animalRate` | Pairing center signs by a bijection, controlling active-face probability and counting anchored face sets |
| `sliceWalk`, `flatCompetitor`, `rectangleRatio`, `surfaceMinimum`, `fullRectangle`, `threeSquare` | Distance along a slice path, a constant slice competitor, row and column constraints, the area envelope and its equality condition |
| `eigenlineFloor`, `positiveSandwich`, `spectralMoment` | Positive operator comparison, exterior-kernel weighting and propagation from one step to $k$ |
| `normalizedRate`, `relativeRemainder`, `lowBand`, `highBand` | The normalized logarithmic rate, division by an approximate squared mean, and energy tails under a time tilt |
| `densityBias`, `positiveRatio` | Signed integral error using a relative density and normalization for positive insertions |

## Finite checks

- **Original four-dimensional center fibers.** The worker built all 32 links and 24 plaquettes of an open $2^4$ box, with independently sampled SU(2) representatives. Sixteen induced face couplings were negative. It summed 131,072 independent sign assignments after removing tree signs, then used a separate face expansion in the binary boundary algebra. The partition residual was $4.5\times10^{-16}$ or smaller. One-loop and two-loop sign moments agreed to $3\times10^{-17}$. The activation identity was checked for both signs of each face. These are exact finite sums evaluated in floating point, conditional on one set of representatives.
- **Geometry and four-dimensional coefficients.** A dynamic program over all sequences of planar slice masks checked 84 cases against the constant-slice formula. A separate binary integer optimization imposed the edge parity equations on four fully four-dimensional prisms and excluded all the stated minimizers. The solver found costs strictly greater than the predicted minima in all four residual problems. In the $2\times2$ rectangle at separation one the two minima both have eight faces. Explicit index gluing with the SU(2) Haar integral gave respective coefficients four and one in units of $4^{-8}$. After excluding both, the next cost was ten. The optimizer is a finite diagnostic; the general minimum and uniqueness follow from the slicing argument. [Boundary and color controls](bulk_control.py)
- **Positive transfer.** On a spatial graph consisting of one plaquette, temporal coupling 1.7 and spatial coupling 0.38, the character-basis vacuum gave mean trace $0.196891$ and temporal moments at steps 0 through 3 of $1.019434,0.059158,0.039190,0.038775$. Repeating the computation with 15 and 22 characters checked stability. These data test the one-step inequality and Jensen on an interacting compact graph.
- **A solvable shell.** On the two-dimensional boundary of a subdivided box, the two disk amplitudes have coefficients $d_j r_j^A$ and the cylinder has eigenvalues $r_j^{Pk}$. Multiplying a boundary insertion by the fundamental character shifts its label by $\pm1$ with the negative label omitted. Gluing characters yields positive sums for the partition, single mean and two-loop moment. At $\beta=0.04$ the normalized ratio was about $2.501\times10^{11}$ for side three at separation one, $1.25$ for side four at separation two, and $1+2.5\times10^{-13}$ for side three at separation two. The analytical prefactors in the four-dimensional bulk have their own [uniform remainder proof](prefactors.md).

## PCP OS execution

Two fresh deployments used a hosted root, its generation worker, and two grandchildren. One grandchild ran the compact-link and cubical controls and emitted the face-count declaration. The second booted the pinned native PCP kernel, received the incidence counts and square side, enumerated all 512 planar fillings of a $3\times3$ square at two separations, and generated the area and counting declarations. The generation worker then booted the native assembly worker with these regions removed from the Lean basis. The root compared its reassembled output against the tracked source, checked it with host Lean and read the axiom reports. The measured worker and kernel identities and the post-exit desks appear in the [read-back](readback.txt). [Launcher](replay.py) · [Controls](controls.py) · [Native worker](certificate.c)

Each deployment also rejected five modified sources in their respective declarations: doubling the eigenline lower bound, increasing the row/column coefficient from two to three, dropping the allowed active-face ceiling from one half to one third without strengthening its premises, changing the one-slice $3\times3$ cost from twelve to eleven, and tightening the normalized log error from three units to two. The 19 accepted declarations reported standard axioms and no warnings. These controls do not certify the continuum Yang–Mills existence or mass-gap statement.

Use the [pinned transfer toolchain](../execution.md), NumPy and SciPy with its HiGHS mixed-integer solver. A completed baseline run supplies the measured kernel and assembly worker, QEMU, the hosted delegation binaries and the host Lean executable.

```sh
(cd "$MATHLIB" && lake exe cache get Mathlib/Analysis/Convex/Integral.lean Mathlib/Analysis/Convex/Mul.lean Mathlib/Analysis/InnerProductSpace/Basic.lean Mathlib/Tactic/Linarith.lean Mathlib/Tactic/Ring.lean)
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python3 replay.py "$TRANSFER_RUN" "$PCP" ./wilson-surfaces-run
```
