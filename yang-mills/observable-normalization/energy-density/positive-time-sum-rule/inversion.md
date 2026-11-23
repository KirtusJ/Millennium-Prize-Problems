# Which spectral law the positive-time diagonal determines

Suppose $M_1<\infty$, and let $\eta=E\nu$ on $E>0$. For real $\xi$, multiplying the time integral by $t^{-i\xi}$ gives
$$
\int_0^\infty D(t)t^{-2-i\xi}\,dt
=K(\xi)\int_{(0,\infty)} E^{i\xi}\,\eta(dE).
$$
The absolute integral is bounded by $cM_1$ and the right-hand factor is the Fourier transform, with positive sign convention, of the finite measure in $\log E$. For $\xi\ne0$, integrate the exponential representation of $F(u)/u^2$ first in $u$, then twice over the unit square:
$$
K(\xi)=\Gamma(1-i\xi)\frac{3^{1+i\xi}-2\,2^{1+i\xi}+1}{(i\xi)(1+i\xi)},\qquad K(0)=c>0 .
$$
The Euler integral is absolutely convergent here. The numerator can vanish only if $1+3e^{i\xi\log3}=4e^{i\xi\log2}$. Equality in the triangle inequality forces both phases to be one. At nonzero frequency this would give $\log2/\log3\in\mathbb Q$, contradicting unique factorization. The gamma factor has no zeros. Dividing by $K(\xi)$ therefore determines the Fourier transform at every frequency and uniquely determines $\eta$. On the open axis $\nu=d\eta/E$ in the sense of measures. [Euler integral and analytic properties](https://dlmf.nist.gov/5.2) · [Fourier uniqueness for finite measures](https://www.statslab.cam.ac.uk/~grg1000/teaching/uniq.pdf)

At fixed positive $t$, the kernel $F(tE)/E$ extends continuously by zero at both ends of compactified energy. The readings of a fixed finite first-moment law are continuous in positive time by dominated convergence. Consequently, if $M_{1,b}$ is uniformly bounded and cutoff readings converge at every time in a fixed countable dense set, every compactified energy subsequential limit has the same interior first-moment law. The entire sequence converges vaguely on the open energy axis to that law. Its raw measure converges there as well, by testing against continuous compactly supported functions divided by energy. This conclusion needs exact limiting data. No uniqueness on an arbitrary finite grid is implied.

## Why a uniform inversion tolerance fails

On log energy $x\in[0,2\pi]$ take the two first-moment probability densities $(1\pm\tfrac12\cos Nx)/(2\pi)$ for any positive integer $N$. Their total variation distance is exactly $1/\pi$. They even share the compact physical band $1\le E\le e^{2\pi}$. Yet the difference of their readings divided by $t$ is uniformly bounded by $c/(\pi e N)$ on all $t>0$. Integrate $g(te^x)\cos Nx/(2\pi)$ by parts. The boundary sine vanishes, and the total variation of $g$ is at most $2c/e$ by the grid argument. This is a quantitative obstruction to recovering a law in total variation from uniformly approximate normalized readings. It coexists with exact uniqueness and vague convergence.

The controls also use a three-atom first-moment distribution and the infrared-divergent raw law $e^{-E}dE/E$. For the latter, pairing exponentials before integration gives $D(t)=\log(1+t^2/[(1+t)(1+3t)])$. The target first-moment law has characteristic function $\Gamma(1+i\xi)$ in log energy. Direct time quadrature reproduces both transforms through frequency six. A family with first-moment weights $0.3,0.5,0.2$ at $1/n,1,n$ respectively sends the last weight to early time and the first weight to late time. [Script](check_readings.py) · [Readings and exact statements](README.md)
