# Matched scale, observables and errors

### Independent calibration

Fix $\ell$ by $g_{\mathrm{SF}}^2(\ell)=2.38$ in pure SU(2). Use the isotropic Wilson regulator, $\beta=4/g_0^2$, at each cutoff. Francesconi, Panero, Preti and Smecca measured the Schrödinger-functional coupling on an $N^3\times N$ interval with periodic space, Dirichlet spatial links in time and $c_t=1$. At $\eta=\pi/4$, $g_{\rm SF}^2=-24N^2\sin[\pi/(2N^2)]/\langle\partial_\eta S\rangle$. I used their direct/reverse averages at $\ell$ in Tables 2–3, taking $\beta$ linear in $1/u$ between the two neighboring measurements. No spectral observable enters the tuning. Their Table 4 reproduces earlier work. [Francesconi et al., Eqs. 10–14 and Tables 2–4](https://arxiv.org/pdf/2003.13734#page=12) · [Tabulated data and interpolation](calibration.py)

| $N$ | Bare $\beta$ used | Linear in $u$ | Leave the closest anchor out, linear in $1/u$ |
| ---: | ---: | ---: | ---: |
| 5 | 3.196581051 | 3.197719246 | 3.200309188 |
| 6 | 3.276133577 | 3.276310274 | 3.279837317 |
| 7 | 3.342724170 | 3.342736605 | 3.346434001 |
| 8 | 3.399810242 | 3.399986279 | 3.403249317 |
| 10 | 3.493705679 | 3.494749511 | 3.496960095 |

The nearest published $u$ ranges from 2.37012 to 2.390472. Changing local interpolation changes $\beta$ by at most 0.00114. Removing the closest anchor changes it by at most 0.00373. These differences check interpolation sensitivity; neither bounds all possible curvature of the calibration curve. Separate chains in the Dirichlet geometry measure $\langle\partial_\eta S\rangle$ directly by differentiating the endpoint links. The derivative agrees with a symmetric action difference on a fluctuating field and reproduces $4/\beta$ on the classical linear Abelian field. Equal renormalized coupling defines the finite-size scheme. Matching has finite statistical and cutoff uncertainty, including possible $O(a/\ell)$ effects from the SF boundaries.

### Spectroscopy

The spectral ensembles use the same $(N,\beta)$ in an $N^3$ periodic spatial box with free temporal ends. Spatial endpoint plaquettes have weight $1/2$, temporal plaquettes have weight one, and there is no temporal seam. With the symmetric spatial half-weights in the transfer $T$, the boundary vector is $1$ at each end. Gauss and all three center projections preserve this vector. The slab length is $6\ell$ in production. An independent endpoint comparison at $N=5,10$ uses $8\ell$. One update cycle is a full SU(2) heat-bath sweep and one deterministic action-preserving overrelaxation sweep. Each stream starts independently from identity links or independent Haar links. The cold SF start uses the classical field. [Wilson sampler](matched.rs) · [Open temporal boundaries in lattice gauge theory](https://arxiv.org/abs/1105.4749)

At each spatial site, form winding holonomies $P_i=(p_i,\mathbf v_i)$ in scalar-vector quaternion notation. Set $A_i=(4p_i^2-1)/3$ and $\mathbf W_i=p_i\mathbf v_i$. The three cyclic diagonal differences $A_j-A_k$ give a redundant basis for $E^+$. The three $\mathbf W_j\cdot\mathbf W_k$ give $T_2^+$. Each is invariant under independent spatial center flips. A loop with imaginary part alone would change sign under a flip. The contractible reading uses four equally oriented square loops in the $jk$ plane based at the same site; their mean imaginary quaternion is $\mathbf B_i$. Use $|\mathbf B_j|^2-|\mathbf B_k|^2$ and $\mathbf B_j\cdot\mathbf B_k$ for $E^+$ and $T_2^+$. Their target square side is $\ell/4$. At nonintegral $N/4$ mix the *completed tensor readings* at its two adjacent integer sides with linear weights. These finite stencils differ across cutoffs. All readings are summed over space and divided by $N^3$ to project to zero momentum. The insertions are gauge invariant. A signed coordinate reversal and an axis interchange test the actual tensor implementation. C4 uses a different denominator and homogeneous-mode normalization. [C4’s specified observable and scope](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7109972966)

A follow-up repeats two production trajectories per size with spatial APE smearing at each observation, $\alpha=1/2$ and $\lfloor N^2/12+1/2\rfloor$ simultaneous spatial iterations. Normalize the sum of the original link with weight $1/2$ and its four spatial staples with weight $1/8$ each. The iteration count scales as $1/a^2$, with finite rounding. This matches a nominal smoothing scale; its physical radius has no independent calibration here. The operation stays on one time slice, broadens the spatial support and leaves the Markov chain intact. The saved unsmeared plaquette is a bitwise trajectory control against the corresponding production prefix. Statistics for the smoothed and unsmeared readings on these trajectories are paired. [APE collaboration, original spatial smearing study](https://www.sciencedirect.com/science/article/abs/pii/0370269387911609)

For tensor readings calculate the mean component product, averaging its three components and all source-sink pairs with both ends at least $\ell$ from the time boundaries. Repeat with a $2\ell$ margin. Cubic symmetry forces the one-point functions to zero at every slice. For unlike probes use the mean of both orderings. For the scalar one-cell plaquette subtract the separately estimated one-point profile at each insertion time. Its plug-in estimate retains finite-sample bias. Interpolate correlation values between adjacent integer lags when necessary. The physical time $\tau=\ell$ is an exact integer separation at every $N$. The effective slope between $t_1\ell$ and $t_2\ell$ is $\log[C(t_1\ell)/C(t_2\ell)]/(t_2-t_1)$. It can be evaluated when both measured correlations are positive. The program retains negative estimates and undefined errors.

Every open-time numerator with source at $s$ has the boundary factors $\langle1,T^s O T^k O T^{T_{\rm lat}-s-k}1\rangle/Z$. Changing the size of the central interval or the source window changes the prepared state. In particular the resulting slopes have no rigorous variational interpretation as vacuum masses. A symmetric numerator with the two exterior preparations held fixed has a positive spectral measure, but the normalization then also varies with total slab length. The open-boundary comparison tests sensitivity; a certified vacuum isolation or partition-function bound remains missing. A4’s midpoint and B4’s thermal-purity tests use a periodic trace. [A4’s open-time qualification](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/4ff9ae7/yang-mills/spectral-support/finite-readings/thermal-midpoint/README.md) · [B4’s purity condition](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7109901327)

### Sample and uncertainty convention

| Ensemble | Independent streams per $N$ | Burn cycles | Saved configurations per stream | Stride |
| --- | ---: | ---: | ---: | ---: |
| SF pilot | 2 | 192 | 256 | 3 |
| SF check | 2 | 384 | 1,024 | 3 |
| Open pilot | 2 | 112 | 96 | 3 |
| Open production | 4 | 384 | 320 | 3 |
| Longer slab, $N=5,10$ | 2 | 160 | 144 | 3 |
| Smoothed production prefix | 2 paired | 384 | 192 | 3 |
| Spatial momentum prefix, $N=5,7,10$ | 2 paired | 384 | 192 | 3 |

Each estimate pools streams of equal length only within its ensemble. Recompute nonlinear observables inside every deletion. The quoted standard error is the largest of the delete-one-block jackknife errors from consecutive blocks of 8, 16 and 32 saved configurations, and the delete-one-whole-stream error. The latter is omitted for a single stream. A block size must divide the stream length and yield at least three blocks. The 144-configuration boundary comparison therefore omits the 32-configuration block. Errors and split-start comparisons are diagnostics with limited independent replication. They do not control autocorrelation beyond the sampled histories or bias common to all starts. A nonpositive input to a replicate log leaves its error undefined. Continuum fits have additional scale, boundary, overlap and extrapolation systematics. [Data reduction](analysis.py)
