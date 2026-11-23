"""analyze.py -- predicates on results/*.txt produced by c1sf.py (fixed before first run).

  A1 (P5 of c1sf) |k_fd/k_an - 1| <= 1e-6 for every row.  [central diff h=1e-4: truncation ~1e-8]
  A2 (P6) |G1p(h=1e-3) - G1p(h=5e-4)| <= 1e-5 for every row  [O(h^2) truncation, Gamma1''' = O(1..10)*R^0]
     (the docstring of c1sf said 1e-7; that was a guess made before seeing |Gamma1'''|; both reported.)
  A3 P1..P4 of c1sf: gradmax<=1e-12, HDmax<=1e-12, herm<=1e-12, mineig>1e-8, every row.
  A4 SU2 d=4: Delta(R) = c1(R)-c1(R/2) > 0 for every R with R/2 also computed (the sign claim).
  A5 SU2 d=4: |Delta(R)/(2 b0 ln 2) - 1| < 0.25 for R >= 8 (my expectation; O(a/L) artefacts with c_t=1).
  A6 U1 d=4: |Delta(R)| < 0.01 for R >= 8; and 0 < c1 <= (n-m)/(2 N_t cos theta) (proved bound).
  A7 SU2 d=3: c1(R)/R tends to a positive constant: c1(2R)/c1(R) in [1.6, 2.4] for R >= 8
     (power counting: one-loop correction ~ g0^2 R in d=3; band is my expectation).
Least-squares fit c1 = A ln R + B + C/R + E/R^2 on R>=4 (SU2 d=4) printed, compared with 2 b0 = 11/(12 pi^2).
Usage: python3 analyze.py outfile
"""
import sys, math, re

def load(fn):
    rows = []
    for line in open(fn):
        line = re.sub(r'np\.float64\(([^)]*)\)', r'\1', line)
        d = {}
        for m in re.finditer(r'(\w+)=(\[[^\]]*\]|\S+)', line):
            k, v = m.group(1), m.group(2)
            if v.startswith('['): d[k] = [float(x) for x in v[1:-1].split(',')]
            else:
                try: d[k] = float(v)
                except ValueError: d[k] = v
        rows.append(d)
    return rows

out = open(sys.argv[1], 'x')
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.write(s + '\n')

fails = []; met = 0
def pred(name, ok, info):
    global met
    say(('MET ' if ok else 'FAILED ') + name, info)
    if ok: met += 1
    else: fails.append(name)

b0 = 11 / (24 * math.pi ** 2)
data = {}
for tag, fn in [('SU2d4', 'results/su2_d4.txt'), ('U1d4', 'results/u1_d4.txt'), ('SU2d3', 'results/su2_d3.txt')]:
    try: rows = load(fn)
    except FileNotFoundError: say('missing', fn); continue
    data[tag] = {int(r['R']): r for r in rows}
    for r in rows:
        R = int(r['R'])
        pred(f'A1 {tag} R={R}', abs(r['k_fd'] / r['k_an'] - 1) <= 1e-6, r['k_fd'] / r['k_an'] - 1)
        dd = abs(r['G1p_h'][0] - r['G1p_h'][1])
        pred(f'A2 {tag} R={R}', dd <= 1e-5, f'{dd:.2e} (old 1e-7 tolerance {"met" if dd <= 1e-7 else "failed"})')
        pred(f'A3 {tag} R={R}', r['gradmax'] <= 1e-12 and r['HDmax'] <= 1e-12 and r['herm'] <= 1e-12 and r['mineig'] > 1e-8,
             f"grad {r['gradmax']:.1e} HD {r['HDmax']:.1e} herm {r['herm']:.1e} mineig {r['mineig']:.5f}")

say('\nTABLE c1(R;G), d=4, eta=pi/4 (floating point; derivative error <~1e-6)')
say('R  c1_SU2  c1_U1  c1_SU2-c1_U1')
for R in sorted(data.get('SU2d4', {})):
    u = data.get('U1d4', {}).get(R)
    say(R, f"{data['SU2d4'][R]['c1']:.6f}", f"{u['c1']:.6f}" if u else '-', f"{data['SU2d4'][R]['c1'] - u['c1']:.6f}" if u else '-')

say(f'\n2 b0 ln 2 = {2 * b0 * math.log(2):.6f} ; 2 b0 = {2 * b0:.6f}')
for tag in ('SU2d4', 'U1d4'):
    D = data.get(tag, {})
    for R in sorted(D):
        if R % 2 == 0 and R // 2 in D:
            dl = D[R]['c1'] - D[R // 2]['c1']
            say(f'{tag} Delta({R}) = c1({R})-c1({R // 2}) = {dl:.6f}  ratio to 2b0ln2 = {dl / (2 * b0 * math.log(2)):.4f}')
            if tag == 'SU2d4':
                pred(f'A4 SU2 Delta({R})>0', dl > 0, dl)
                if R >= 8: pred(f'A5 SU2 Delta({R}) within 25% of 2b0ln2', abs(dl / (2 * b0 * math.log(2)) - 1) < 0.25, dl)
            else:
                if R >= 8: pred(f'A6 U1 |Delta({R})|<0.01', abs(dl) < 0.01, dl)
U = data.get('U1d4', {})
for R in sorted(U):
    T = R; d = 4
    n = R ** 3 * (T + 3 * (T - 1)); m = R ** 3 * (T - 1) + 1; Nt = 3 * R ** 3 * T
    th = (math.pi / 2) / R ** 2
    bound = (n - m) / (2 * Nt * math.cos(th))
    pred(f'A6b U1 R={R} 0<c1<=bound', 0 < U[R]['c1'] <= bound, f"c1={U[R]['c1']:.6f} bound={bound:.6f}")

# fit
S = data.get('SU2d4', {})
Rs = [R for R in sorted(S) if R >= 4]
if len(Rs) >= 4:
    import numpy as np
    for cols, name in [((lambda R: [math.log(R), 1, 1 / R, 1 / R ** 2]), 'A lnR + B + C/R + E/R^2'),
                       ((lambda R: [math.log(R), 1, 1 / R]), 'A lnR + B + C/R')]:
        M = np.array([cols(R) for R in Rs]); y = np.array([S[R]['c1'] for R in Rs])
        coef, *_ = np.linalg.lstsq(M, y, rcond=None)
        say(f'fit {name} on R={Rs}: coef={coef.tolist()} maxres={np.abs(M @ coef - y).max():.2e}; A/(2b0)={coef[0] / (2 * b0):.4f}')
    # fit with A fixed to 2b0
    M = np.array([[1, 1 / R, 1 / R ** 2] for R in Rs]); y = np.array([S[R]['c1'] - 2 * b0 * math.log(R) for R in Rs])
    coef, *_ = np.linalg.lstsq(M, y, rcond=None)
    say(f'fit A=2b0 fixed: B,C,E={coef.tolist()} maxres={np.abs(M @ coef - y).max():.2e}')

D3 = data.get('SU2d3', {})
for R in sorted(D3):
    say(f"SU2 d=3 R={R} c1={D3[R]['c1']:.6f} c1/R={D3[R]['c1'] / R:.6f}")
    if 2 * R in D3 and R >= 8:
        q = D3[2 * R]['c1'] / D3[R]['c1']
        pred(f'A7 SU2 d3 c1({2 * R})/c1({R}) in [1.6,2.4]', 1.6 <= q <= 2.4, q)
say(f'\nCOUNTS met={met} failed={len(fails)} failed_list={fails}')
