# Result
R1 = G(8)/G(16) = 5.5796296064  (fine resolution)
- Res A (h=0.5, A=12000, N=2048): G(8)=3.341967266754e-04 G(16)=5.989579954775e-05 R1=5.5796354536
- Res B (h=0.25, A=16000, N=4096): G(8)=3.341963764579e-04 G(16)=5.989579954775e-05 R1=5.5796296064
- Tail contributions (res B, n=8,16): 4.318e-36, 4.305e-36
- Relative difference: 1.048e-06; stated tolerance 1e-6 relative
- M^2 = 3.907521731335e-03
- Control I_0(1) = 1.266066
Rerun: cd /home/user/z4-workers/a3-C/child/grandchild && python3 g4d.py (remove result.md first; mode x)
Predicates P1 control, P2 two-res<1e-6, P3 1<R1<10, P4 Bessel rep check (5.05e-19): [True, np.False_, np.True_, np.True_]
Failed predicates: ['P2']
