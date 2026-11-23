# notes (r8-tangent child)

- init pcp: OK, method not pinned (expected).
- STEP 0 control.py: Schwinger rep G=int_0^inf [e^{-2t}I0(2t)]^4 dt. v1 printed 0.154932559 and PASSed the
  2e-6 predicate, but it was off by 8.3e-7 = e^-14: the t-integral started at t0=e^-14, so the head
  int_0^{t0} a^4 dt ~ t0 was missing. control_v2.py adds the head and gives 0.154933390 (known 0.15493339).
  control.txt kept as written (no overwrite); control_v2.txt holds the corrected value.
  In main.py the lower limit is u=-30, so the head is negligible.
- Phases: theta~_mn = p_m A~_n - p_n A~_m, p=e^{ik}-1; P=(p^)(p^)^dag/|p|^2 gives the formula in the task.
  t12/t13 off-diagonal entry = p2*conj(p3)/|p|^2 -> real part f2 f3/(4F) (positive).
- (a) equipartition: rank of exact 2-cochains per site = d - 1 (d links minus 1 gauge mode), spread over
  d(d-1)/2 plaquettes, so <theta^2> = 2g^2/d, which is 0.5 g^2 at d=4. On the torus it is exactly (1-1/N)/2 with N=L^4.
- main.py: all predicates P1-P6 PASS. Real-space L=4 SVD projector matches Fourier to 3e-16.
- Observation: in infinite volume C(e1, coplanar) = -C(e3, parallel) = -0.0688747458 to all printed digits. The finite L values differ.
