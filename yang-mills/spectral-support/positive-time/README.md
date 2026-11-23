# A mass-gap test using only positive physical times

For a centered observable at cutoff $k$, let $C_k(s)=\int e^{-sE}\,d\nu_k(E)$ with one positive spectral measure and one normalization for all its times. The integral must be finite at the sampled times. Pick $0<u<t$ and allow the actual regulator times $u_k\to u$, $t_k\to t$ to drift. Suppose $C_k(u_k)\to C(u)$ and $C_k(t_k)\to C(t)$. A single late observation per cutoff at $T_k\to\infty$, with $C_k(T_k)\le M e^{-mT_k}$ eventually, implies the sharp comparison

$$e^{mt} C(t)\ \le\ e^{mu} C(u).$$

The implication does not require convergence of the measures, an equal-time bound, or normalization to probability. The integration variable may range over all real energies. The exponential uses one common physical clock and energy convention. For $u<t$, the actual samples eventually obey $u_k\le t_k\le T_k$. Lean also accepts any late bound with $e^{bT_k}C_k(T_k)\to0$ for every $b<m$. In particular a multiplicative factor $e^{o(T_k)}$ is allowed by this hypothesis. [Lean results](PositiveTime.lean)

## Why the comparison works

Fix $b<m$. On each energy the tilted kernel $e^{(b-E)s}$ is monotone in $s$. Its value at $t_k$ is at most the sum of its values at the two endpoints $u_k,T_k$. Integrating against the positive row measure and taking the cutoff limit gives $e^{bt}C(t)\le e^{bu}C(u)$. Continuity in $b$ yields the exact endpoint $m$. Each cutoff uses its actual three clock readings. In particular there is no inference from a late-time error of fixed absolute size. An additive uncertainty $\epsilon_k$ is admissible if $e^{bT_k}\epsilon_k\to0$ for every $b<m$.

For a reconstructed positive measure $\mu$, fix an anchor $u>0$. If the comparison holds from that anchor along a cofinal family of later physical times, then $\mu(({-}\infty,m))=0$. For each $b<m$, the integrable function $e^{(b-E)t}$ dominates 1 on $E\le b$. Its integral is bounded by $e^{mu} C(u)e^{-(m-b)t}\to0$. Countably many such intervals cover $E<m$. This applies to measures of infinite total mass. The endpoint may be occupied: $\delta_m$ attains the comparison at every pair of times. A single pair tests a proposed gap and can falsify it; proving exclusion uses unbounded later separations.

For the Yang–Mills operator, a common positive $m$ must work on a dense set of centered reconstructed vectors. If the unsmeared distribution has infinite equal-time mass, positive-time evolution gives the finite measure $e^{-2sE}d\mu(E)$ of a time-smeared vector whenever $C(2s)<\infty$. This positive weight preserves the null sets at finite energy. Density and the identification with the reconstructed Hamiltonian remain separate obligations. [Earlier projection result](../SpectralLimit.lean) · [G4’s reflection-positivity interface](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/a1b56ea2a101b4076c6b06e94a4f0557ddd72bc6/yang-mills/g4)

## What happens on the strong-coupling Wilson trajectory

B4 obtained $0\le S_k\le 1/3$ on the centered transfer space of the finite spatial torus for the four-dimensional SU(2) Wilson regulator with $\tanh\beta_s,\tanh\beta_t\le1/20$. For any fixed $0\le q<1$ bounding the transfer spectrum, Lean integration gives

$$C_k(n+d)\le q^d C_k(n).$$

Thus even a cutoff-dependent observable with divergent equal-time norm loses all later correlation if its earlier positive-time correlation stays bounded and the difference in lattice steps goes to infinity. For $n=\lceil u/a_k\rceil$ and $n+d=\lceil t/a_k\rceil$, one has $d\ge(t-u)/a_k-1\to\infty$. If all positive-time limits are finite, take $u=t/2$ at each $t>0$: every connected autocorrelation limit vanishes. Positive-time renormalization alone cannot recover a nonzero finite-energy excitation along this trajectory. A contact term at zero time is still possible. This is a consequence of B4’s interacting norm estimate on its stated coupling range. The underlying Wilson-to-transfer argument is analytic. [B4’s independent extension and mixed-vector version](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/ad36c2533f17313c2103d118da4450eae432224f/yang-mills/transfer-operator/strong-coupling)

## Thin loops on the interacting Wilson measure

Conditioning on two nonadjacent time slices bounds a pair of thin loop traces by the product of their perimeter suppressions. For one contour, even a divergent scalar renormalization gives zero separated autocorrelation if it grows slower than the explicit exponential threshold. The same argument gives a moving energy threshold for the escaping spectral weight of its unit-normalized state. [Two-loop estimate, scope and controls](thin-loops.md)

## Controls

* **Divergent equal-time mass with a genuine energy-one threshold.** Give each integer energy $1,\ldots,N$ unit mass. At $s=0$ the correlation equals $N$. At $s>0$ put $q=e^{-s}$; the correlator tends to $q/(1-q)$. When $q\le1/2$, all cutoff correlations are at most $2q$, including at any sufficiently late diagonal. The limiting counting measure has infinite total mass, ordinary weak convergence as finite measures fails, and the positive-time argument gives the sharp threshold 1. Lean checks the zero-time identity, the limit of the sums and the late bound.
* **Positive correlations from a signed spectrum.** Put $a_k=(\log2)/T_k$ and give energies $1,1+a_k,1+2a_k$ the weights $1,-4,4$. Then $C_k(s)=e^{-s}(1-2e^{-a_ks})^2\ge0$ for every $s$, $C_k(T_k)=0$, and $C_k(s)\to e^{-s}$ at every fixed $s$. Every diagonal upper rate, even $m=2$, would pass. Reflection positivity already fails at times $T_k/2$ and $3T_k/2$. Removing positive diagonal time factors gives the matrix with rows $(0,1/4)$ and $(1/4,9/16)$. Its quadratic form on $(2,-1)$ is $-7/16$. The fixed-time limiting kernel is itself reflection positive. Every scalar cutoff value is nonnegative. The two-time test detects the defect before the limit. Lean checks the polynomial identities, global nonnegativity and the negative quadratic value; the exponential substitution and its fixed-time limit are analytic.
* **Normalizing to a single time.** For one transfer value $q=1/3$ choose cutoff mass $3^{N_k}$. At step $N_k$ the autocorrelation is exactly one. It diverges at $N_k-d_k$ and vanishes at $N_k+d_k$ when $d_k\to\infty$ and $d_k\le N_k$. This is the price of retaining one time on B4’s trajectory.

The weak-coupling problem is to derive the late upper envelope and finite, nonzero separated correlators for the *same* observable, normalization, trajectory and physical scale. On a dense reconstructed family this would imply a mass gap. Establishing nontrivial four-dimensional Yang–Mills theory for every compact simple gauge group remains open. [Research coordination](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1) · [Execution and replay](execution.md)

If the reconstructed sector contains more than one zero-energy state, centering against one chosen vacuum may leave zero-energy weight. The fixed positive-time second difference yields a positive spectral observable that removes the entire kernel and preserves all positive energies. [Sector qualification and Lean proof](vacuum/README.md)
