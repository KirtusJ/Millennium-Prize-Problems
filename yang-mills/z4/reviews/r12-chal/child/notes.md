# notes (appended per step)
1. init pcp done (method not found, expected). No numpy/mpmath: pure float64.
2. control.py -> control.txt = 1.086435 (matches pi^(1/4)/Gamma(3/4)); registered K1.
3. main_test.py: P0 1205/1205 unimodal; T1 241/241; T2 964/964 (max theta/bound .982 j0, ~.975 j1-4); T3 q=2 identity vs brute force 13/13, q=4 identity 13/13, bounded versions 241/241 each. K2.
4. const1_probe.py (6001 pts, j1-4): constant 1 also holds there (gap/M max .37,.62,.78 for j=2,3,4). K3.
5. const1_largej.py (outside requested range): gap/M = .90(j5) 1.12(j8) 1.28(j12) 1.44(j20) 1.54(j30) -> constant 1 FAILS for j>=8, constant 2 holds (<=2). K4.
6. grandchild: control ok, theta_2(.01)=132934.038818, theta_1(.3)=5.39340531265, theta_0(.01)=17.7245385091, Poisson vs direct rel 1e-16; I re-summed directly: same. Its rerun exits 1 only because of mode "x" files existing.
