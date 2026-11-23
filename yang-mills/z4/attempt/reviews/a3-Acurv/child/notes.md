# notes
control: Tr exp(tX)=2cos(t/sqrt2); d2=-1
step1: first run exit1 = ModuleNotFoundError scipy (environment defect, not predicate failure); replaced expm/minimize with own code
P0 control FD d2= -0.9999999583953922 pass True
P1 max|analytic-FD| random 1.4018675498217448e-07  at Q=-1 1.667267424121377e-07 pass True
Q1 b= 0.5 lam= 1.491862189340054e-16 1-2b= 0.0 P2 pass True
Q1 b= 1 lam= -0.9999999999999997 1-2b= -1 P2 pass True
Q1 b= 2 lam= -3.0 1-2b= -3 P2 pass True
Q1 b= 4 lam= -7.000000000000003 1-2b= -7 P2 pass True
Q2 b= 0.5 random min 0.001135336891562057 local min -9.156802940042876e-16 Q1 value 0.0 diff -9.156802940042876e-16
Q2 b= 1 random min -0.9961695736633885 local min -1.0000000000000016 Q1 value -1 diff -1.5543122344752192e-15
Q2 b= 2 random min -2.9978481427289054 local min -3.0000000000000036 Q1 value -3 diff -3.552713678800501e-15
Q2 b= 4 random min -6.981999158593614 local min -7.000000000000011 Q1 value -7 diff -1.0658141036401503e-14
Q3 gauge singular values [2.         2.         2.         1.41421356 1.41421356 1.41421356
 1.41421356 1.41421356 1.41421356 0.         0.         0.        ]
rank 9
Q3 b= 0.5 horizontal eigs [1.40125195e-16 1.70218131e-16 1.72306222e-16] gauge-block min 0.9999999999999988 full lam 1.491862189340054e-16
Q3 b= 1 horizontal eigs [-1. -1. -1.] gauge-block min 0.9999999999999988 full lam -0.9999999999999997
Q3 b= 2 horizontal eigs [-3. -3. -3.] gauge-block min 0.9999999999999988 full lam -3.0
Q3 b= 4 horizontal eigs [-7. -7. -7.] gauge-block min 0.9999999999999989 full lam -7.000000000000003
Sub-agent (FD only, grandchild/): lam(Q=-1,b=1) = -0.99999973 (h=1e-3), eigs I+H: -1 x3, +1 x9. Reread code & reran in grandchild_rerun/ and grandchild_rerun2/ (K3 PCP-checked): results.txt identical. Agrees with my analytic -1.
