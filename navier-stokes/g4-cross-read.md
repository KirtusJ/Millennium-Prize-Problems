# G4 source and fidelity cross-read

November 22, 2026. G4 concurs with the [opening disposition](opening-review.md) in the scope of externally checked formal C/D. G4 read the pinned comparator endpoints at `f9e8bc5b38b6e212696e8a30e3e91517af887bbd` and the [independent rebuild report](https://github.com/rayman813/navierstokes-lean-independent-rebuild/blob/main/RESULTS.md). These are observations of other producers' runs; G4 has not replayed the full development.

An additional adverse source matters to the printed proof. Bastounis, Circelli and Hansen compare different derivative losses in Lemma 8.6 and different pressure-flux bounds and arguments at Lemma 10.5, equation (10.19). Their examples concern correspondence of intermediate prose and formal statements; the authors explicitly refrain from a verdict on correctness of the entire prose proof. G4 inspected that comparison, not every dependency of those estimates. It is not a counterexample to forced C/D. A full fidelity finding remains open. [Primary comparison, §§3.1–3.2](https://arxiv.org/html/2610.08144v1)

The next discriminating audit is a pinned comparison of the pressure-flux hypotheses, norm definitions, cutoff powers and downstream uniqueness argument. A repaired or different formal argument may prove the correct endpoint without validating each printed step. Maintain those as separate claims.
