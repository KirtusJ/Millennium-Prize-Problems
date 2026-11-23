# Spatial flow as a predictor of magnetic transfer

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00) · Yang–Mills existence and mass gap

Can measurements made entirely on one spatial time slice reproduce a magnetic measurement propagated by Euclidean transfer? In the free Wilson vacuum an explicit positive average of spatially smoothed magnetic **fields**, squared after averaging, reproduces the propagated centered energy exactly. In the compact four-dimensional $SU(2)$ Wilson vacuum every fixed probability distribution of these spatial clocks has a strictly positive squared error for the unflowed plaquette target at every finite coupling. The lower bound holds uniformly in even spatial side $L\ge4$ and can be measured with three connected correlators. [Free reconstruction](free.md) · [Compact obstruction and a weak-limit comparison](wilson.md)

| Question | Result |
| --- | --- |
| How much spatial flow does one free transfer step require? | The first-passage law of a rate-two continuous-time walk represents each one-particle transfer multiplier. For $n$ steps, capping a positive clock at $U$ has optimal uniform error of order $\min(1,n/\sqrt U)$ across the full spatial symbol interval. [Clock law and sharp order](free.md) |
| Can spatial measurements resolve moving two-particle energies? | Two independently variable spatial flow times on the two magnetic fields span the symmetric scalar amplitudes in the free channel. A shared time incurs a strictly positive projection error for a time-translated vector at nonzero external momentum. [Projection calculation](free.md) |
| Which states enter the nonlinear prediction? | In the electric one-square model the raw centered target is pure adjoint. The predictor has strictly positive fundamental spectral weight at each finite clock index. As that index grows, the normalized weight in each fixed bounded energy window decays at an explicit exponential rate with an $n^{3/2}$ prefactor. [Exact coefficients and rate](square.md) |

Two recursive native PCP deployments produced identical Lean source. The kernel checks 18 supporting declarations, including the integrated bounded-clock inequality and the squared-discrepancy bound for two positive-measure cylinders. The field-theory comparisons and the asymptotic rate are written proofs with independent numerical checks. The interacting continuum construction and its physical mass gap remain open. [Verification and reproduction](execution.md) · [Clay formulation](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
