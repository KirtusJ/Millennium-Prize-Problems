"""Reduce the two pinned Z4 archives without importing the original reduction code."""
from collections import defaultdict
from hashlib import sha256
from itertools import combinations, product
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tarfile

import numpy as np


PIN = "9101d04632d396701e3b13c49312d8fc39bf79bd"
ROOT = Path(__file__).resolve().parent
BETA = {6: 3.276133577, 8: 3.399810242}


def archived(n, path=None):
    if path:
        raw = Path(path).read_bytes()
    else:
        name = f"yang-mills/z4/attempt/reviews/z1-mix{n}/results.tgz"
        raw = subprocess.check_output(["git", "-C", ROOT, "show", f"{PIN}:{name}"])
    blob = b"blob " + str(len(raw)).encode() + b"\0" + raw
    from hashlib import sha1
    assert sha1(blob).hexdigest() == {6:"2f2ebfdd45fe988f4264fd2e4e221b0bcc9adbad",8:"87a155984c3cae837fc83b60059b0934517774b1"}[n]
    print(n, "archive sha256", sha256(raw).hexdigest())
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r|gz") as t:
        return {m.name: t.extractfile(m).read() for m in t if m.isfile()}


def mul(p, q):
    v, w = p[1:], q[1:]
    return np.r_[p[0]*q[0]-v@w, p[0]*w+q[0]*v+np.cross(v,w)]


def angles(n, lines=None, delta=0):
    field = {}
    if lines is not None:
        for site, axis, *q in np.loadtxt(io.BytesIO(lines), ndmin=2):
            field[int(site), int(axis)] = np.array(q)
    else:
        field[2,1] = np.array([-np.cos(delta), 0, 0, np.sin(delta)])
        field[2,2] = np.array([0., 1, 0, 0])
    one = np.array([1.,0,0,0])
    out = []
    for z,y,x in product(range(0,n,2), repeat=3):
        for i,j in combinations(range(3),2):
            pos = [x,y,z]
            q = one
            for axis, sign in ((i,1),(j,1),(i,-1),(j,-1)):
                for _ in range(2):
                    if sign < 0:
                        pos[axis] = (pos[axis]-1) % n
                    key = (pos[0]+n*(pos[1]+n*pos[2]), axis)
                    link = field[key] if lines is not None else field.get(key, one)
                    q = mul(q, link if sign==1 else link*[1,-1,-1,-1])
                    if sign > 0:
                        pos[axis] = (pos[axis]+1) % n
            out.append(np.arccos(np.clip(-q[0], -1., 1.)))
    assert len(out)==3*(n//2)**3
    return np.array(out)


def stats(streams):
    sums = sum(streams)
    means = sums[1:] / sums[0]
    v1,v4 = means[2:4] - means[:2]**2
    j1,j4 = means[4:6]
    return np.array([v1,v4,j1,j4,j1/v1,j4/v4])


def jack(streams):
    n = len(streams)
    drop = np.array([stats(streams[:i]+streams[i+1:]) for i in range(n)])
    return stats(streams), np.sqrt((n-1)*np.var(drop,axis=0))


def reduce_side(n, files):
    def data(path):
        return np.loadtxt(io.BytesIO(files[path]), skiprows=1, delimiter=",", ndmin=2)
    def summarise(matrix, columns):
        x,y,a,b = matrix[:,columns].T
        return np.array([len(x), x.sum(), y.sum(), x@x, y@y, a.sum(), b.sum()])

    series = defaultdict(dict)
    clearance = {}
    for path in sorted(files):
        match = (re.fullmatch(r"results/(L-d[\d.]+|clear[024])/s(\d+)\.csv",path) if n==6 else
                 re.fullmatch(r"results/(?:mix|clear/runs)/([dk][^-]+-[^-]+(?:-cfg\d+)?)-s(\d+)-(?:hot|cold)\.csv",path))
        if not match:
            continue
        tag, index = match.group(1), int(match.group(2))
        raw = data(path)
        if n==6:
            command = files[path[:-4]+".meta.txt"].decode().splitlines()[0].split()
        else:
            label = "hot" if index%2 else "cold"
            assert path.endswith("-"+label+".csv")
            command = json.loads(files[path[:-4]+".meta"].splitlines()[1])["cmd"].split()
        assert int(command[4])==index%2 and int(command[6])==len(raw)
        # Put literal raw holonomy first on both hosts.
        cols = ([0,1,3,4],[5,6,7,8]) if n==6 else ([5,6,7,8],[0,1,3,4])
        series[tag][index] = [summarise(raw,c) for c in cols]
        if n==6:
            col = data(path[:-4]+".colours.csv")
        else:
            col = raw[:,9:57]
        assert np.all(col>=0)
        for start in range(0,col.shape[1],24):
            supported = 3 if start%48==0 else 4
            block = col[:,start:start+24]
            assert np.all(block[:,supported:]==0) and np.all(block[:,:supported].sum(axis=0)>0)
            target = ([3,4,7,8][start//24] if n==6 else [3,4][start//24])
            # Six prints colours with seven significant digits, eight with twelve decimals.
            np.testing.assert_allclose(block.mean(axis=1), raw[:,target], atol=7e-13,
                                       rtol=5.1e-7 if n==6 else 0.)
        if index != 0:
            continue
        if n==6:
            meta = files[path[:-4]+".meta.txt"].decode().splitlines()
            saved = float(next(x for x in meta if x.startswith("min_angle")).split()[1])
            recorded = [float(z) for z in next(x for x in meta if x.startswith("coarse_angles")).split()[1:]]
            skel = files["results/gen/chain.skel"+tag[-1]+".txt"] if tag.startswith("clear") else None
            delta = 0 if skel else float(tag.split("d")[1])/BETA[n]
            loop_angles = angles(n,skel,delta)
            np.testing.assert_allclose(np.sort(recorded),np.sort(loop_angles),atol=2e-8,rtol=0)
        else:
            meta = json.loads(files[path[:-4]+".meta"].splitlines()[0])
            saved = meta["min_angle_from_minusI"]
            skel = files["results/clear/skeletons/"+tag.split("-",1)[1]+".skel"] if tag[0]=="k" else None
            delta = 0 if skel else float(tag.split("-c")[1])/BETA[n]
            loop_angles = angles(n,skel,delta)
            if skel:
                ref = files["results/clear/skeletons/"+tag.split("-",1)[1]+".angles"]
                np.testing.assert_allclose(loop_angles,np.loadtxt(io.BytesIO(ref))[:,-1],atol=2e-8,rtol=0)
        assert abs(min(loop_angles)-saved)<2e-8
        clearance[tag] = saved
    assert len(series)==(8 if n==6 else 7)
    for tag, grouped in sorted(series.items()):
        assert sorted(grouped)==list(range(len(grouped)))
        for ref in (0,1):
            streams = [grouped[k][ref] for k in sorted(grouped)]
            f,e = jack(streams)
            cold,ec = jack(streams[::2])
            hot,eh = jack(streams[1::2])
            z = (hot-cold) / np.hypot(eh,ec)
            zp = (hot-cold) / (2*e)
            print(n,tag,['raw','traceless'][ref],f"streams={len(streams)} rows={int(streams[0][0])} angle={clearance[tag]:.6f}",
                  f"J4={f[3]:.7f} V4={f[1]:.7f} r4={f[5]:.6f}({e[5]:.6f})",
                  f"r1={f[4]:.6f}({e[4]:.6f}) zV4={z[1]:.2f} zr4={z[5]:.2f} pooled-zr1={zp[4]:.2f} pooled-zr4={zp[5]:.2f}")
    pattern = r"results/ctl_g4seeds/minus6-s\d+.csv" if n==6 else r"results/control/g4bin-minus8-s\d+.csv"
    controls = [summarise(data(path),[0,1,3,4]) for path in sorted(files) if re.fullmatch(pattern,path)]
    assert len(controls)==4
    f,e = jack(controls)
    print(n,"short control",f[5],e[5])


if __name__=="__main__":
    if len(sys.argv) not in (1,3):
        raise SystemExit("Give both local results.tgz paths, or fetch the pinned commit and run without arguments.")
    for i,n in enumerate((6,8)):
        reduce_side(n,archived(n,sys.argv[i+1] if len(sys.argv)>1 else None))
