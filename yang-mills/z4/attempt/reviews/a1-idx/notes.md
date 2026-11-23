# notes a1-idx
step0: control.txt = 0.272341 (-ln tanh 1)
step1: transfer-operator subfolders by ls = 13 (incl. pcp/). PCP register init. child prompt written; launching child-run1 in background.
step2: read A4 README (observable-normalization): abstract spectral-measure tests; Lean momentLowerBound, separatedTimeWitness (SeparatedTime.lean); explicitly says application to YM trajectory "remains open". NEG examples mu_n=delta_n, n^-1 delta_1.
step3: read C4 README (central-quotients): exact SO(3) pushforward density of SU(2) Wilson weight (cube 8177/2048), flat SO(3) holonomy on T^4 w/o SU(2) lift, E2 one-link quotient gap >4γ/(4+γ); continuum/gap open. Subresults: weak-coupling curvature -> Gaussian/free Maxwell limit (tangent-curvature, magnetic-smearing).
step4: D4 README: Lean SpectralLimit.lean: uniform decay rate on dense family => no spectrum in (r,1) (abstract). NEG: six E1 readings admit gapless measure. Adjoint-band: SU(2) adjoint plaquette positive-energy component at fixed spatial mesh, volume uniform. Ordinary-loop/electric-slab/graph-holonomies: weak-coupling trajectories -> free/Haar limits. "No rate for interacting 4D YM derived".
step5: G4 README: Lean ReflectionPositivity.lean: RP preserved under pointwise kernel limits (abstract). complex/, integral/ (split compact-group holonomy action RP), site/, exterior/, flow-audit (NEG: negative original-plane form for flowed observable at lattice flow time 20). Lists 5 open obligations.
step6: read volume-uniformity (free field control, Lean no_uniform_gap) and z4 README + OVERALL_DISPOSITION.md (Z4's own prior index; used as cross-reference, not as evidence).
step7: skimmed all A4 and C4 sub-READMEs (opening paragraphs). Key: weak-coupling results are Gaussian/free limits (tangent-curvature, magnetic-smearing, lie-curvature, contact-law, star-orders); fixed-mesh Hamiltonian results (hamiltonian-variance, excited-band, momentum, locality, electric-disorder, uniform-band strong coupling). NEG: flow-reflection/flow-momentum/spatial-flow (negative reflected form for 4D-flowed obs), flow-basis, lorentz-test, transfer-clock, transfer-increments counterexample.
step8: skimmed D4 and G4 sub-READMEs. G4 wilson/: openSlab_wilson_reflection_positive (Lean) finite open slab RP of Wilson law. graph-holonomies NEG: b(1+beta)->0 => Haar, OS form rank one.
step9: Lean inventory: outside B4 Lean files check scalar/finite identities; main analytic theorems are text proofs (READMEs say so, e.g. CQ 'does not formalize measure theory').
step10: child control.txt=13, my ls count=13 -> child control PASS (graded before reading other child output).
step11: read B4 top README + spatial-heat-trace, joint-cutoff, strong-coupling, hamiltonian-time openings (for rerun of child's work).
step12: child INDEX_B4.md draft read (16 rows); grandchild control 391=17*23 correct. Now rerunning spot checks.
step13: child returned (K1 exit 0). Rerun: subfolder count 13 OK; WilsonInfluence decl count 20 reproduced (incl noncomputable); child registers re-verified by me.
step14: inventory.py run via check K2 exit 0: P1 13, P2 child=13 met, P3 7/7, P4 no sorry (text grep) met, P5 FAILED: central-quotients/Model.lean (definitions only) and z4/lean/Z4YM.lean (import aggregator) lack #print axioms -> my expectation was wrong, not a target defect. Writing INDEX.md.
step15: INDEX.md written. Running final verifies.
step16: report.md written. Done.
