# MK for 4d U(1), b=2 (mk.py, result.txt, control.txt)
Control: I1(1)/I0(1)=0.4464 (own continued fraction; scipy absent).

## Recursion used (my derivation; stated assumption)
1. Bond moving: group-space plaquette weight W(theta)^(b^(d-2)). Wilson W=exp(beta cos) -> beta_mv = b^(d-2) beta (=4 beta).
2. Decimation/composition, in character space: c_n' = (c_n(beta_mv))^(b^2) (b^2=4).
   Check: Villain c_n=exp(-n^2/2beta): bond move gives 1/beta -> 1/(b^(d-2) beta); ^b^2 gives 1/beta'=b^(4-d)/beta, i.e. beta'=beta in d=4 (exactly marginal), matches the quoted result. In d=2 gives c^(b^2) (area scaling), also correct.
3. Wilson variant: c_1' = [I1(4beta)/I0(4beta)]^4, refit beta' with I1(beta')/I0(beta')=c_1'. Only n=1 tracked; higher n discarded (re-fit).
Caveat: the b^2 decimation exponent is fixed by requiring Villain consistency, not independently derived from a lattice picture.

## Predicates (before running)
P1 Villain: beta'=beta for all beta (no flow).
P2 Wilson-refit, small beta: c1~beta/2 => beta'~32 beta^4, flows to strong coupling (beta->0).
P3 Wilson-refit, large beta: the Wilson refit is not Villain; expect a constant O(1) drift, not log running; (asymptotic hand calc: beta' - beta -> 3/8) i.e. weak-coupling flow, beta_n ~ beta_0 + 3n/8.
P4 an unstable fixed point separates them at O(1).

## Results
- beta0=0.5: 0.5,0.488,0.465,0.420,0.335,0.190,0.032,3e-5,~0 : flows to strong coupling in 8 steps (super-exponential, ~beta^4).
- beta0=1,2,5,10,50: beta increases monotonically, ~linear in n: increments 0.35-0.5 at beta~1-2, 0.397 at beta=10, 0.379 at 50, 0.377 at 100 (-> 3/8, matches P3). 30 steps: 1->13.5, 2->14.5, 5->17.0, 10->21.7, 50->61.4.
- Unstable fixed point near beta*~0.525 (sign change of beta'-beta, scanned at 0.025 spacing).
- Villain: exactly beta'=beta.

## Conclusions
Flow to strong coupling only for beta0 below ~0.525 (confinement-like); above it beta grows LINEARLY in the step number n (so exponentially in log-scale of length, beta ~ 0.375*log2(L)), i.e. no stall and not marginal: the non-Villain refit breaks marginality and gives drift toward weak coupling (Coulomb/ deconfined phase of 4d U(1), consistent with known first-order/ phase transition qualitatively; the MK fixed point location 0.525 is not quantitatively the true transition ~1.01 for Wilson). It is not log-running of beta in n; the Villain version stalls exactly. Result depends on the single-coefficient refit and the unverified decimation exponent; MK is an uncontrolled approximation.
