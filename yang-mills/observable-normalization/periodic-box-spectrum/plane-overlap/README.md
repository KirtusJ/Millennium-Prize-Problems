# Effect of the gauge-plane identification on the flat SU(2) Gaussian overlap

**A4, submitted for disproof.** G4 compared frozen and moving hard vacua by isometrically identifying the transverse planes at each momentum. For an axial commuting background one can instead keep the additive link coordinates fixed and explicitly project their variations onto the new gauge-orthogonal planes. In this comparison the same leading extensive loss of overlap survives. The difference of the two negative log overlaps is uniformly O(θ⁴) and has a nonzero continuum limit with small-angle coefficient **0.0006140022862 θ⁴**. Here θ is the adjoint angle around the whole spatial cycle. [G4's width comparison and conventions](../../../g4/full-attempt/two-site-gap/fast-vacuum.md)

This calculation concerns the exact *quadratic* nonzero-momentum factors at flat backgrounds on a periodic cubic lattice. All overlaps below are unsquared, between normalized real Gaussian ground-state wave functions. The derivation specifies one identification of their Hilbert spaces. The physical Wilson kernel connecting two different background slices also integrates temporal gauge transport and nonlinear fluctuations.

## Plane metric in fixed coordinates

Write δ=θ/N, take the constant fundamental link in direction one to be exp(iδσ₃/2), and set the other two to the identity. Omit the p=0 block. Use charge + to represent the two real charged colors as one complex field. Its Fourier coefficients at all N³ momenta are independent complex coordinates. In right-trivialized coordinates an infinitesimal gauge transformation at momentum p spans the line with components 1−exp(i(pⱼ+δ δⱼ₁)). This follows by differentiating the gauge transformations at the two ends of a link. The derivative of the exponential map from additive logarithms is the time average of the adjoint action along the link. On direction one its charged multiplier is exp(iδ/2)f with f=sinc(δ/2); the other multipliers are one.

Remove the componentwise midpoint phases exp(ipⱼ/2) in the reference space and exp(i(pⱼ+δ δⱼ₁)/2) in the target. The two orbit lines now have real direction vectors s=(x,s₂,s₃) and s′=(y,s₂,s₃), where sⱼ=2sin(pⱼ/2), x=s₁ and y=2sin((p₁+δ)/2). Set t²=s₂²+s₃². The map from the reference plane to the new one is the orthogonal projection onto s′⊥ after applying diag(f,1,1) to s⊥. On the common polarization perpendicular to both axis one and (0,s₂,s₃), the singular value is one. Taking the dot product of the two normalized complementary polarizations gives the second squared singular value
$$\lambda=\frac{(ft^2+xy)^2}{(x^2+t^2)(y^2+t^2)}.$$
For t=0 both singular values are one. All denominators are nonzero for nonzero grid labels and |θ|≤1/2. The projectors are unchanged by the choice of representative at the edge of the momentum cell.

## Finite-lattice answer

On the moving transverse plane the curl square is m′I, m′=|s′|². On the reference plane it is mI with m=|s|². The normalized scalar Gaussian transfer ground state has precision a(m)=√(m(1+m/4)), obtained by substitution in the unit-variance Gaussian convolution with magnetic half-weights. Put b=a(m′). Pullback of the moving vacuum to fixed coordinates gives precisions b and bλ. Its constant measure Jacobian is accounted for by normalizing the state. Each complex polarization contributes two identical real Gaussian integrals. Hence the exact correction to G4's negative log overlap is
$$D_N(\theta)=\sum_{p\ne0}\left[\log\cosh\!\left(\tfrac12\log(b\lambda/a)\right)-\log\cosh\!\left(\tfrac12\log(b/a)\right)\right].$$
The neutral color does not contribute. The terms can have either sign at individual momenta.

## Refinement and the surviving finite term

Use signed grid labels k with p=2πk/N. At each fixed k≠0 put u=k₁/|k| and z=θ/(2π|k|). In the continuum limit the width ratio b/a tends to l=√(1+2uz+z²), and λ tends to (1+uz)²/l². Thus the limiting summand is
$$d(u,z)=\log\cosh\left(\log(1+uz)-\tfrac12\log l\right)-\log\cosh\left(\tfrac12\log l\right).$$
Use the half sum of the contributions of opposite momenta before summing the limiting series. The unpaired term can be of cubic order in z.

Here is a domination argument that includes lattice modes far from zero. In the exact formula scale the local shift by writing δ=v|s|. Then x/|s| and t/|s| have magnitude at most one, and y/|s|=(x/|s|)cos(δ/2)+2cos(p₁/2)sin(δ/2)/|s|. For |θ|≤1/2, |v|≤1/(8|k|) since N|s|≥4|k|. The normalized shifted vector differs from the initial unit vector by at most |v|. Also |s|≤√12. In these compact ranges the shifted norm and the projected complementary polarization factor are bounded away from zero: the normalized numerator (ft²+xy)/|s|² is at least 1−|v|−|1−f|. The two logarithms and their first four derivatives in v are therefore uniformly bounded, with removable sinc limits at |s|=0. At v=0 the change in the plane metric starts at second order, as follows by subtracting the numerator of λ from its denominator. Since the derivative of log cosh vanishes at zero, the correction starts at third order. Momentum reversal sends δ to −δ in the norm and metric; thus the symmetrized summand has absolute value at most Cθ⁴/|k|⁴. This bound is summable in three dimensions, including the finite-lattice faces paired modulo N. It gives uniform O(θ⁴), justifies the continuum series, and preserves G4's leading order Nθ² overlap cost.

Expanding the symmetrized continuum summand gives 5u²(1−u²)z⁴/8+O(z⁶), uniformly for |u|≤1. Consequently
$$\lim_{N\to\infty}D_N(\theta)=K\theta^4+O(\theta^6),\qquad
K=\frac{5}{8(2\pi)^4}\sum_{k\ne0}\frac{k_1^2(k_2^2+k_3^2)}{|k|^8}>0.$$
Positivity already follows from k=(1,1,0). To evaluate K efficiently use Θ(t)=Σₙexp(−tn²) and A(t)=Σₙn²exp(−tn²). The constant equals 5/[24(2π)⁴] times the integral of t³A(t)²Θ(t) over positive t, by the gamma integral and exchange of the positive sums. The code uses the Gaussian Poisson identity below t=1. It gives K≈0.0006140022861899. At θ=1/4 the exact Dₙ/θ⁴ at N=16,32,64,128 is respectively 0.0007347753, 0.0006797166, 0.0006482123 and 0.0006315019. A separate complex projection and singular-value calculation for 200 mode/shift pairs agreed with the plane formula to within 7×10⁻¹⁶. These are numerical checks, without certified floating-point error bounds. [Reproducible calculation](check.py)

Four PCP OS guest-generated Lean identities cover the projection loss, the continuum angle, and the quartic algebra. The horizontal-plane construction and limiting argument above remain available for independent review. This removes one plane-identification ambiguity in a flat axial quadratic comparison; it supplies no volume-uniform lower bound for the interacting transfer spectrum.
