"""Recompute the exact finite-box records and test the independent character formula."""
import argparse
from fractions import Fraction as F
from itertools import combinations
import json
from math import isclose, log, pi, sqrt
from pathlib import Path
import sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import numpy as np
import sympy as sp
from scipy.special import ive, logsumexp
from response import box, cell_sources, evaluate

MODELS = ('wilson', 'abelian', 'matched')
PAIRS = (3,5,6)


def report(r):
    masks = (3,5,6,7)
    assert all(v>0 for v in r['pairs'])
    factor = sqrt(float(np.prod(r['pairs'])))
    t0 = r['triangle']
    result = {k:r[k] for k in ('faces','chords','supports')}
    result.update(V0=list(map(str,r['pairs'])),T0=str(t0),R0=float(t0)/factor)
    for model in MODELS:
        a = r['A'][model]
        v, t = [a[m] for m in PAIRS], -a[7]
        # R1_over_R0 is rational whenever T0 != 0.
        relative = t/t0 - sum(x/y for x,y in zip(v,r['pairs']))/2
        result[model] = dict(A0=str(a[0]),V1=list(map(str,v)),T1=str(t),
                             R1_over_R0=str(relative),R1=float(relative)*result['R0'])
    assert any(r['A']['wilson'][m]!=r['A']['matched'][m] for m in masks)
    return result


def compare_trees(shape, source):
    r = evaluate(shape,source)
    alt = evaluate(shape,source,reverse=True)
    for model in MODELS:
        assert r['A'][model]==alt['A'][model],(shape,model)
    assert r['pairs']==alt['pairs'] and r['triangle']==alt['triangle']
    return r


def face_links(face):
    x,a,b = face
    for d,other in [(a,b),(b,a)]:
        yield (x,d)
        far = tuple(v+int(i==other) for i,v in enumerate(x))
        yield (far,d)


def response_by_support():
    shape = (5,1,1,1)
    faces = box(shape)[0]
    f,mid,g = cell_sources(faces,(0,2,4))
    marked = f+g
    links = set().union(*(set(face_links(face)) for face,on in zip(faces,marked) if on))
    groups = [[],[],[],[]]
    for i,face in enumerate(faces):
        # Split the all-ones source into four mutually exclusive masks.
        group = 0 if marked[i] else 1 if links.intersection(face_links(face)) else 2 if mid[i] else 3
        groups[group].append(i)
    rows = {}
    for name,indices in zip(('same_face','other_face_sharing_link','middle_cell','other_disjoint'),groups):
        v = np.zeros(len(faces),dtype=int)
        v[indices] = 1
        r = evaluate(shape,lambda fs: np.stack((f,g,v)))
        rows[name] = dict(faces=len(indices),T0=str(r['triangle']),
                          T1=str(-r['A']['wilson'][7]),matched_T1=str(-r['A']['matched'][7]))
    assert sum(row['faces'] for row in rows.values())==len(faces)
    assert sum(F(row['T0']) for row in rows.values())==2*r['pairs'][0]
    for model,field in [('wilson','T1'),('matched','matched_T1')]:
        assert sum(F(row[field]) for row in rows.values())==3*r['A'][model][3]
    return rows


def character_controls():
    # A one-cell-thick open 2D rectangle admits independent plaquette variables.
    sources = lambda fs: np.eye(len(fs),dtype=int)[:3]
    flat = compare_trees((3,2),sources)
    expected = [F(-9,4),F(3,8),F(3,8),0,F(3,8),0,0,0]
    assert flat['A']['wilson']==flat['A']['matched']==expected
    assert flat['pairs']==[0,0,0] and flat['triangle']==0

    cube = compare_trees((1,1,1),sources)
    x = sp.symbols('s:3')
    u = [1/(1+z) for z in x]+[1]*3
    S = sum(u)
    coeff = sum(3*t - 18*t*t/S + 15*t**3/S**2 for t in u)/24
    for mask in range(8):
        expr = coeff
        for i in range(3):
            if mask & (1<<i):
                expr = sp.diff(expr,x[i])
        assert cube['A']['wilson'][mask]==F(expr.subs(dict.fromkeys(x,0)))
    # Independent finite-beta check against the positive character sum on S^2.
    # Divide out the complete leading Gaussian prefactor; differentiate no fitted data.
    for weights in [np.ones(6),np.array([.7,1.3,2,.8,1.2,.9])]:
        S = (1/weights).sum()
        limit = (3*S-18*(weights**-2).sum()/S+15*(weights**-3).sum()/S**2)/24
        errors = []
        for beta in (64,128,256,512):
            xval = beta*weights
            order = np.arange(1,1+int(16*sqrt(beta/S)))
            vals = 2*ive(order[:,None],xval[None,:])/xval
            logZ = logsumexp(2*np.log(order)+np.log(vals).sum(axis=1))
            logZ0 = (np.log(2/(np.sqrt(2*pi)*xval**1.5))).sum()+1.5*log(beta/S)+.5*log(pi/2)
            approx = beta*(logZ-logZ0)
            errors.append(approx-limit)
        assert max(abs(errors[i+1]/errors[i]) for i in range(3))<.53
        assert abs(2*errors[-1]-errors[-2])<4e-6
        print('sphere weights', weights.tolist(),'A',limit,'extrapolation error',2*errors[-1]-errors[-2])
    return dict(surface_A=list(map(str,cube['A']['wilson'])),plane_A=list(map(str,expected)))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--write',action='store_true',help='refresh the exact arithmetic fixture')
    args = p.parse_args()
    records = {'controls':character_controls(), 'cases':{}}
    for shape,times in [((5,1,1,1),(0,2,4)), ((7,1,1,1),(1,3,5)),
                        ((7,1,1,1),(0,2,6)), ((5,2,1,1),(0,2,4))]:
        source = lambda fs: cell_sources(fs,times)
        r = compare_trees(shape,source)
        f = source(box(shape)[0])
        assert np.all(f.sum(axis=1)==24) and np.max(f.sum(axis=0))==1
        key = 'x'.join(map(str,shape))+'@'+','.join(map(str,times))
        row = report(r)
        records['cases'][key] = row
        assert row['wilson']['T1']!=row['matched']['T1']
        assert row['wilson']['R1_over_R0']!=row['matched']['R1_over_R0']
        print(key, 'R0',row['R0'],'Wilson R1',row['wilson']['R1'],'matched R1',row['matched']['R1'],flush=True)
    # Six inward faces at each of three symmetry-equivalent boundary corners
    # of an isotropic box. The sources have no common link pairwise.
    corners = [(0,0,0,0), (2,2,0,0), (0,2,2,0)]
    def corners_source(fs):
        return np.array([[int(all(v<=y<=v+int(i in (a,b))
                                  for i,(v,y) in enumerate(zip(x,point))))
                          for x,a,b in fs] for point in corners])
    faces = box((2,2,2,2))[0]
    chosen = corners_source(faces)
    links = []
    for weights in chosen:
        edges = set()
        for (x,a,b), keep in zip(faces,weights):
            if keep:
                edges.update(face_links((x,a,b)))
        links.append(edges)
    assert all(not (a & b) for a,b in combinations(links,2))
    corner = report(compare_trees((2,2,2,2),corners_source))
    assert corner['supports']==[6]*3 and len(set(corner['V0']))==1
    records['cases']['2x2x2x2@corners'] = corner
    print('2x2x2x2 corners R0',corner['R0'],'Wilson R1',corner['wilson']['R1'],
          'matched R1',corner['matched']['R1'],flush=True)
    def global_source(fs):
        f = cell_sources(fs,(0,2,4))
        f[2] = 1
        return f
    glob = evaluate((5,1,1,1),global_source)
    assert glob['triangle']==2*glob['pairs'][0]
    for model in MODELS:
        assert -glob['A'][model][7]==3*glob['A'][model][3]
    records['global'] = dict(tree_pair=str(glob['pairs'][0]),tree_triangle=str(glob['triangle']),
                             wilson_pair=str(glob['A']['wilson'][3]),wilson_triangle=str(-glob['A']['wilson'][7]))
    records['response_by_support'] = response_by_support()
    result = json.dumps(records,sort_keys=True,indent=2,allow_nan=False)+'\n'
    path = HERE/'evidence/coefficients.json'
    if args.write:
        path.write_text(result)
    else:
        previous = json.loads(path.read_text())
        for key,row in records['cases'].items():
            ref = previous['cases'][key]
            assert isclose(row.pop('R0'),ref.pop('R0'),rel_tol=2e-15)
            for model in MODELS:
                assert isclose(row[model].pop('R1'),ref[model].pop('R1'),rel_tol=2e-15)
        assert records==previous,'exact record differs from recomputation'
    print('Exact local and integrated responses, gauge-tree invariance and source controls passed.')

if __name__ == '__main__':
    main()
