# z1-mix6: side 6, time period 12, beta = 3.276133577 (report assembled by the director)

The worker completed all runs and the reduction; the container was restarted before it wrote its report. This file is assembled by the director from `results/tables.md`, `notes.md` and `REPLAY.md`, which are the worker's own. Nothing here was recomputed after the restart. Same model family as the director; not independent review.

Control: G4's sampler `replicas.rs` built unchanged. G4's side-6 rows: W = −I four-face ratio 0.0464(55), one-face 0.0639(23). Here, 24 streams × 1152: four-face 0.0469(5), one-face 0.0613(4) (z = −1.1 against G4's one-face value). The worker's first 4-stream control failed its own predicate; it attributes this to underestimated 4-stream errors (its expectation), not to a defect of G4. Child: independent code, ratios agree; its mean spread is about 2.6 σ above the worker's, unresolved, not used.

The full table (numerator J, denominator Var, ratios, hot/cold z, stream spread, smallest angle from −I over all coarse spatial plaquettes, per-colour shares) is `results/tables.md`. Summary, large runs (24 × 1152):

| δ | min angle | J4 | Var4 | J4/Var4 | β·J1/Var1 | relative to δ=0 (one face) | disk prediction |
|---|---|---|---|---|---|---|---|
| 0 | 0 | .002875(17) | .06131(88) | .0469(5) | .2008(13) | 1 | 1 |
| 0.5/β | .1526 | .002948(18) | .06313(61) | .0467(5) | .2020(18) | 1.006(11) | 1.010 |
| 1/β | .3052 | .002992(16) | .06617(79) | .0452(6) | .1991(22) | 0.992(13) | 1.039 |
| 2/β | .6105 | .002858(17) | .05963(37) | .0479(4) | .2040(17) | 1.016(11) | 1.152 |
| 4/β (extra) | 1.2210 | .002129(8) | .03687(36) | .0577(7) | .2158(16) | 1.075(11) | 1.531 |

Clear skeletons sampled from the unconditioned measure (8 × 576 each): min angle 1.1427, 0.9586, 1.1820; J4/Var4 = .0920(24), .0860(20), .0928(23); J1/Var1 = .0805(21), .0716(15), .0714(21); Var4 = .00770, .00972, .00773.

Colours: only the four xy colours of the links inside the marked square contribute to J; the other 20 contribute exactly zero (structural: the tests depend only on those links).

All hot/cold checks met (|z| ≤ 1.64).
