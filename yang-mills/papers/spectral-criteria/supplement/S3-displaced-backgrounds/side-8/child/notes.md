# notes
- control: E[a0^2]=1/4 (a0^2 mean over S^3 = 1/4) -> control.txt
- wrote mc.rs (Rust, predicates P0-P4 in docstring)
- beta=0 run (2 streams,burn5,2000 meas each) done; grandchild T209 done: J1/Var=0.041705+-0.000081 (pred 1/24)
- P3 FAILED as predicted by me/grandchild (J1/Var=1/24 expected; got 0.129+-0.0023): defect of my expectation, not target: colours pv=1,2 of plane xy (pairs (Ux(1,1,0),Uy(1,0,0)) and (Ux(0,1,0),Uy(0,0,..)) ) also contain the plaquette-P links, so 3 colours touch f1 -> corrected prediction 3/24=0.125 (agrees at 1.7 sigma). Grandchild's 1/24 assumption (23 colours untouched) was wrong the same way.
- main run: 4 streams (cold,hot,cold,hot), burn 288, 500 meas each every 6 sweeps, seed 2026: J1/Var=0.0589+-0.0017, J4/Var=0.0501+-0.0019, Var f4=0.0569+-0.0021, spread 0.3417+-0.0028 (jackknife, 50-sample blocks)
- report.md written
