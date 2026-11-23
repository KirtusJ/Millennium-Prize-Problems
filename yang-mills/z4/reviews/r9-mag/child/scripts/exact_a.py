"""Exact-fraction check of item (a) of the electric-endpoint note.
Predicates (fixed before running):
 E1: vertex of q(u)=(2-u)(289/256+27u/16) is u*=575/864 in [0,2], q(u*)=1329409/442368, q(u*)<=99/32,
     and q(u)<=99/32 on an exact grid of 2001 points of [0,2].
 E2: (2u-u^2)(K+3/2) == (2-u)(uK+3u/2) identically (checked on random exact rationals), and 3/16+3/2 == 27/16.
 E3: (99/32)*(16/9) == 11/2 ; 4*(11/2-1) == 18 ; 4/18 == 2/9.
 E4: (17/16)^2 == 289/256 and 17t/8 - t^2 <= 289/256 on exact grid.
 E5: random exact instances (u,K,S) with 0<=u<=2, S in [0,1], uK<=289/256+3u/16, 9<=(16K+24)S
     all satisfy 2u-u^2 <= 11S/2 and 4*(2u-u^2-S) <= 18 S.
Exit 0 iff all hold. Seed 12345.
"""
from fractions import Fraction as F
import random, sys
random.seed(12345)
ok = True
def chk(name, c):
    global ok
    print(name, "PASS" if c else "FAIL"); ok &= bool(c)
q = lambda u: (2-u)*(F(289,256)+F(27,16)*u)
# derivative: 575/256 - 27u/8
us = F(575,256)/F(27,8)
chk("E1", us == F(575,864) and 0<=us<=2 and q(us)==F(1329409,442368) and q(us)<=F(99,32)
    and all(q(F(i,1000))<=q(us) for i in range(2001)))
print("  99/32 - q* =", F(99,32)-q(us), float(F(99,32)-q(us)))
e2 = F(3,16)+F(3,2)==F(27,16)
for _ in range(200):
    u=F(random.randint(0,2000),1000); K=F(random.randint(0,10**5),997)
    e2 &= (2*u-u*u)*(K+F(3,2)) == (2-u)*(u*K+F(3,2)*u)
chk("E2", e2)
chk("E3", F(99,32)*F(16,9)==F(11,2) and 4*(F(11,2)-1)==18 and F(4,18)==F(2,9))
chk("E4", F(17,16)**2==F(289,256) and all(F(17,8)*F(i,500)-F(i,500)**2<=F(289,256) for i in range(0,2001)))
n=0; e5=True; tight=F(0)
while n<20000:
    u=F(random.randint(0,4000),2000); S=F(random.randint(1,1000),1000)
    Kmin=F(9,16)/S-F(3,2); Kmax=(F(289,256)+F(3,16)*u)/u if u>0 else F(50)
    Kmin=max(Kmin,F(0))
    if Kmin>Kmax: continue
    K=Kmin+(Kmax-Kmin)*F(random.randint(0,1000),1000)
    n+=1
    e5 &= (2*u-u*u)<=F(11,2)*S and 4*(2*u-u*u-S)<=18*S
    if S>0: tight=max(tight,(2*u-u*u)/S)
chk("E5", e5)
print("  instances:", n, " max (2u-u^2)/S seen:", float(tight), "(bound 5.5)")
print("ALL PASS" if ok else "SOME FAIL"); sys.exit(0 if ok else 1)
