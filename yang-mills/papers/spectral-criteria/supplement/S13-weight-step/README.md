# S13: random test of the refinement step under a linear weight bound (Proposition 5.7)

`weightstep.py`, `weightstep_result.txt`. 20,000 random finite-dimensional instances (seed 11), half of them with the coarse space close to the low-energy space. For each instance the constant of the weight bound is the smallest admissible one, so the hypothesis holds by construction; the four inequalities of the proof (inverse-Hamiltonian bound, bound on the mixing rate, the implicit and the explicit bound on the deficit) hold in every instance. The right side of the explicit bound is positive in 11,190 instances; in the others that inequality tests nothing. The smallest slack is 3.2e-4.

The test is of the algebra of the proposition on finite matrices. It says nothing about whether the weight bound holds for the Wilson measure.

## One-step criterion (Proposition 5.9), added later the same day

`onestepcrit.py`, `onestepcrit_result.txt`: 20,000 random instances for `d ≥ b/(1 + κ/t)` and its converse, and 2,000 random reversible chains for the minorisation bound; three predicates met. The bound is attained to four figures in some instances (largest ratio of bound to deficit 1.0000), so it cannot be improved in general.

## Direct forms proposed by a reviewer (added later the same day)

`directstep.py`, `directstep_result.txt`: the sharper refinement step `d ≥ (b − κ)_+/(1 + C/m)` and the one-step criterion with an exceptional projection, an arbitrary ratio `s/t` and, in 2,000 further instances, a kernel. D2 to D5 met; the new bound was never below that of the earlier Proposition 5.7 and was strictly larger in 14,737 of 20,000 instances. **D1 FAILED** and is kept: the three vector inequalities of the proof were compared after forming `1 − b` in floating point, which is exactly zero when the norm is below rounding. `directstep2.py`, `directstep2_result.txt`: the same three inequalities compared in logarithms with the norms themselves; met in all instances (48 skipped for norms below 1e-250).
