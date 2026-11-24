"""Predicates: w(k) at k=1,2,5 matches grandchild (0.2217258034,0.6508379686,1.2736194789) within 1e-7 (my p uses h=1e-5 too, so same noise ~1e-11*k^2); w'>0 via formula at 1,2,5; formula vs FD h=1e-3 within 1e-6."""
import sys
sys.argv=['x']
exec(open('check2.py').read().split("res={}")[0])
W=lambda k:k*k*(1-3*R(k)/k-R(k)**2)
gc={1:0.2217258034,2:0.6508379686,5:1.2736194789}
ok=True
for k,g in gc.items():
    w=W(k); h=1e-3; fd=(W(k+h)-W(k-h))/(2*h); f=wp_formula(k)
    print(k,w,fd,f); ok&=abs(w-g)<1e-7 and f>0 and abs(fd-f)<1e-6
print('PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
