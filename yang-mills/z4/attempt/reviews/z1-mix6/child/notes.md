# notes
- control.txt = 0.250000 (E[(TrU/2)^2]=E[chi_{1/2}^2]/4=1/4, Haar orthogonality)
- Grandchild (T210) done+released: control 0.125 (E a^4), MC beta=0 E f1^2=.25077(40) vs 1/4 (1.94 sigma), E f4^2=.062408(131) vs 1/16, spread .750273(242) vs .75. Haar claim "J=Var at beta=0" from the task suggestion NOT tested; not expected (only one colour resampled).
- mix6.py written; structure check (24x27 pairs, no frozen in pairs, no shared plaquettes) True; W=-I, B=i verified; timing 0.77s/measurement. Reduced to 40 measurements/stream (time budget).
