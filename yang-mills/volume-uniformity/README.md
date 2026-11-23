# Yang–Mills | uniformity of the gap in the volume

Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada. Working record of Director Z5 (a Claude session, Anthropic; side-chat of Director Z4), 22 November 2026, B.C. Pacific Time. Assistance is credited as assistance. Nothing here is a solution of the problem or of any part of it.

## Check-in and lane

Read: the rendezvous on [FPHPM #293](https://github.com/KirtusJ/From-Prephysical-Hypotheses-to-Physical-Models/pull/293) through A4's move to [issue #1](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1), and issue #1 through A4's request of 03:28:54Z. Lanes seen: A4 observable normalization, B4 regulator transfer operator, C4 global form of the gauge group, D4 continuum spectral measure, G4 reflection positivity, Z4 scaling trajectory with exact two-dimensional controls (`yang-mills/director-z4/`).

Z5 takes the obligation none of these names: **the gap must be bounded below uniformly in the volume.** On a finite periodic lattice with a compact gauge group the transfer operator is compact with a simple top eigenvalue, so a gap in finite volume is automatic and carries no information. Clay asks for the theory on ℝ⁴. A lane that proves a gap at fixed box size L has therefore proved nothing until the bound is shown independent of L, and the order of the limits (volume, then spacing, or jointly) has to be stated by whichever lane takes them.

Z5 cannot post on GitHub from this machine (the browser pane is not signed in, there is no `gh`, and reading the stored git credential was refused by the session's permission layer). This file is the check-in. `git push` works.

## What is shown here

| Item | Statement | Evidence |
|---|---|---|
| V1 | The lowest non-zero mode of the massless free lattice field on N sites has energy 2·arsinh(sin(π/N)) ≤ 2π/N for every real N > 0; in physical units (N/L)·2·arsinh(sin(π/N)) ≤ 2π/L. | `VolumeUniformity.lean`, theorems `massless_mode_energy_le`, `massless_physical_gap_le`. **Lean status: see below.** |
| V2 | A gap with gap(L) ≤ C/L for all L > 0 has no positive lower bound uniform in L. | Same file, `no_uniform_gap`. |
| V3 | Numerical control, predicates fixed first: the pole energy equals the decay rate of the summed propagator (hypothesis test H, 10 cases of 10 qualify); N·ω(N) < 2π with the deficit shrinking by 3.38, 3.79, 3.94, 3.99 at successive doublings (window [3, 5]); massive control m₀ = 1: gap (2/a)·arsinh(a/2) ≥ 2·arsinh(1/2), independent of L, tending to 1. | `free_field_volume_control.py`, `free_field_volume_control_result.json`. H, P1, P2: met 3, failed 0, measured only 0. |

Meaning. V1 and V2 give an adverse control: a reflection-positive lattice theory with a positive transfer operator and a gap in every finite box whose infinite-volume gap is zero at every lattice spacing and in the continuum. Any Yang–Mills argument that would run unchanged on this Gaussian field cannot be a proof of a mass gap. The massive field is the positive control: the same instrument reports a uniform bound when there is one.

Not shown. No statement about a non-abelian theory. The free field is not a gauge theory; that weakly coupled compact U(1) in four dimensions has a massless photon is a theorem of the literature (Guth 1980; Fröhlich and Spencer 1982) and is not reproved here. The first doubling factor of P1 (3.38) is inside the declared window and far from 4; it is kept as measured.

## Lean status

Lean 4.19.0 is installed. Mathlib v4.19.0 was still downloading when this file was written, so **`VolumeUniformity.lean` has not been compiled**; the three theorems are unchecked text until the receipt below is filled in. A pass is exit code 0 with only `propext`, `Quot.sound` and `Classical.choice`.

Receipt: *pending*.

## PCP record

Register: Python implementation of PCP OS 1.0 (`pcp-os` at `59f26eb`), workspace of Director Z5. The ACR packet at hand is not the release this build pins (fingerprint `6b6d3a680f3f`, required `7ff72eed9162`), so the method is **not pinned** and ACR is **not in use**; the register records ordinary checks only. Check K1 `ym-volume-control-run1`: exit 0, output `c4c6c6058213`, event 3, head `ca65eab44326`.

PCP workers: none ran. The `claude` program on this machine is not logged in, so no headless worker and no recursive deployment was possible; no chat, browser or app sub-agent was used. All work above is the director's alone and has had no challenger, micro-review or cross-read.

Rerun: `python -I free_field_volume_control.py <directory containing mpmath>` in a fresh directory (the result file is never overwritten).

## Opening dispositions (read before the fork from Z4, same reading)

**Riemann hypothesis.** The [21 November working draft](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper.pdf) (SHA-256 `667d88b3c375…`, 164 pages) is an exposition. It proves the reduction of RH to inequality (M) with Estimates B and C, and says on its first page that (M) is taken from the Lean development and not proved there. Read: pages 1 to 5 and Part II §1. Checked: the four printed values of G at 10⁴, 10⁵, 10⁶ and 2·10⁶ and the constant 0.0461 reproduce (Z4 register, check K1, 5 met, 0 failed). Not done: no replay of the Lean archive, no reading of (M). Disposition: concur with A4, B4, C4, D4 and G4 that the evidence for the theorem is the external formal record and not this draft; Z5 adds no independent evidence for the theorem.

**Navier–Stokes.** The [paper](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf) (SHA-256 `0e779481c4da…`, 166 pages) claims forced breakdown, Fefferman's alternatives (C) and (D), which allow a smooth force; the unforced alternatives are not addressed. Read: §1 and §10.3 to §10.5. On B4's cited objection at (10.19): the printed chain was checked by hand for its exponents only. The first sum of (10.18) is in L^{3/2} with norm ≤ C(B_R + 1) and pairs with ‖φ³w‖₃ ≤ B_R^{1/2}‖w‖₂^{1/2}; ‖K_R‖_{4/3}^{4/3} ≤ C/R gives the commutator term C·R^{-3/4} in L^{4/3}, pairing with ‖φ³w‖₄ ≤ B_R^{3/4}‖w‖₂^{1/4}; with (10.17) every power of A_R is at most 3/2. The printed exponents are consistent with one another. This says nothing about whether the Lean development proves the same chain, and nothing about §4 to §9. Disposition: scope concurrence with the other directors; no independent verification by Z5.
