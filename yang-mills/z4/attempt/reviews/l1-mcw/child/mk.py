"""Write results.md from data_v1.json (mode x). No new physics."""
import json,numpy as np
d=json.load(open('data_v1.json')); o=d['out']
L=[]
L.append("# T124 results (exact Gaussian, 2x2x2xT; no Monte Carlo)\n")
L.append("Method: per colour phi=sqrt(beta)*theta ~ N(0,P), P projector on range(B); X=(1/2)sum_a phi^T M phi => <X>=1.5 tr(MP), Cov=1.5 sum P_pq^2. P from exact time-Fourier blocks (48x32). T->infinity = T=512 (time-direction transfer-matrix gap makes finite-T error ~e^{-3.5T}; T=32..512 agree to 1e-17 for ratios, so extrapolation is trivial). Colour sum included (3 colours).\n")
L.append("## Q1  C_X(0) and C_X(t)/C_X(0)\n")
L.append("C_X(0) (T=32,48,64,512): "+"; ".join(f"{x}: {o['32'][x][0]:.10g}/{o['48'][x][0]:.10g}/{o['64'][x][0]:.10g}/{o['512'][x][0]:.10g}" for x in ('S','A1','E'))+"  (exact rationals 7/2, 51/4, 25/8; differences <=1e-14, roundoff)\n")
for T in ('32','48','64','512'):
    L.append(f"### T={T}"+(" (= T->inf)" if T=='512' else "")+"\n\n| t | S | A1 | E |\n|---|---|---|---|")
    for t in range(7):
        L.append(f"| {t} | "+" | ".join(f"{o[T][x][t]/o[T][x][0]:.12e}" for x in ('S','A1','E'))+" |")
    L.append("")
L.append("Note: at T=32/48/64 the three tables are identical to ~1e-17 relative; difference from T->inf is not resolvable in double precision for t<=6.\n")
P=np.array(o['512']['Ppp_by_orientation'])
L.append("## Q2  single plaquette (T->inf)\n")
sp=P[3]; L.append(f"Spatial plaquette (any of 12,13,23; spread over sites/orientations {o['512']['Ppp_spread']:.1e}): P_pp = {sp:.13f}; mean = 1.5 P_pp = {1.5*sp:.12f}; variance = 1.5 P_pp^2 = {1.5*sp**2:.12f}. These are T-independent (T=16..512 identical to 1e-12).")
tp=0.5469303758
L.append(f"Temporal-type plaquette (for reference): P_pp(T) = {1-sp:.13f} - 1/(8T) (checked T=16..256), limit mean {1.5*(1-sp):.10f}, variance {1.5*(1-sp)**2:.10f}. Sanity: spatial+temporal P_pp average = 1 (tr P/(plaquettes) = 1/2 asymptotically).")
L.append(f"Mean of O_12 = 8*mean = {8*1.5*sp:.10f}.\n")
L.append("## Q3  spectrum, T->inf\n")
E1=4*np.arcsinh(1.0)
L.append(f"Spectrum (checked by exact-fit, residual 6e-16): E_m = 4 asinh(sqrt m) (two photons of equal spatial momentum, phat^2=4m), E_1={E1:.10f}, E_2={4*np.arcsinh(2**.5):.10f}, E_3={4*np.arcsinh(3**.5):.10f}. Three terms reproduce C(t) t=0..8 to 6e-16 relative.\n")
L.append("| X | w_1 (abs) | w_1/C(0) | w_2 | w_2/C(0) | w_3 | w_3/C(0) |\n|---|---|---|---|---|---|---|")
for x,(w,C0) in {'S':((1.5,1.5,.5),3.5),'A1':((4.5,6,2.25),12.75),'E':((1.5,1.25,.375),3.125)}.items():
    L.append(f"| {x} | {w[0]} | {w[0]/C0:.10f} ({w[0]}/{C0}) | {w[1]} | {w[1]/C0:.10f} | {w[2]} | {w[2]/C0:.10f} |")
L.append("\nE1 is the same for S, A1, E: 3.5254943 (auditor's 3.52549435 agrees to 2e-9, rounding). Weights: w1/C(0) = 3/7=0.428571 (S), 6/17=0.352941 (A1), 12/25=0.48 (E). Auditor's 0.046875 = 3/64 matches NONE of these normalised weights. It equals w_1(S)/32 = 1.5/32, i.e. the single-orientation absolute weight 1.5 divided by 32; no definition in the task gives that normalisation (my reading: unverified guess).")
open('results.md','x').write("\n".join(L)+"\n")
