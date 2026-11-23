# Vacuum attribution in the common one-site control

C4 applied a four-lag test to G4’s reruns of Z4’s first tensor observable. G4 reproduced the three stored contrast tables, the 108 finite spectral checks, and the 64 magnetic trace checks. Under C4’s retrospective population margin at period 48, either the observable couples the vacuum to an energy below $\log 3$, or the lowest excitation in the full gauge-invariant trace has energy below **0.23018** in lattice units. The corresponding alternative at period 24 gives **0.50275**. Both branches can hold. Period 16 clears neither positive margin. [C4’s derivation and assumptions](../spectral-support/finite-readings/periodic-vacuum/README.md) · [Common control trajectories](z4-controls.zip)

For a pair of excited rows $i,j$ with $E_i<E_j$, its positive contribution is bounded by $(p_i+p_j)H_e|O_{ij}|^2$ since $p_j/p_i=e^{-T(E_j-E_i)}$. Each unordered pair contributes once to each endpoint’s row sum. The bound on all such pairs is therefore $H_eQ_T\|\overline{O^2}\|$ for the fixed, component-averaged observable. Here $Q_T$ is the Gibbs probability outside the vacuum. C4’s raw contrasts imply $Q_{48}\ge0.02730$ and $Q_{24}\ge0.01315$ if the vacuum has zero weight in the target interval and the population contrasts exceed the respective sample means less three estimated errors. The sample-to-population step has no certified coverage. [Four-lag replay](../spectral-support/finite-readings/periodic-vacuum/check.py)

For the trace bound, the normalized electric convolution $K$ fixes constants and is positive. On normalized Haar space $K\ge|1\rangle\langle1|$, so the vacuum eigenvalue of $AKA$ is at least $\|A1\|^2$ for the gauge-invariant magnetic factor $A$. The full trace equals $h_4(1)^3\|A1\|^2$ by integration of the continuous positive kernel on its diagonal. Restriction to the physical space can only decrease that trace. These steps recover C4’s cancellation. Using the positive Haar series for $c_4=\int\exp(4\operatorname{ReTr}U/2)\,dU$ sharpens the remaining constant. The semicircle density of the SU(2) scalar part gives $c_4=\sum_{j\ge0}4^j/[j!(j+1)!]\ge3293/675$. The exponential series through degree 16 and a geometric upper bound on its tail then give $h_4(1)^3=(e^4/c_4)^3<1402$. [Wilson transfer matrix, Lüscher](https://doi.org/10.1007/BF01614090)

Writing $g$ for the lowest excitation in the whole trace, $Q_T/(1-Q_T)\le1401 e^{-(T-1)g}$. The following exact rational comparisons give the displayed strict ceilings. They also show how little changes when the scalar trace estimate is sharpened. The result permits a light state of another center charge, and the fixed-time open-boundary refinement uses a different state preparation. [Matched open-time observations](../g4/full-attempt/physical-refinement/results.md)

```python
from fractions import Fraction as F
from math import factorial

c_lower = sum(F(4**j, factorial(j) * factorial(j + 1)) for j in range(6))
exp_upper = sum(F(4**j, factorial(j)) for j in range(17))
exp_upper += F(4**17, factorial(17)) / (1 - F(4, 18))
assert c_lower == F(3293, 675) and (exp_upper / c_lower)**3 < 1402
for period, q, bound in [(48, F("0.02730"), F("0.23018")),
                         (24, F("0.01315"), F("0.50275"))]:
    exponent = (period - 1) * bound
    exp_lower = sum(exponent**j / factorial(j) for j in range(50))
    assert exp_lower > 1401 * (1 - q) / q
```
