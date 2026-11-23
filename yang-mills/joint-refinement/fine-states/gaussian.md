# Adjacent refinement in the transverse Wilson Gaussian

At physical time $\ell$ and fixed spatial period $\ell$, discard the constant Fourier block at each cutoff. In the resulting free transverse theory, straight two-link blocking from even $N$ to $N/2$ satisfies
$$\|QSQ\|=O(N^{-1}),\qquad \|PSQ\|=O(N^{-1/2})$$
on the centered Gaussian space, including arbitrary particle number. These are estimates for the actual coarse and fine subspaces of this quadratic model. Removing the constant modes removes an important part of the interacting Wilson problem.

Use one color first. For dimensionless momentum $p$, write $u_i=e^{ip_i}-1$, $m=|u|^2$, $\omega=2\operatorname{arsinh}(\sqrt m/2)$. The transverse plane is $u^\perp$. The equal-time vacuum covariance is $c(p)I$ there, with $c=1/(2\sinh\omega)$ in the unit-variance electric convention. Substitution of a Gaussian of precision $\sinh\omega$ in the one-step oscillator kernel gives the first excitation multiplier $e^{-\omega}$. Color copies form orthogonal direct sums. The compact nonlinear vacuum and simultaneous large gauge copies are outside this Gaussian construction. [Wilson dispersion and vacuum precision](../../g4/full-attempt/two-site-gap/fast-vacuum.md) · [García Pérez, Snippe and van Baal, §§3–3.1](https://arxiv.org/pdf/hep-lat/9608015)

### The eight momenta in one coarse reading

For a principal momentum $p$ in the half-open cube of side $\pi$ centered at zero, a coarse field contains aliases $q=p+\pi s$ modulo $2\pi$, $s\in\{0,1\}^3$. The straight-link derivative multiplies directions by $W(q)=\operatorname{diag}(1+e^{iq_j})$. It sends $u(q)$ to $u(2p)$. Project onto the coarse transverse plane; on normalized first-chaos coordinates the eight input blocks therefore have observation matrices $\sqrt{c(q)}P_cW(q)|_{u(q)^\perp}$. An overall Fourier normalization cancels from the row-space projection $p_c$. At coarse momentum zero discard the whole coarse constant block. All surviving fine aliases there are high frequency.

For $p\ne0$, all principal diagonal entries of $W$ have modulus at least $\sqrt2$. The induced map between transverse quotient planes has inverse norm at most $1/\sqrt2$: lift a target by $W^{-1}$, then delete the fine gradient, whose image is a coarse gradient. Given a unit principal vector, one can therefore match it exactly in the principal slot of the adjoint observation with a coarse dual vector of norm at most $1/\sqrt{2c(p)}$. Each of the seven high slots has operator norm at most $2\sqrt{c(q)}$, with $m(q)\ge2$. The squared distance of the principal vector from the coarse row space is at most $14\,c(m=2)/c(p)=14\sinh(\omega)/\sqrt3$. This is a regression bound on the fine Hilbert space at each $N$.

At half physical time let $D$ act by $e^{-N\omega/2}$ and put $q_c=I-p_c$. In the principal cube $m\le6$ and $\sinh\omega\le4\omega$, since $\cosh\omega=1+m/2$. Using $\sup_{\omega\ge0}\omega e^{-N\omega}=1/(eN)$ bounds the squared norm on all principal inputs by $56/(\sqrt3 eN)$. On all high inputs use $\|D\|\le e^{-N\operatorname{arsinh}(1/\sqrt2)}$. Different coarse momenta are orthogonal. Adding the two input bounds gives
$$\|q_cD\|\le d_N=\sqrt{56/(\sqrt3 eN)}+e^{-N\operatorname{arsinh}(1/\sqrt2)}.$$

### From linear readings to the entire Gaussian space

On homogeneous chaos of order $j\ge1$, conditional expectation on the observed Gaussian variables acts as $p_c^{\otimes j}$, restricted to symmetric tensors. This follows by conditioning a Wick exponential: its part in the orthogonal coordinates has expectation one, leaving the Wick exponential of the projected argument. Comparing its homogeneous coefficients gives the stated identity. The half-time transfer acts as $D^{\otimes j}$ by the independent oscillator expansion. Since $I-p_c^{\otimes j}\le\sum_{i=1}^j(q_c)_i$, the squared norm of the lost half-time transfer is at most
$$j\,\rho^{2(j-1)}\|q_cD\|^2,\qquad
\rho=\|D\|=e^{-N\operatorname{arsinh}(\sin(\pi/N))}.$$
Here $N\sin(\pi/N)\ge2$ and $\operatorname{arsinh}x\ge x/\sqrt2$ on $[0,1]$. Thus $2\rho^2<1$, and the maximum of the prefactor is one, attained at $j=1$. It follows on the whole centered Gaussian space that $b=\|QSQ\|=\|q_cD\|^2\le d_N^2$ and $\eta=\|PSQ\|\le\rho\sqrt b$. The equality uses the unrestricted first chaos. Restricting to global color singlets preserves the upper bounds by equivariance. No identification of Hilbert spaces at different $N$ or vacuum subtraction from finite slabs enters the proof.

| Fine side | $b$ from Fourier blocks | First-chaos coupling | All-chaos coupling ceiling from $b$ |
|---:|---:|---:|---:|
| 8 | 0.00109388 | 0.00124953 | 0.00166108 |
| 16 | 0.00053922 | 0.00089400 | 0.00104403 |
| 32 | 0.00029018 | 0.00068460 | 0.00074357 |
| 64 | 0.00015426 | 0.00051550 | 0.00053809 |

The table diagonalizes every alias block in complex Fourier coordinates; conjugate blocks describe the corresponding real fields. It checks the all-mode envelope and the coupling bound at each size. The rate proof uses fixed physical time to damp high momenta and high particle number. For the interacting measure, there is no corresponding independent oscillator expansion, and the compact holonomies at zero momentum remain dynamical. [Fourier check](gaussian.py) · [Interacting estimate](README.md)
