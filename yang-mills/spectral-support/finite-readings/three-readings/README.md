# Sharp spectral weight from three positive-time readings

For a vacuum connected autocorrelator with a positive spectral measure, fix physical base time t>0, stride h>0 and a threshold E*>0. Set q=exp(−h E*) and x=exp(−h E). Write Cj=C(t+jh) for j=0,1,2 and assume C0>0. The probability law tilted by exp(−tE) has moments m=C1/C0 and z=C2/C0. A measured triplet is feasible on the closed transfer interval [0,1] exactly when m lies in [0,1] and m²≤z≤m. An atom at x=0 is a compactified infinite-energy endpoint. Vacuum subtraction must remove the entire zero-energy contribution if all counted weight is to be called excited.

The smallest possible **fraction of the correlator at time t from energies strictly below E*** is given by the first applicable row. These extrema are over measures on [0,1]. The threshold itself counts outside the event.

| Condition | Minimum | Attaining support |
|---|---:|---|
| z≤qm | 0 | 0 and z/m |
| m>q and z≤(1+q)m−q | (m−q)²/(z−2qm+q²) | q and b=(z−qm)/(m−q) |
| Otherwise | (z−qm)/(1−q) | 0, q and 1 |

For the first row, place mass m²/z at z/m when z>0, using the point mass at zero when z=0. In the second row b is in (q,1] because z≥m² and the row condition bounds b above. Put mass (m−q)/(b−q) at b and the rest at q. The polynomial 1−(b−x)²/(b−q)² minorizes the event indicator and equals it at both support points. In the third row the masses at 1, q and 0 respectively are (z−qm)/(1−q), (m−z)/(q(1−q)), and (z−(1+q)m+q)/q. Each is nonnegative under the row conditions. The polynomial x(x−q)/(1−q) minorizes the indicator and agrees at all three points. Substitution verifies both moments in every row. For strict exclusion of either transfer endpoint the lower certificates still hold, although a displayed extremizer can be inadmissible.

**Uncertain measurements.** For any displayed minorant P(x)=a0+a1 x+a2 x², a simultaneous bound |Cj−Yj|≤ej certifies an absolute tilted weight of at least max(0,Σ ajYj−Σ |aj|ej). Divide by Y0+e0 if positive for a fraction. Selecting b after inspecting the readings preserves this guarantee because the same joint observation event controls every coefficient vector. A point estimate substituted into the piecewise table has no such guarantee. For weight strictly above E*, reflect x to 1−x and use moments 1−m and 1−2m+z with threshold 1−q. Three readings of one probe provide no lower bound on the first excitation energy of the full theory.

**A finite temporal circle can give a false positive.** Take energies 0 and log 2, a unit off-diagonal probe, stride one, temporal circumference eight and base time one. The thermal trace gives Cj=(2^(7−j)+2^(1+j))/257, hence readings (130,68,40)/257. At E*=log 2 the table returns 6/65 of the base reading strictly below the only transition energy. The backward exponential produces this false signal even with exact data, zero probe mean, and valid moment inequalities. If a transfer trace is used, bound the difference from the vacuum correlator jointly at all three lags and include it in the errors, or derive a trace-specific kernel. Increasing the number of configurations cannot remove temporal wrapping.

**Verification.** The companion Lean file checks the pointwise inequalities and extremal moment identities. Three PCP OS guests emitted the source in sequence, each after integer controls for its assigned polynomial. The integral argument, case partition, and transfer interpretation are given above. This criterion targets the physical-time test in issue #1 and complements the [matrix moment completion test](../moment-problem.md).
