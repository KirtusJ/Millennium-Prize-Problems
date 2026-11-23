# A measured quotient plaquette with positive-time weight

Complete-history observability is a density result. A4's radial estimate gives an explicit equal-time **quotient observable** whose positive-time weight stays bounded below uniformly in periodic cubic box size. Work in A4's continuous-time \(SU(2)\) Hamiltonian with generators \(i\sigma_j/2\), electric coefficient \(\kappa>0\), magnetic coefficient \(\lambda\ge0\), side at least three, and \(g=\lambda/\kappa\). Put
\[
 B=\min(g,17\sqrt g/8+3/16),\qquad v_*=[128\pi^4(1+4B)^2]^{-1}.
\]
For the adjoint plaquette trace \(A=4x_p^2-1\), \(x_p=\operatorname{Tr}U_p/2\), one has
\[
 \operatorname{Var}(A)\ge v_*,
 \qquad C_A(t)\ge v_*e^{-tM_A/v_*},\qquad
 M_A=\begin{cases}\kappa\min(16,128B/g),&g>0,\\16\kappa,&g=0.\end{cases}
\]
Here \(C_A(t)\) is the vacuum autocorrelation of the centered observable. The adjoint trace is directly measurable on a single \(SO(3)\) plaquette, so its whole time correlation agrees in the exact pushforward. This comparison requires no reconstruction of an odd fundamental character from long histories. [A4's kinetic and radial estimates](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/a751b0bf6d99fc55067963d52075c91af216571a/yang-mills/observable-normalization/hamiltonian-variance)

To see why the same variance floor applies, write \(x_p=\cos\theta\). For every positive integer \(k\), put \(F_k=2\cos(k\theta)\). The preimage of \(|F_k-m|\le d\) in the angular interval \([0,\pi]\) has exactly the same total length as for \(k=1\). Split the interval into its \(k\) monotonic branches, rescale by \(k\), and reflect the decreasing or increasing branch as necessary. Each branch contributes \(1/k\) times the one-branch length. That length is at most \(\pi\sqrt{d/2}\). In A4's proof each radial fibre has a uniform bound on its angular density, and the integral over exterior and angular-direction fibres of those suprema is at most \(2\sqrt{1+4K_e}\). This bounds the probability of a union of intervals by its total length times the same density bound. Taking \(K_e\le B\) gives
\[
 \Pr(|F_k-m|\le d)\le\sqrt2\,\pi\sqrt{(1+4B)d}.
\]
Choosing \(d=[8\pi^2(1+4B)]^{-1}\) leaves at least half the probability outside. Center at the true mean. Since \(A=1+F_2\), this proves the claimed variance floor. Every even \(k\) defines a quotient observation.

With the same generator normalization and the four distinct plaquette links, the ground-state Dirichlet form for \(F_k\) is \(4\kappa k^2 E[\sin^2(k\theta)]\). For each incident link the radial gradient of \(\theta\) in the three generator directions has squared norm \(1/4\) away from the two poles, a Haar-null set. At \(k=2\) the form is \(16\kappa E[\sin^2(2\theta)]\), bounded above by \(16\kappa\). It is also \(64\kappa E[x_p^2(1-x_p^2)]\le128\kappa E[1-x_p]\le128\kappa B/g\) for \(g>0\). Jensen's inequality for the normalized centered spectral measure now gives the stated autocorrelation. At \(g=0\) the adjoint trace has Haar variance one and is an exact eigenfunction of energy \(8\kappa\), providing a normalization check.

The result concerns a single directly measurable observable at fixed regulator parameters. Along a spatial continuum trajectory the constants can deteriorate, and a lower bound on an autocorrelation gives no lower mass-gap bound. The argument extends A4's published radial proof analytically. The measured Lean certificates in this directory cover the declarations listed in the [execution record](execution.md).

## A bounded positive energy band where the fixed-mesh gap applies

B4 obtains a volume-independent lower gap \(\Delta>0\) for the continuous-time Hamiltonian when \(z=\kappa_B\lambda\) is sufficiently small for the cited perturbation theorem. Here the coefficient of the unit-round Laplacian is \(1/(2\kappa_B)\), so \(\kappa=2/\kappa_B\) in A4's convention and \(g=z/2\). The centered adjoint plaquette lies in the exact winding-neutral sector. Its spectral measure \(\mu_A\) on each finite periodic graph has total mass at least \(v_*\), first moment at most \(M_A\) and support above or at \(\Delta\). Set \(R=2M_A/v_*\). Markov's inequality bounds \(\mu_A((R,\infty))\le v_*/2\), hence
\[
 \mu_A([\Delta,R])\ge v_*/2,\qquad
 C_A(t)-2C_A(t+s)+C_A(t+2s)
 \ge \tfrac12 v_*e^{-tR}(1-e^{-s\Delta})^2
 \quad(t\ge0,\ s>0).
\]
Both endpoints and the positive weight are independent of spatial volume at fixed Hamiltonian coefficients in this perturbative regime. B4's time-limit comparison at fixed spatial mesh and volume applies to these bounded quotient multipliers by pulling them back to the cover. A bulk gap on a spatial refinement trajectory and the same positive band there remain open. [B4's Hamiltonian normalization and local stability argument](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/6c086a6c4dd605a99869ed8c8c2ae3a1eaa6a2aa/yang-mills/transfer-operator/hamiltonian-time) · [D4's positive-time vacuum filter](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/4fdd79bb39e710287e8fd278ce9abfff6177a572/yang-mills/spectral-support/positive-time/vacuum)
