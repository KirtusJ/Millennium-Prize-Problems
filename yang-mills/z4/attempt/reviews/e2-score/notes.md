# notes e2-score (T229)
step0: control.txt = 0.272341. Register pcp initialised. Child admitted T232, started (child-run1) on ||Z||/beta, Var numerics.
step1 (geometry, from replicas.rs): coords x%n,(x/n)%n,x/n^2; frozen spatial link dir i at slice 0 iff other two spatial coords even.
 free in-plane links: u=U_x(0,1), v=U_x(1,1), w=U_y(1,0), z=U_y(1,1). frozen: U_x(0,0),U_x(1,0),U_y(0,0),U_y(0,1),U_y(2,*),U_x(*,2).
 P(x,y)=U_x(x,y)U_y(x+1,y)U_x(x,y+1)^*U_y(x,y)^*. Transport path x then y: (1,1): U_x(0,0) w. so
 g3 = U_x(0,0) w [v U_y(2,1) U_x(1,2)^* z^*] w^* U_x(0,0)^*  -> {v,z,w,w*}: auditor correct.
 colours(): o=0,pz=0: colour px+2py; pair = (x-link with odd y, y-link with odd x) of the plaquette at site: c0 (u,w), c1 (v,w), c2 (u,z), c3 (v,z). Only colours 0..3 move u,v,w,z (o=1,2 pairs have z-odd x/y links).
step2: e2.py run e2-run1 (exit 0) -> e2_run1.txt. Pre-run fix: my own docstring expectation g0:{u+,w+} was wrong (u enters P(0,0) conjugated) - corrected BEFORE first run; orientation irrelevant to claim.
 G1 PASS: g3 free content {w+,v+,z-,w-}: auditor's {v,z,w,w} correct; w once each way from the transport, plaquette P(1,1) holds v,z.
 G2 PASS colours 0..3 = (u,w),(v,w),(u,z),(v,z). G3 PASS (colour 3: Y3 contains v,z once; w fixed in colour 3). G4 PASS 24/24 colours factorize, 648/648 pairs share exactly one face.
 A1 PASS sum A^2 = 2+Y^2 (err 3e-15), min 2. A2 PASS but partly tautological (other marks' FD exactly 0) -> add e2b: FD mixed on the actual marks vs 2+Y_j^2.
 C1 PASS constants: max ratio 55.29 at b=1 (<=58<64). floors 5.616449e-7, 5.215257e-7.
 C2 PASS zero-staple: ||Z||/beta = 5.13, 2.77, 2.41, 2.41 at beta 1,3.3,10,30 (-> sqrt6); Var(Y/4)*20736 b^2 = 287..1910.
step3: e2b-run1 FAILED exit 1 (my defect: helper slice included code using undefined pred); fixed with e2_lib2.py, rerun e2b-run2.
step4: e2b-run2 PASS B1 (max err 7.5e-8). colour1 measured: sum(4DEF)^2 min 0.459 <2 -> colour 1 correctly not credited.
step5: child T232 returned. Control graded FIRST: 1.000000 correct. Child's Z expansion reread line by line (zscore.py:58-64) = mine (e2.py Zfull), heat-bath conditionals correct. Rerun in rerun_child/ (K5): all 20 rows identical (diff 0.0). max ||Z||/beta = 6.898 (<=72), min Var(Y/4)*20736 b^2 = 240.3; 20/20 cases P1-P7. Grandchild T234 zero-staple beta=1 ||Z||/beta = 5.1337 agrees with my quadrature 5.1336 (independent methods).
step6: e2c-run1 (K6) H1 PASS 81/81 cells (3 orientations x 27 cells, n=6): 4 spokes, 4 colours, >=3 bilinear colours each. (e2c.py line 6 is a dead exec('') no-op, my clutter.)
step7: report.md written; registers verified (both PASS last lines quoted). T232 released.
