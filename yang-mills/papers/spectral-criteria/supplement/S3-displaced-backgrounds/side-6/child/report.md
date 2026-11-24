# T208 report (z1-mix6 child)
## Verdict table
| Item | Verdict | Evidence |
|---|---|---|
| Control (E[(TrU/2)^2]) | STANDS | control.txt = 0.250000 |
| S1 pair structure (24x27, no frozen link, no shared plaquette between pairs of a colour) | STANDS | checked over whole lattice, True |
| S2 holonomies W=-I, B=i | STANDS | computed from links |
| R1 mean spread vs .3442(.0084) | DEFECT (disagrees) | .36843(.00439), z=2.56 > 2 |
| R2 Var(f4) vs .06182(.00732) | STANDS | .04908(.00361), z=-1.56 |
| R3 J/Var f1 vs .0639(.0023) | STANDS | .07131(.00442), z=1.49 |
| R4 J/Var f4 vs .0464(.0055) | STANDS | .05740(.00375), z=1.65 |
| R5 sanity | STANDS | 0<J/Var<1, Var f1 > Var f4 |
| Grandchild beta=0 Haar check | STANDS | see below |
| Haar claim "J=Var at beta=0" | NOT CHECKED | only one colour resampled per J term, so J=Var not expected; untested |

## Numbers (full protocol: 4 streams, 200 discard, 80 meas, gap 6; results80/, analysis80.txt)
Delete-one-stream jackknife (4 streams, 3 dof, so errors are noisy):
spread .36843(.00439); Var(f4) .04908(.00361); Var(f1) .10816(.00561); J f1 .00771(.00033); J f4 .00282(.00017); J/Var f1 .07131(.00442); J/Var f4 .05740(.00375).
Per-stream means (f1,f4,spread,J1,J4): s0 cold -.31373 -.3405 .37334 .00769 .00258; s1 hot -.28576 -.33549 .35628 .00704 .00254; s2 cold -.23676 -.3045 .37611 .00861 .00327; s3 hot -.29365 -.32615 .36798 .00752 .00288.
Seeds 7101..7104 (stream 0..3), numpy default_rng. Hot/cold streams agree, so no visible start-state bias. Earlier run with 40 measurements per stream (results/, analysis40.txt) is a shorter pilot, same code.
Overall: three of four reference numbers agree within 2 combined sigma. Spread does not (z=2.56). Overall statement: NOT all agree.

## Failed predicates
R1 spread failed. It was a pre-stated expectation; I cannot tell whether it is a defect of the reference, of my code, or a chance fluctuation (4-stream jackknife has only 3 dof; z=2.56 with a t-like error would be much less significant). Not resolved. My code has no independent test of the heat bath beyond the structure and the beta=0 grandchild check on the observables (the sampler was not itself tested against e.g. a known plaquette value at this beta).
Tolerance source: 2 sigma of combined errors (95% for normal estimates); reference sigmas as given.

## Not checked
Heat-bath correctness against known plaquette expectation; autocorrelation (6-sweep gap, only 4 streams, errors from streams only); J at beta=0 on the lattice; the two other positive-sign conventions of path ordering beyond the stated one.

## Grandchild (T210, admitted and released)
Question: at beta=0 with independent Haar links on a 2x2 xy square, are E[f1^2]=1/4, E[f4^2]=1/16, E[spread]=3/4? Own control first (E[a^4]=0.125000). Outcome (400k samples, grandchild/results.md): .250770(396), .062408(131), .750273(242), all within 2 sigma (max 1.94). I reread results.md and ran nothing different; I did not rerun its code.

## Rerun
cd /home/user/z4-workers/z1-mix6/child; mkdir results80b; for s in 0 1 2 3; do python3 mix6.py $s results80b 200 80 6; done; python3 analyze.py results80b
PCP: last line of python verify: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
last line of pcpos verify: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
