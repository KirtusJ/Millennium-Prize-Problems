# Results (transfer-operator, read-only)
Control: 17*23 = 391 (control.txt).

## (a) Declarations (Lean: lines starting theorem/lemma/def/structure, indentation allowed; MD: lines containing word "theorem")
Lean: strong-coupling/WilsonInfluence.lean 20; spatial-heat-trace/HeatTrace.lean 17; wilson-surfaces/WilsonSurfaces.lean 19; blocked-time/BlockedTime.lean 18; girth-shell/GirthShell.lean 20; coarse-holonomies/CoarseHolonomies.lean 17; hamiltonian-time/HamiltonianTime.lean 11; weak-cavity/WeakCavity.lean 25; connected-rectangles/ConnectedRectangles.lean 28; periodic-time/PeriodicTime.lean 10; TwoSector.lean 10; spatial-plaquette/WilsonSlice.lean 4; joint-cutoff/JointCutoff.lean 14.
MD ("theorem"): strong-coupling/README.md 4; wilson-surfaces/positive-probes.md 1; wilson-surfaces/prefactors.md 1; blocked-time/execution.md 2; blocked-time/README.md 1; blocked-time/compact-groups.md 1; blocked-time/local-limit.md 1; girth-shell/execution.md 1; girth-shell/README.md 1; coarse-holonomies/binary-experiment.md 2; coarse-holonomies/execution.md 1; coarse-holonomies/compact-groups.md 2; README.md 1; hamiltonian-time/execution.md 2; hamiltonian-time/README.md 4; hamiltonian-time/plaquette.md 1; hamiltonian-time/plaquette.md 1; weak-cavity/execution.md 1; connected-rectangles/gap.md 1; connected-rectangles/analyticity.md 1; periodic-time/execution.md 2; spatial-plaquette/README.md 2; joint-cutoff/evolution.md 1.
(127 files total; pcp/ has only replay.py and worker.c.)

## (b) Beta regime per folder (heuristic, from grep of beta wording)
- strong-coupling: strong coupling (small beta). strong-coupling/README.md:5 "If both tanh beta_s and tanh beta_t are at most 1/20, ... norm at most 1/3, uniformly in L"
- wilson-surfaces: mixed: fixed beta, plus beta->0 (strong coupling) with joint scaling. wilson-surfaces/README.md:35 "Now let beta=beta(b) down to 0 at any rate"; :24 "Hold any admissible beta>0 fixed."
- connected-rectangles: joint limit (beta vs lattice spacing b). connected-rectangles/README.md:15 "If |log beta| b^2 -> infinity, the first term gives C_k=..."
- blocked-time: joint limit, tree-level beta scaling with mesh. blocked-time/local-limit.md:42 "let a spatial mesh b down to 0 and take kappa=beta b, lambda=beta/b"
- joint-cutoff: joint limit. joint-cutoff/README.md:74 "bare tree-level matching kappa=beta b, lambda=beta/b with L lattice..."
- hamiltonian-time: joint (beta_t=kappa/a, beta_s=a*lambda) at fixed spatial spacing. hamiltonian-time/README.md:5
- girth-shell: fixed beta / small spatial coupling expansion, with joint edge. girth-shell/joint.md:3 "second spatial derivative at fixed positive temporal coupling"
- spatial-heat-trace: joint (B=1+4beta_s+2beta_t = x^{o(1)} as b->0). spatial-heat-trace/rare-cubes.md:3
- weak-cavity: weak coupling (large beta, fixed finite cube) plus fixed anisotropic couplings. weak-cavity/spectrum.md:21 "at the anisotropic finite couplings beta_s=1, beta_t=0.01"
- coarse-holonomies: fixed beta. coarse-holonomies/binary-experiment.md:32 "at isotropic coupling beta=1, J=6 ..."
- periodic-time: beta barely mentioned (only angle variables / renormalization coefficients); no beta-regime treatment.
- spatial-plaquette, pcp: no beta wording.
- None of the folders was found treating beta->infinity at fixed lattice explicitly in a beta wording grep (weak-cavity is the nearest, "weak-coupling").
