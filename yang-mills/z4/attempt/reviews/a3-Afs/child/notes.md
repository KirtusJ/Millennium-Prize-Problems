# notes (append-only)
- control: I2(2)/I1(2)=0.433127 (control.txt). Sub-agent power series gives 0.43312743 -> agree.
- Step1 table.txt: a_U1=0.7413754, a_SU2=0.4792791; z(L) increasing; predicates T1-T3 true.
- Step2 MC (prog2_mc.py), L=2: P1 3/3, P2 5/5, P3 3/3; L=3: same. Largest pulls: C(2) L=3 +2.62, m_eff(2) L=3 -2.71 (<3 but not small).
- Sub-agent (grandchild/): control I_0(0)=1 passed; I1/I0(2.3)=0.74137542 matches quadrature 0.7413754154; I2/I1(2.3)=0.47927908 matches 0.4792790783. I reran its script on a copy: identical output.
