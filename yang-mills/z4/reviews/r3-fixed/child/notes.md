# notes
- Control: (1/2pi) int_0^{2pi} exp(cos t) dt by 64-node periodic trapezoid (mp.dps=30) = 1.26606587775201 -> 1.266066 (matches I0(1), known).
- Plan: periodic trapezoid with M nodes on [0,2pi). For SU(2), (2/pi) sin^2 t dt on [0,pi] equals (1/pi) sin^2 t dt on [0,2pi) by symmetry t->2pi-t, so the same periodic rule applies.
- Trapezoid error ~ Fourier coefficient at order M of exp(beta cos t) relative to c_0 ~ exp(-M^2/(2 beta)). Largest beta = 4*64^2 = 16384; M=4096 gives exp(-512), M=8192 also negligible. Factor exp(-beta) cancels in ratios; use exp(beta(cos t - 1)) for scaling.
- Run 1 (via pcp check K1, exit 0, ~9.6 s): all predicates P1-P3 PASS; node-count diffs <= 6e-47; mpmath.quad cross-check at N=4 agrees to ~1e-48.
- Physics sanity (not a declared predicate): sigma_U1 -> 1/2 (c1/c0 ~ 1 - 1/(2beta)), sigma_SU2 -> 3/8 (c_half/c0 ~ 1 - 3/(2beta)), approached as O(1/N^2). Observed.
- pcp verify: result: PASS.
