"""A single signed four-cube observable with two exact calibration nulls."""
import argparse
from fractions import Fraction as F
import json
from math import gcd, isclose, lcm, sqrt
from pathlib import Path
import sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import numpy as np
from response import box, cube_sources, evaluate

def calculate(shape, ends, origins):
    fs = box(shape)[0]
    left,right = cube_sources(fs,ends)
    profiles = [cube_sources(fs,group).sum(axis=0) for group in origins]
    def run(profile, reverse=False):
        return evaluate(shape,lambda faces: np.stack((left,right,profile)),reverse)
    columns = [run(f) for f in profiles]
    tree = [r['triangle'] for r in columns]
    matched = [-r['A']['matched'][7] for r in columns]
    wilson = [-r['A']['wilson'][7] for r in columns]
    cross = [tree[(j+1)%3]*matched[(j+2)%3]-tree[(j+2)%3]*matched[(j+1)%3]
             for j in range(3)]
    denominator = lcm(*(v.denominator for v in cross))
    nums = [int(v*denominator) for v in cross]
    common = gcd(*nums)
    assert common and nums[2]
    sign = 1 if nums[2]>0 else -1
    coefficients = [sign*n//common for n in nums]
    h = sum(c*f.astype(object) for c,f in zip(coefficients,profiles))
    assert all(not (h[i] and (left[i] or right[i])) for i in range(len(fs)))
    r,alt = run(h),run(h,True)
    for m in ['wilson','abelian','matched']:
        assert r['A'][m]==alt['A'][m]
    assert r['triangle']==alt['triangle']==0
    assert r['variances']==alt['variances'] and all(v>0 for v in r['variances'])
    assert r['A']['abelian'][7]==r['A']['matched'][7]==0
    t = -r['A']['wilson'][7]
    assert t==sum(c*s for c,s in zip(coefficients,wilson)) and t!=0
    scale = max(map(abs,coefficients))
    relative = [F(c,scale) for c in coefficients]
    standard_squared = t*t/np.prod(r['variances'])
    standard = (1 if t>0 else -1)*sqrt(float(standard_squared))
    susceptibility = t*t / (r['pairs'][0]**2*r['variances'][2])
    normalized = (1 if t>0 else -1)*sqrt(float(susceptibility))
    data = dict(shape=shape,ends=ends,profiles=origins,
                coefficients=list(map(str,coefficients)),relative=list(map(str,relative)),
                T0=list(map(str,tree)), matched_T1=list(map(str,matched)), wilson_T1=list(map(str,wilson)),
                combined_T0='0',combined_matched_T1='0',combined_wilson_T1=str(t),
                variances=list(map(str,r['variances'])),standard_squared=str(standard_squared),
                standard=standard,endpoint_covariance=str(r['pairs'][0]),
                log_response_squared=str(susceptibility),log_response=normalized)
    print('relative source weights',[float(v) for v in relative])
    print('unscaled integer-source T1',t)
    print('variance-normalized Wilson response',standard,'tree and both Abelian responses exactly zero')
    print('relative response of endpoint covariance',normalized,flush=True)
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true')
    args = parser.parse_args()
    time_group = [[(t,0,0,0) for t in group] for group in [(2,6),(3,5),(4,)]]
    transverse_group = [[(2,x,0,0)] for x in range(3)]
    data = {
        'time':calculate((9,1,1,1),[(0,0,0,0),(8,0,0,0)],time_group),
        'space':calculate((5,3,1,1),[(0,0,0,0),(4,0,0,0)],transverse_group),
    }
    path = HERE/'evidence/null.json'
    if args.write:
        path.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    else:
        old = json.loads(path.read_text())
        for key in data:
            for field in ('standard','log_response'):
                assert isclose(old[key].pop(field),data[key].pop(field),rel_tol=2e-15)
        assert old==json.loads(json.dumps(data))

if __name__=='__main__':
    main()
