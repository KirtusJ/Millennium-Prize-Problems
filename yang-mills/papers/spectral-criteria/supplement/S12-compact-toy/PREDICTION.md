# Weak-coupling expectation for the compact toy, written before the results of `u1toy.py` were read

Written while the run over β = 0.5 … 8 was in progress and before its result file existed (the file is written at the end of the run). Only a trial at β = 1 on grids 8 and 10 had been seen (γ_opt = 0.96091, lattice gap 1.1622, weight/energy 0.2448 for the first excited level).

Quadratic approximation at large β. Let S be the sum and D the difference of the holonomies of the two parallel lines in one direction. S is a zero mode: each of its four links moves by an independent Gaussian of variance 1/β per step, so the state e^{iS/2} (one unit of electric flux, spread evenly) has energy 1/(2β). D is twice the normalised transverse mode at momentum (0, π), an oscillator with cosh ω = 3, so Var D = 4/(2 sinh ω · β) = 1/(√2 β). The coarse holonomy is Θ = (S + D)/2. Then

1. the first excited level is fourfold (one unit of flux in either direction, either sign) with energy ≈ 1/(2β);
2. its weight in the fine detail is 1 − e^{−Var D/4} ≈ Var D/4 = 0.1768/β, so weight/energy → 0.354;
3. a fine-detail vector near e^{iΘ}·D has resolvent sum ≈ 1/(1 − e^{−2ω}) + (0.1768/β)/(1 − e^{−1/β}) → 1.0303 + 0.1768 = 1.207, which suggests γ_opt → about 0.83 as β → ∞, below the free value 0.9706 (which leaves the winding modes out). This is an estimate from one trial vector, so the limit of γ_opt is at most about 0.83 if the estimate is right, and may be lower.

These are expectations, not predicates; the comparison is reported in the README of this folder.
