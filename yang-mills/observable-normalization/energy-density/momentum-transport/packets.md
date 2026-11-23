# Fixed spatial tests for the three-momentum measurement

The transfer correlators can be measured for fixed Schwartz spatial packets. Choose a real smooth nonzero $\psi$ with support contained in $[l,L]$ with $0<l<L<\infty$, where $v$ is squared spatial momentum. Use $w(v)=|\psi(v)|^2$, translations $a_i=ih$ for $i=0,1,2$ with $h>0$, and three weights $v^m$ for $m=0,1,2$. All choices are independent of the cutoff.

With Fourier measure $d^3p/(2\pi)^3$, take the radial Fourier profile
$$
 \widehat f_{i,m}(p)=2\pi\,|p|^{-1/2}\,v^{m/2}\psi(v),
 \qquad v=|p|^2-a_i
$$
on the translated annulus and zero elsewhere. The squared radial measure of this profile is exactly $v^m w(v)\,dv$, because the radial Jacobian is $\sqrt{|p|^2}\,d(|p|^2)/(4\pi^2)$. The profiles give real Schwartz tests with finite spatial width and rapidly decreasing tails. Exact annular localization requires those spatial tails. Truncating in position space would require a separate correlator error.

Let $C_{i,m}$ denote the ordinary positive-time autocorrelation of the same $O=T^{00}+S$ smeared with $f_{i,m}$. Form $Y_{i,m}=P_{a_i} C_{i,m}(t)$. Since $a_i$ is constant across the band, the transform acts before or after spatial integration. In the finite-reading bounds use $U=l+a_i$ for the common lower bound on squared energy and the series radius. Equivalently absorb $v-l\ge0$ into the invariant mass variable in that bound.

Write $A_m=\iint v^m w(v)f_s(v,t)\,dv\,dA(s)$ and likewise for $X_m,B_m$. Then
$$
 Y_{i,m}=Y_{0,m}+2a_i(A_{m+1}+X_m)+a_i^2 A_m,\qquad
 Y_{0,m}=A_{m+2}+2X_{m+1}+B_m.
$$
The three shifted values for each profile give
$$
 A_m=\frac{Y_{2,m}-2Y_{1,m}+Y_{0,m}}{2h^2},\qquad
 H_m=\frac{Y_{1,m}-Y_{0,m}-h^2 A_m}{2h}=A_{m+1}+X_m .
$$
Consequently the nine positive curves determine the common packet averages
$$
 A_0,\qquad X_0=H_0-A_1,\qquad B_0=Y_{0,0}-2H_1+A_2.
$$
The extra spatial weights remove the variation of $v$ *inside* the annulus. Simply substituting the central momentum in the plane-wave formula would introduce an uncontrolled bias. A nonzero $B_0$ certifies positive scalar spectral weight under the assumed covariant identification. Since $w$ is nonzero and $f_s(v,t)>0$ everywhere on this domain, $B_0=0$ implies absence of scalar excited weight. The same positivity gives $X_0^2\le A_0B_0$.

There is an exact centering simplification on a finite periodic Wilson box. Periodize each spatial packet on the box. Its Fourier series is then finite because the continuum Fourier support is compact. Once its upper momentum is below the mesh Nyquist frequency, every term is a nonzero spatial lattice character. Summing over translated link centers or translated face centers at any fixed orientation gives zero, since the staggered offset multiplies the character by a constant phase. Translation invariance of the periodic Wilson measure therefore makes the one-point expectation of each such energy insertion exactly zero, including at finite time period. This permits directly using its two-point reading on each finite clock grid. The allowed Fourier set must sample the chosen band to obtain a signal. [B4’s Wilson insertion and finite-period comparison](../../../transfer-operator/joint-cutoff/energy-density.md)

To test this on Wilson data, keep the continuum profiles and physical times fixed while controlling the growing-box, clock and cutoff errors. Periodization has its own infinite-volume limit. Exact Lorentz transport of the finite-box correlator is not assumed. The resulting finite intervals can test the proposed mixing law or give a lower bound for one channel if the data warrant it. The identity allows fixed positive frequency-band widths and uses ordinary smeared readings. A single-channel reading does not cover all fields in the vacuum Hilbert space. [Execution and controls](execution.md)
