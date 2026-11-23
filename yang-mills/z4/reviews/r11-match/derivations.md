# Derivations used by ym.py / analyse.py (r11-match)

## Flow normalisation
U = exp(i theta.sigma). For S = sum_{unoriented p} Re tr(1 - U_p) (2x2 trace) the Lie derivative along
T^a = -i sigma_a/2 of the local term -Re tr(U V) (V = sum of staples) is d^a S = -w_a with U V = w0 + i w.sigma;
Luscher's S_w sums over ORIENTED plaquettes (factor 2), so Z = -g0^2 dS_w = -i w.sigma = -P_ta(U V).
ym.flow_force uses exactly this (z = -w). Checked by C6: a factor-2 error would change exp(-2 s k^2) to
exp(-4 s k^2) and miss the free-field value by far more than 20% at s=0.5.

## Free-field magnetic density with spatial flow
Per colour a, S_a = (beta/2) sum_p Phi_a^2, Phi = lattice curl of theta (abelian at leading order).
Feynman gauge: <theta_mu(k) theta_nu(-k)> = delta_mu,nu / (beta khat^2), khat^2 = sum_mu 4 sin^2(k_mu/2).
For spatial i<j: <|Phi_ij(k)|^2> = (khat_i^2 + khat_j^2)/(beta khat^2); sum over i<j in 1..3 gives
2 khat_s^2/(beta khat^2). Spatial flow (linearised) damps the 3D-transverse part as exp(-s khat_s^2), Phi_ij
depends only on that part, so Phi^2 picks up exp(-2 s khat_s^2).
Deficit 1 - 1/2 Tr U_p = 1 - cos|Phi| ~ |Phi|^2/2 summed over 3 colours:
   E_free(s) = sum_{i<j} <1 - 1/2Tr U_ij> = (3/beta) (1/V) sum_{k != 0} khat_s^2 exp(-2 s khat_s^2)/khat^2.
Check: s=0, infinite volume, <khat_s^2/khat^2> = 3/4 -> 9/(4 beta) = 3 plaquettes x 3/(4 beta), the known
weak-coupling SU(2) plaquette 1 - <P> = 3/(4 beta).  (Finite 6^4: 5.6207e-2 vs 5.6250e-2 at beta=40.)

## Physical normalisation of Ebar (Q0)
U_ij = exp(i Phi.sigma), Phi^a = g a^2 F^a_ij / 2 at tree level -> 1 - 1/2Tr U_ij = g^2 a^4 (F^a_ij)^2 / 8.
With G = g F and E_mag = (1/2) sum_{i<j} G^a_ij G^a_ij (the spatial part of (1/4) G G):
   sum_{i<j} (1 - 1/2Tr U_ij) = (a^4/4) E_mag   ->   E_mag a^4 = 4 Ebar,   Q0 = (s/a^2)^2 * 4 Ebar.
The brief's beta-normalised form: magnetic ACTION density (1/g^2) E_mag a^4 = (beta/4) * 4 Ebar = beta*Ebar
(beta = 4/g^2), Q0beta = (s/a^2)^2 beta Ebar. Q0beta carries a factor 1/g^2(a) and is NOT expected to agree
between spacings (ratio ~ beta_f/beta_c = 1.087 times Q0 ratio); Q0 is the RG-sensible one (cf. t^2 E).

## Physical matching
sqrt(8s) = l/3 -> s/a^2 = N^2/72: 0.5 (N=6), 2.0 (N=12). tau = N/6, N/3: 1,2 (N=6); 2,4 (N=12).
l sqrt(sigma) = N a sqrt(sigma) (FHK Table 3): 6 x 0.3690 = 2.214, 12 x 0.1905 = 2.286; mismatch +3.25(94)%.
Since Ebar is a slice average, R ~ 1/(l^3) x f(l) in physical units; a +3.25% size mismatch alone would
give R_f/R_c ~ 1.0325^-3 = 0.91 (rough, ignoring f). This is the stated systematic of the matching.
