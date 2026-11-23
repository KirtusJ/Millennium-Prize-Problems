# notes r14-micro
Step 0: control.txt = 0.272341 (-ln tanh 1).
Step 1: register init; child started for arithmetic (A1-A15 list in child/PROMPT.txt).
Step 2: read r11-match + results. Findings: 'three lattice spacings' WRONG (extension = same 12^4 lattice extended, report §4 'third spacing not done'); LTW mismatch~0 note omitted; ext R(0) ratio 0.880(25) and Q0 +1.3sig thermalisation concern omitted; 'restart' in SF §7 not in MM.
Step 3: read r11-flowchal, r12-wild. Findings: '3/(48pi^2) to 0.25%' holds only at tau=8 (tau=16 -1.3%, tau=1 +4%); wild's free-theory-only/subtraction not checked omitted; transverse electric remainder divergence omitted; flowchal 4^4 orientation 12 only dropped.
Step 4: read r11-flowbounds, r12-chal. Findings: B2 '1e7-1e9' is builder's; challenger found 7e4-1e15 (omitted); builder DEFECT of PROOF_FREE_BOUNDS 3b-3d route omitted; v2~s^-5/2 measured-only (B3 s-scaling) not in sec 3; 2nd-process explanation 'another worker's child' not in report (report: started in its own dir, WebFetch granted, child_check.log); grid-measured inputs D4 etc omitted; 'variance ∝ b^-5, S1′' not in reports.
Step 5: read r12-vol, r13-volchal. Findings: '10^-3 to 10^-13' should be 1e-13 to 2e-2; 'Consequence for B3 ... proved under theta<1/7' overstated (challenger NOT CHECKED, U_q uniform-in-c unchecked, also needs l/sqrt(s)>~9); challenger DEFECT 'l only via Poisson' omitted.
Step 6: read r11-lit. Findings: 'locators as read by worker and its child' - child did only Q4 (FHK/LTW); 'carried out' for Cao-Chatterjee (Thm 1.6 conditional on tightness) / CCHS (local existence) mildly overstated; SF7 'one child and one grandchild saved papers' - reports show two children (r11-lit, r11-match), no grandchild.
Step 7: read r12-lean (Lean table counts match). Child finished K1 exit 0 in 86 s; control graded next.
Step 8: arith.py run1 (register arith-run1).
Step 9: arith run1: 24 met, 5 failed, 3 measured. Q5_R0/Q6_R0/Q6_Rl6/Q8 failures are my own (recomputed from rounded inputs; result file values 0.9128(328), 2.7, 7.6, 88.3 match summary). Q20 failure = summary defect. Child control 3.25 CORRECT.
Step 10: child rerun (K3) identical report.md/results.json; grandchild solve.py rerun identical; grandchild control (r=2 -> acosh((1+sqrt3)/2)) correct by algebra.
Step 11: verifies run; restart grep done.
Step 12: report.md written. Findings WRONG 5, OVERSTATED 8, OMITTED 9.
