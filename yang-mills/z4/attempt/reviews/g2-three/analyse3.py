"""analyse3.py -- tables from results/ (no new physics). Predicates evaluated here: L4 (m_e change N-2 -> N < 1e-3),
L5 (MA 48 -> 64 change < 1e-9), C5 (E0, gaps non-increasing / converged digits, measured only).
Usage: python3 analyse3.py OUTFILE"""
import json,glob,math,sys
f=open(sys.argv[1],'x'); w=lambda s:(f.write(s+'\n'),print(s))
L=lambda n:json.load(open('results/'+n+'.json'))
v=L('lat3_v0_b2_N8'); w('v0 beta=2 N=8 L1=%s maxerr=%.2e m_e=%.10f (exact -ln(I3/I1)=2.0118191813)'%(v['L1'],max(s['L1err'] for s in v['sectors'].values()),v['m_e']))
for b in (2,4):
    d=L(f'lat3_dec_b{b}_N8'); w('dec beta=%d N=8 L2=%s diff=%s levels=%s'%(b,d.get('L2'),d.get('L2_diff'),[round(x[0],7) for x in d['levels'][:5]]))
w('\n| beta | N | m_e | sector | 2nd | 3rd | m_e beta^(1/3) | m_e beta | L3 |')
w('|---|---|---|---|---|---|---|---|---|')
tab={}; ok=True
for b in ('0.01','1','2','4','8'):
    for N in (6,8,10):
        try: r=L(f'lat3_full_b{b}_N{N}')
        except FileNotFoundError: continue
        lv=r['levels']; me=r['m_e']; tab[(b,N)]=me; bb=float(b)
        w('| %s | %d | %.7f | %s | %.7f %s | %.7f %s | %.5f | %.5f | %s |'%(b,N,me,lv[1][1],lv[2][0],lv[2][1],lv[3][0],lv[3][1],me*bb**(1/3),me*bb,r['L3']))
w('\nL4 (|m_e(N)-m_e(N-2)|<1e-3):')
nm=0;nf=0
for (b,N),me in sorted(tab.items()):
    if (b,N-2) in tab:
        d=abs(me-tab[(b,N-2)]); p=d<1e-3; nm+=p; nf+=(not p); w('  beta=%s N=%d-%d: %.2e %s'%(b,N-2,N,d,'met' if p else 'FAILED'))
w('  L4 met %d failed %d'%(nm,nf))
r64=L('lat3_full_b4_N8_MA64'); d=abs(r64['m_e']-tab[('4',8)]); w('L5 MA48->64 beta=4 N=8: %.2e %s'%(d,'met' if d<1e-9 else 'FAILED'))
from math import log
I=lambda n,x: sum((x/2)**(2*m+n)/(math.factorial(m)*math.factorial(m+n)) for m in range(60))
w('beta=0.01 strong coupling: -ln(I3/I1)=%.6f, m_e(N=8)=%.6f, diff=%.2e'%(-log(I(3,.01)/I(1,.01)),tab[('0.01',8)],tab[('0.01',8)]+log(I(3,.01)/I(1,.01))))
w('\ncontinuum h3 (w=2 unless noted): N, E0, J=2 gap (mult), 0++ gap')
for n in ['cont3_N12_w2','cont3_N16_w2','cont3_N20_w2','cont3_N24_w2','cont3_N28_w2','cont3_N24_w1.5']:
    try: r=L(n)
    except FileNotFoundError: continue
    c=r['clusters']; w('  %s dim=%d E0=%.7f gaps=%s C4=%s'%(n,r['dim'],c[0]['E'],[(round(x['E-E0'],6),x['size']) for x in c[1:4]],r['C4_counts']))
f.close()
