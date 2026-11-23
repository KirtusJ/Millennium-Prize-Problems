# Return of the same coarse plaquette on two time slices

We measured the actual Euclidean-time return of a coarse loop in periodic four-dimensional SU(2) Wilson ensembles at the two matched bare couplings from [PR #26](../full-complement/fixed.md). This probes a different operation from refreshing 24 colours at one fixed background. For the same spatial location and orientation at each endpoint, the reported ratio is the number of paired hits divided by the number of initial hits. In equilibrium it estimates $\Pr(A_\theta(t)\mid A_\theta(0))$, averaged over starting fields in the gate. The conditional row supremum in the [theorem](return.md) requires control over every starting field. A small averaged return alone cannot supply it.

The table uses a radius of 1.2 radians about $-I$, chosen from a grid of six radii because it has the most paired hits. Parentheses give paired delete-one-stream standard errors in the last digits. $L$ is the spatial box length and $a=L/N$.

|Spatial side and coupling|Gate marginal|Return after $a$|Return after $2a$|Return after $L/2$|
|---|---:|---:|---:|---:|
|6, Haar ($\beta=0$)|0.2740(6)|0.2747(7)|0.2748(17)|0.2734(19)|
|6, $\beta=3.276133577$|0.03995(23)|0.05035(210)|0.04099(212)|0.03868(201)|
|8, $\beta=3.399810242$|0.03482(19)|0.04640(74)|0.03583(78)|0.03532(57)|

At spatial side eight the four streams recorded 54,761 starting hits in 1,572,864 loop readings, with 2,541 paired hits one slice later and 1,934 at half a box. At radius 0.2 there were only 50 starting hits and zero paired hits at each of the three lags. This leaves the tails empirically unresolved. At radius 1.2 the hot- and cold-start half-box returns on side eight were 0.03511 and 0.03553. At $\beta=0$ distinct time slices are independent and the exact marginal and return both equal $(\theta-\sin\theta\cos\theta)/\pi$. The finite-coupling half-box returns lie close to the marginal for this observable and these temporal preparations. The largest eigenvalue of the fine transfer or its compression need not be attained by this indicator.

**Reproduction.** The temporal period is $2N$ at every point. For each of the three designs run four independent streams, alternating cold and hot initialization, with base seeds 2417301, 2517301 and 2617301 in table order and offsets $7919i$ for $i=0,1,2,3$. Discard four sweeps at Haar and 288 sweeps at the two positive couplings. Take 128 measurements per stream with three full heat-bath sweeps between successive observations. Each measurement covers every spacing-two coarse plaquette in the three spatial orientations and every time origin. The location, orientation and radius stay fixed across each lag. Radii are 0.2 through 1.2 in steps of 0.2. The measured observables are gauge invariant. The simulations use finite periodic time, and autocorrelation, finite preparation and four-stream uncertainty limit inference.

Compile [returns.rs](returns.rs) with Rust 2021 and optimization. Its arguments are coupling, seed, hot flag (0 or 1), spatial side, temporal period, burn sweeps, and measurement count. The executable reuses the [deposited single-link Wilson heat bath](../../g4/full-attempt/two-site-gap/wilson_mc.rs). The raw archive gives exposures, hits and the three lag counts by measurement. Run the reduction with Python and NumPy. [Raw stream counts](returns.zip) · [Paired reduction](returns.py)
