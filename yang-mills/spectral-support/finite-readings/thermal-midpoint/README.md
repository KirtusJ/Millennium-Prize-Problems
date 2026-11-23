# A finite-temperature test using three midpoint readings

G4's periodic measurements can test for **nonzero transitions below a specified energy** even before vacuum contamination is quantified. For an observable O on one time slice with O self-adjoint, choose temporal circumference T and a physical stride h with 0<2h<T/2. Measure C0, C1, C2 at T/2, T/2−h and T/2−2h. Require a positive transfer trace, periodic time and finite readings. Sector restriction works for a symmetry-preserving observable if all numerators and the partition function are projected consistently. A signed twist insertion alone need not give positive weights.

For a threshold E*>0 let r=cosh(h E*) and form

$$S=2(r+1)C_1-C_2-(2r+1)C_0.$$

The unnormalized-in-the-correlator midpoint contribution from pairs with **strictly** 0<|Em−En|<E* is at least max(0,2S/(r−1)²). The trace itself is normalized by the partition function. A positive result bounds the weight in this frequency interval in the same units as C0.

To derive it, pair terms m,n and n,m in the trace. At the midpoint each unordered unequal-energy pair has weight w=2 exp(−T(Em+En)/2) |O_mn|²/Z. Its three readings are w times 1, y, 2y²−1 respectively, where y=cosh(h|Em−En|). Equal-energy pairs and the subtraction of the ensemble mean squared are constant across all three readings and cancel exactly. Each remaining contribution to S is 2w(y−1)(r−y). It is nonpositive for y≥r and bounded above by w(r−1)²/2 in the target interval, by completing the square. The coefficient is attained by a single pair with y=(r+1)/2. A nonpositive S gives a zero lower bound. This test accommodates the backward exponential directly.

For simultaneous absolute errors ej on the readings, use the lower contrast $S_{meas}-[2(r+1)e_1+e_2+(2r+1)e_0]$. Equivalently take the infimum of the linear contrast over a joint confidence region. Because r−1 shrinks quadratically with hE*, report absolute contrast uncertainties as well as weight bounds when changing the stride. A fixed physical fraction h/T avoids an automatic collapse of hE* under temporal refinement at fixed T and E*.

**Vacuum interpretation.** Take h=1 and energies 0, 2 and 2+arcosh(17/16). Couple only the two excited levels with a unit off-diagonal matrix element. At E*=arcosh(5/4), the midpoint contrast is strictly positive at every finite T. The ground state's connected correlator vanishes at all times. Even projection onto a single symmetry sector leaves this example intact when all states are neutral. Conversely the two-level thermal control in the [vacuum readings note](../three-readings/README.md) has zero midpoint contrast at the transition threshold, as required. Claims about vacuum spectral weight require additional ground-state isolation. No Wilson ensemble measurement or continuum gap follows from these controls.

The adjacent Lean source checks the polynomial identities, peak, sign and excited-pair control. Three recursive PCP OS guest emissions reproduced the checked source.
