# notes (child, r9-mag)

- Step 0 control: max at u=575/864, value 1329409/442368; 99/32 - max = 39167/442368 = 0.088539 -> control.txt.
- PCP workspace `pcp` initialised (method not pinned warning, as expected).
- Sources read: input/README.md (electric endpoint), input/excited-band_README.md, input/execution.md.

## (a) by hand
- uK bound: K+gu<=B<=17sqrt(g)/8+3/16 => uK <= 17t/8 - t^2 + 3u/16 (t=sqrt(g)u) <= (17/16)^2 + 3u/16 = 289/256+3u/16. OK.
- sphere step: (3-4S)^2<=16KS <=> 9 <= 16KS+24S-16S^2 ; negative branch S>3/4 => 24S>18>=9 (needs K>=0). OK.
- (2u-u^2)(K+3/2) = (2-u)(uK+3u/2) <= (2-u)(289/256+27u/16) [needs 2-u>=0]. 3/16+24/16=27/16 OK.
- max of (2-u)(289/256+27u/16) on [0,2]: vertex u=575/864 in [0,2], value 1329409/442368 = 3.00513 <= 99/32 = 3.09375. OK (slack 0.0885).
- 9<=(16K+24)S <=> S(K+3/2)>=9/16, and forces K+3/2>0 when S>0.
- 2u-u^2 <= (99/32)/(K+3/2) <= (99/32)(16/9)S = (11/2)S. OK.
- M0 = 4(2u-u^2-S) <= 4(11/2-1)S = 18S = (18/(4kappa)) M1 => M1 >= (2kappa/9) M0. OK.

## (b) by hand
- pointwise E <= L + E^2/U + U 1_[L,U](E) for E>=0: three cases OK.
- L M0 = (kappa/18) M0 <= (kappa/18)(9/(2kappa)) M1 = M1/4 ; M2/U <= D A/(4D) = A/4.
- U nu >= 3M1/4 - A/4 >= A/2 => nu >= A/(2U) = A^2/(8D). OK.
- 4D/A > kappa/18 is automatic: D>=M2>=M1^2/M0 >= M1 (2kappa/9) >= 2kappa A/9 => 4D/A >= 8kappa/9.

## Task 3 by hand
- Old: L=A/16 used L*M0 <= (A/16)*4 = A/4 (mass bound M0<=4). K_F variant: L=A/(4K_F), M0<=K_F.
- New: the low-energy term bound L*M0 <= M1/4 via M1 >= (2kappa/9)M0 (variance-retaining relation), not the mass bound.
- kappa/18 independent of g; A/16 = 9kappa/(128(1+B)) depends on g.
- CAVEAT: A/16 > kappa/18 iff 1+B < 81/64 iff B < 17/64; for g<17/64, B=g, so for g<17/64 the OLD edge is higher. "stronger" is not pointwise in g.

## Runs
- scripts/exact_a.py -> exact_a.out.txt : E1-E5 PASS (PCP check K1). max (2u-u^2)/S seen 5.3175 < 5.5.
- scripts/band_b.py : killed (too slow, unvectorised LP); band_b.out.txt is empty (0 bytes), left in place.
- scripts/band_b2.py -> band_b2.out.txt : INVALID B4 numbers (3.88 etc.). Cause: MY optimizer accepted p=-1e-10 with E~4e5
  (M2 error ~18). Hand 2-atom bound showed 3.88 < 9/2 was impossible -> my tool was wrong, not the target.
- scripts/band_b3.py -> band_b3.out.txt : fix (clip then relative-tolerance check), D grid extended. B1-B6 PASS (PCP check K2).
  min ratio nu([L,U])/(A^2/8D) -> 9/2 as D/(kappa A) -> inf (6.92 at D=5, 4.58 at D=100, 4.5002 at D=1e6, L=1,A=1).
  Hand: extremal = atom just below L with mass b=(e-4L)w/(3L) plus band atom at e solving 3Ae^2=4D(e-L), w=3A/(4(e-L)) -> 9A^2/(16D).
  D < 2kappa A/9 (=4 at L=1,A=1) is infeasible, consistent with D >= M1^2/M0 >= (2kappa/9)A.
- verify: PASS.
