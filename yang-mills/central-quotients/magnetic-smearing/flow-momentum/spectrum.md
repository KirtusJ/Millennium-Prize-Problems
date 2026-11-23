# The spatial-flow magnetic spectrum at fixed momentum

Use the same field and Fourier convention as in the [full-flow comparison](reflection.md). With spatial-only flow each propagator retains its positive energy $p$ or $q$. Put $k=|\mathbf k|$. For $k>0$ change variables from $\mathbf p$ to $E=p+q$, $z=p-q$ and its azimuth. Then $E\ge k$, $|z|\le k$, and after integrating the azimuth, $d^3p=\pi p q\,dE\,dz/k$. The physical-energy measure for the point magnetic density, Fourier transformed in its relative spatial displacement, is absolutely continuous. It vanishes for $E<k$ and for $E>k$ has density
$$
 \rho_{s,k}(E)=
 \frac{d\, e^{-sE^2}}{512\pi^2 k}\!
 \int_{-k}^{k}e^{-s z^2}
 \big[(E^2-k^2)^2+(k^2-z^2)^2\big]\,dz .
$$
Indeed the Wick and transverse factor under $d^3p/(2\pi)^3$ is $d\,p q(1+c^2)/8$. One has $2pq\,c=k^2-p^2-q^2$, and $2(p^2+q^2)=E^2+z^2$. Multiplication by the Jacobian gives the stated sum of two squares. Direct integration at $s=0$ yields
$$
 \rho_{0,k}(E)=\frac d{\pi^2}
 \left[\frac{(E^2-k^2)^2}{256}+\frac{k^4}{480}\right]\mathbf 1_{E>k}.
$$
This also follows independently from A4's Maxwell densities: $H=(T-U)/2$, $T=(\mathbf E^2+\mathbf B^2)/2$, $U=(\mathbf E^2-\mathbf B^2)/2$, with zero mixed spectrum. Meyer's leading-order gauge-theory calculation includes energy–momentum spectral functions at finite external spatial momentum. Its stress-tensor channels and thermal terms have different definitions from the flowed magnetic reading here. [A4's two-polarization calculation](../../../observable-normalization/energy-density/maxwell-benchmark/README.md) · [Meyer, *Energy-momentum tensor correlators and spectral functions*](https://arxiv.org/pdf/0806.3914)

Changing $z=ky$ gives a continuous $k\downarrow0$ limit,
$$
 \rho_{s,0}(E)=d E^4 e^{-sE^2}/(256\pi^2).
$$
Thus the zero-momentum correlator has $G_s^{\rm sp}(t,0)\sim3d/(32\pi^2 t^5)$. For every fixed $k>0$ the right endpoint density
$$
 \rho_{s,k}(k+)=\frac{d e^{-sk^2}}{512\pi^2 k}\int_{-k}^k e^{-s z^2}(k^2-z^2)^2\,dz
$$
is strictly positive. There is no atom at $E=k$, since the collinear boundary has zero three-dimensional momentum volume. Substituting $E=k+y/t$ and using dominated convergence gives $G_s^{\rm sp}(t,k)\sim \rho_{s,k}(k+)e^{-kt}/t$. In particular the measured large-time exponential rate is positive for $k>0$ in this *massless* theory. The behavior as $t\to\infty$ is not uniform at $k=0$. For all $E>k$, the positive density lies between $e^{-s(E^2+k^2)}\rho_{0,k}(E)$ and $e^{-sE^2}\rho_{0,k}(E)$, so every positive-width energy window just above $k$ has strictly positive measure.

### Finite wave packets in the original compact vacuum

At fixed physical $s>0$ these momentum laws are also attainable limits of actual spatially flowed, centered $SU(2)$ magnetic readings under the program's ordered Wilson tangent. Use the original finite-spatial-box, infinite-time positive transfer and the energy $r^4\beta\sum_{i<j}(1-\operatorname{Re}U^{\rm sp}_{ij})$ with spacing $1/r$. For a fixed smooth compactly supported $f$, take the Riemann sum of these energies against $r^{-3} f(x)$. Subtract its vacuum expectation. The compact observable is a bounded function of a single slice at each finite regulator.

At fixed $r$ there are finitely many summands and the lattice flow clock $sr^2$ is fixed. First send $\beta=L\to\infty$ in the earlier joint local moment comparison. This covers all the terms in the packet, with complex conjugation for its reflected partner. Then send $r\to\infty$. To justify the Riemann limit at once, write its connected centered Gaussian covariance in Fourier space. The lattice spatial magnetic symbols, after temporal momentum integration, are bounded in rescaled variables by $C|p|e^{-c s|p|^2}$ for each magnetic field factor, uniformly for nonnegative temporal lags. Spatial phases have modulus one. The packet transform $r^{-3}\sum_x f(x/r)e^{i\mathbf P\cdot x/r}$ is bounded uniformly by its discrete $L^1$ norm and converges to the corresponding continuum transform at every fixed $\mathbf P$. The expanding-zone dominated convergence argument for the two independent momenta therefore applies also to the variance at zero time. It gives the measure with kernel $|\widehat f|^2$ in the previous section. [Original nonlinear fixed-clock comparison](../spatial-flow/wilson.md)

To select a specified $\mathbf k$, use $f_M(x)=M^{-3/2}w(x/M)e^{-i\mathbf k\cdot x}$ with $w$ smooth and compactly supported, $\|w\|_2=1$. Either Fourier sign gives the same radial kernel. For a real packet at nonzero momentum, combine the opposite carriers with a normalized cosine. Their squared Fourier weights converge to equal masses at opposite momenta, and their overlap tends to zero by separation of the translated Schwartz profiles. Its squared Fourier transform is an approximate unit mass at that momentum in $d^3P/(2\pi)^3$. At $s>0$ the continuum spatial-flow kernels at fixed $t\ge0$ are continuous and bounded in $\mathbf P$ by Gaussian domination. The limit $M\to\infty$ of the packet covariance thus gives the displayed fixed-momentum Laplace transform, including its finite variance. Choose $M$, then a sufficiently fine $1/r$, then a sufficiently large even $L=\beta$ to approximate any increasing finite list of integer physical time tests and the variance. Impose $L/(rM)\to\infty$ so each growing packet fits inside its box. The positive compact physical-energy measures converge weakly along the resulting diagonal: push forward by $E\mapsto e^{-E}$, use all integer moments and polynomial density on $[0,1]$, and use the absence of a limiting atom at zero in that coordinate. Their limiting masses on intervals converge at every finite endpoint. The same diagonal can include countably many target momenta by meeting finite collections successively.

For the fully flowed magnetic energy, the same packet argument at finitely many times, now on the even periodic cubes of the earlier result, transports any fixed negative test for any fixed momentum to some finite compact $SU(2)$ regulators. Full heat flow gives integrable domination already in four-dimensional Fourier space. Choose a sufficiently large *finite* packet, then a large but fixed $r$, and finally a sufficiently large $\beta=L$. This does not require taking a global spatial sum of the interacting covariance before an estimate of its tails. The finite-packet result has energy and momentum **resolution**. It gives no claim of strong convergence of exact single-momentum eigenspaces in the finite Wilson boxes.

All these compact transfers use the program's microscopic weak-coupling limit and select the bare trajectory. A calibrated interacting trajectory, a nonzero rest mass and existence for all simple groups remain separate obligations. In particular an exponential at a nonzero momentum by itself cannot supply the rest mass in Clay's problem. [Official formulation](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
