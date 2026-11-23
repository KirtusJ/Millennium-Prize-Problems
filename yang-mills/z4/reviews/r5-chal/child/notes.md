# Notes

## Step 0
control.txt: mpmath quad of x^2 e^-x on [0,inf) = 2.0 (OK).

## Derivation (done by hand before any run)
Coulomb gauge, A(x) = ∫ d^3k/((2π)^3 sqrt(2ω)) Σ_λ [ε_λ(k) a_λ(k) e^{ikx} + h.c.], [a,a†]=(2π)^3 δ^3 δ_λλ', ω=|k|.
This normalization gives H = Σ_λ ∫ d^3k/(2π)^3 ω a†a (+const) for H=(1/2)∫(E^2+B^2), E=-∂_t A.
B = curl A  ->  B_i ∋ i (k×ε)_i a e^{ikx}.  Σ_λ (k×ε_λ)_i (k×ε_λ)_j = k^2 δ_ij - k_i k_j.
(a) G(x,t) := <Ω|B_3(x) e^{-tH} B_3(0)|Ω> = ∫ d^3k/((2π)^3 2k) (k^2 - k_3^2) e^{ik·x - k t}.
Scalar kernel D = ∫ d^3k/((2π)^3 2k) e^{ikx-kt} = 1/(4π^2 (r^2+t^2)).
G = (-∇^2 + ∂_3^2) D  =>  G(x,t) = (t^2 + x_3^2 - x_1^2 - x_2^2) / (π^2 (r^2+t^2)^3).
Check: G(0,t)=1/(π^2 t^4).
(b) Wick (Gaussian, vacuum-subtracted :B^2:): C(t) = 2 ∫∫ f(x) f(y) G(x-y,t)^2
  = 2 ∫ d^3x F(x) G(x,t)^2,  F(x) = (f*f)(x) = π^{3/2} e^{-|x|^2/4}.
Momentum form: C = 1/(2(2π)^3) ∫ d^3k d^3q (P(k)P(q)/(kq)) e^{-|k+q|^2} e^{-(k+q)t}, P(k)=k^2-k_3^2.
Small t: G = t^-4 g(x/t); C ≈ 2F(0) t^-5 ∫ g^2 d^3u; ∫ g^2 = 1/(20π^2) (Beta integrals)
  => p0 = 5, A0 = 2π^{3/2}/(20π^2) = 1/(10√π) ≈ 0.0564190.
Large t: G -> 1/(π^2 t^4); C ≈ 2 (∫f)^2 /(π^4 t^8), (∫f)^2 = 8π^3
  => pinf = 8, Ainf = 16/π ≈ 5.092958.  (Consistent with 2-photon spectral density ρ(E) ~ E^7.)

## Runs
- twopoint (K1): P_2pt PASS, rel errors <= 6e-20 at 6 points (incl. a negative-G point on e1 axis). Took ~8.5 min.
- corr, mc: launched in parallel.
- mc (K2): P_MC PASS. t=1: MC 4.9730e-2 +- 8.8e-5 vs quad 4.96061e-2 (1.41 sigma); t=2: 1.19688e-3 +- 8.5e-7 vs 1.196594e-3 (0.34 sigma).
  => momentum-space normalization (mode norm, pol sum, Wick 2, f~) agrees with position-space G.

## Plan / predicates: see docstrings of twopoint_check.py, corr.py, mc_check.py (fixed before first run).
