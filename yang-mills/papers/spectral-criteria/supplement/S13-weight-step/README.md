# S13: random test of the refinement step under a linear weight bound (Proposition 5.7)

`weightstep.py`, `weightstep_result.txt`. 20,000 random finite-dimensional instances (seed 11), half of them with the coarse space close to the low-energy space. For each instance the constant of the weight bound is the smallest admissible one, so the hypothesis holds by construction; the four inequalities of the proof (inverse-Hamiltonian bound, bound on the mixing rate, the implicit and the explicit bound on the deficit) hold in every instance. The right side of the explicit bound is positive in 11,190 instances; in the others that inequality tests nothing. The smallest slack is 3.2e-4.

The test is of the algebra of the proposition on finite matrices. It says nothing about whether the weight bound holds for the Wilson measure.
