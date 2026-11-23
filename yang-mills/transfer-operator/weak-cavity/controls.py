"""Independent finite-complex, compact SU(2) and bulk Fourier checks."""
from itertools import combinations, product
import json

import numpy as np
from scipy.linalg import eigh
from scipy.special import ive

from cube_control import evaluate
from thermal_control import run as check_thermal


def neighbor(x, i):
    y = list(x)
    y[i] += 1
    return tuple(y)


def cellular(n):
    sites = list(product(range(n+1), repeat=3))
    edges = [(x,i) for x in sites for i in range(3) if x[i]<n]
    index = {p:j for j,p in enumerate(edges)}
    # Rooted coordinate tree. Its path sum transports both ends of each chord.
    paths = {sites[0]: np.zeros(len(edges), dtype=int)}
    tree = set()
    for x in sites[1:]:
        i = max(j for j in range(3) if x[j])
        y = list(x)
        y[i] -= 1
        y = tuple(y)
        tree.add(index[y,i])
        path = paths[y].copy()
        path[index[y,i]] += 1
        paths[x] = path
    chords = sorted(set(range(len(edges)))-tree)
    c = []
    for k in chords:
        x,i = edges[k]
        row = paths[x]-paths[neighbor(x,i)]
        row[k] += 1
        c.append(row)
    c = np.array(c)
    rows = []
    face_index = {}
    for x in sites:
        for i,j in combinations(range(3),2):
            if max(x[i],x[j]) < n:
                row = np.zeros(len(edges),dtype=int)
                for key,sign in [((x,i),1),((neighbor(x,i),j),1),
                                 ((neighbor(x,j),i),-1),((x,j),-1)]:
                    row[index[key]] = sign
                face_index[x,i,j]=len(rows)
                rows.append(row)
    curl = np.array(rows)
    fill = np.zeros((len(chords),len(rows)),dtype=int)
    for row_index,edge in enumerate(chords):
        x,i = edges[edge]
        for j in range(i+1,3):
            for step in range(x[j]):
                base = tuple(x[a] if a<j else step if a==j else 0 for a in range(3))
                fill[row_index,face_index[base,i,j]]=-1
    assert np.array_equal(fill@curl,c)
    assert np.max(np.sum(abs(fill),axis=1))<=2*n
    assert np.max(np.sum(abs(fill),axis=0))<=(n+1)**2
    restricted = curl[:,chords]
    assert np.array_equal(restricted@c,curl)
    gram = curl@curl.T
    assert np.array_equal(gram, restricted@(c@c.T)@restricted.T)
    true = np.linalg.eigvalsh(gram)
    true = true[true>1e-9]
    lam = 4*np.sin(np.pi*np.arange(n+1)/(2*(n+1)))**2
    expected = sorted(sum(lam[list(k)]) for k in sites
                      for _ in range(max(0,sum(i>0 for i in k)-1)))
    assert len(expected)==len(chords) and np.max(np.abs(true-expected)) < 1e-10
    wrong = np.linalg.eigvalsh(restricted.T@restricted)[0]
    assert wrong < true[0]*.7
    return len(chords), float(true[0]), float(wrong)


def square(g, eta=1.):
    # Positive electric convolution in the complete character basis.
    bt, bs = 1/(eta*g*g), eta/(g*g)
    cut = int(10/g)+8
    d = np.arange(1,cut+1)
    ix, jx = np.abs(d[:,None]-d), d[:,None]+d
    vals = ive(np.arange(2*cut+2),bs)
    gs = vals[ix]-vals[jx]
    gd = (vals[np.abs(ix-1)]+vals[ix+1]-vals[jx-1]-vals[jx+1])/2
    weights = (ive(d,bt)/ive(1,bt))**2
    gram = weights[:,None]*gs*weights
    obs = weights[:,None]*(2*(gs-gd)/g**2)*weights
    ev, vec = eigh(gram,subset_by_index=[cut-2,cut-1])
    gap = np.log(ev[1]/ev[0])
    mat = vec[:,0]@obs@vec[:,1]/np.sqrt(ev[0]*ev[1])
    theta = 2*np.arcsinh(eta)
    target = 6/(1+eta*eta)
    tail = (ive(cut+1,bt)/ive(1,bt))**4
    assert tail < 1e-28
    return [float(gap),float(mat**2),float(abs(gap-2*theta)),float(abs(mat**2-target)),float(tail)]


def bulk_sum(n,t,offset=(0.,0.,0.)):
    m, b = n+1, n**(-.5)
    assert m%2==0
    k = round(t/b)
    freq = np.pi*np.arange(m)/m
    lam = (2*np.sin(freq/2))**2
    shifts=np.rint(np.array(offset)/b).astype(int)
    oscillation=np.cos(freq[1::2,None]*shifts[0])*np.cos(freq[None,1::2]*shifts[1])
    xy = lam[1::2,None]+lam[None,1::2]
    total = 0.
    for i in range(m):
        phase=(i%2)*np.pi/2-freq[i]/2
        factor = 1 if i==0 else 2*np.cos(phase)*np.cos(phase+shifts[2]*freq[i])
        omega = np.sqrt(xy+lam[i])
        nu = omega*np.sqrt(1+omega**2/4)
        total += factor*np.sum(oscillation*4*xy*np.exp(-2*k*np.arcsinh(omega/2))/(2*nu))
    scaled = total/(m**3*b**4)
    rsq=(shifts*b)**2
    tsq=(k*b)**2
    target = (tsq-rsq[0]-rsq[1]+rsq[2])/(np.pi**2*(tsq+sum(rsq))**3)
    return [k,float(scaled),float(scaled/target)]


def external_wick_pairs(sites):
    def recurse(legs):
        if not legs:
            return 1
        a, *others = legs
        return sum(recurse(others[:j]+others[j+1:]) for j,b in enumerate(others) if a//2 != b//2)
    return recurse(list(range(2*sites)))


WICK = """theorem wickColors (d v c : ℝ) :
    d*(v^2+{pairs}*c^2)+d*(d-1)*v^2-(d*v)^2={pairs}*d*c^2 := by ring
"""


def run(out):
    boxes = {str(n):cellular(n) for n in range(1,5)}
    compact = {str(eta): [square(g,eta) for g in (.24,.15,.09,.055)] for eta in (.65,1.,1.6)}
    for rows in compact.values():
        assert all(rows[i+1][2]<rows[i][2] and rows[i+1][3]<rows[i][3] for i in range(3))
        assert rows[-1][2]<.006 and rows[-1][3]<.025
    bulk = {str(n):bulk_sum(n,2.) for n in (31,63,127,255)}
    assert abs(bulk['255'][2]-1)<.025
    displaced=[bulk_sum(255,1.,r) for r in ((1.5,0,0),(0,0,1.5))]
    assert displaced[0][1]<0<displaced[1][1] and all(abs(v[2]-1)<.09 for v in displaced)
    # Six consistently oriented unit-cube faces in binary coordinate labels.
    faces = []
    for axis in range(3):
        j,k=1<<((axis+1)%3),1<<((axis+2)%3)
        for high in (False,True):
            x=1<<axis if high else 0
            a,b=(j,k) if high else (k,j)
            faces.extend([x,x|a,x|a|b,x|b])
    (out/'counts.bin').write_bytes(bytes(faces))
    pairs, triangle = external_wick_pairs(2), external_wick_pairs(3)
    assert (pairs, triangle)==(2,8)
    (out/'geometry').write_text(WICK.format(pairs=pairs))
    (out/'checks.json').write_text(json.dumps({"external_Wick_pairings":[pairs,triangle],"original_cube_bond":{str(seed):evaluate(seed) for seed in (184,966)},"thermal_SU2":check_thermal(),"boxes":boxes,"square_SU2":compact,"bulk":bulk,"displaced":displaced},indent=2)+"\n")
