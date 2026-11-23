"""Relative dual plaquettes of an absolute four-dimensional cubical box."""
from itertools import combinations, product
from pathlib import Path
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scalar-response'))
import numpy as np
from response import box, cube_sources, evaluate_words, parity


def shift(x,axis,step):
    return tuple(v+step*(i==axis) for i,v in enumerate(x))


def dual_face(face):
    x,a,b = face
    dirs = [i for i in range(4) if i not in (a,b)]
    y = shift(shift(x,a,1),b,1)
    return (y,*dirs),parity((a,b,*dirs))


def relative_box(lengths,reverse=False):
    sizes = tuple(n+1 for n in lengths)
    points = list(product(*(range(n+1) for n in sizes)))
    def relative(x,axes):
        return all(v<sizes[i] if i in axes else 0<v<sizes[i] for i,v in enumerate(x))
    tree_dir = 3 if reverse else 0
    tree = {(shift(x,tree_dir,-1),tree_dir) for x in points if relative(x,())}
    chords = {}
    for x in points:
        for a in range(4):
            if relative(x,(a,)) and (x,a) not in tree:
                chords[x,a] = len(chords)
    faces,words = [],[]
    for x in points:
        for a,b in combinations(range(4),2):
            if not relative(x,(a,b)):
                continue
            faces.append((x,a,b))
            path = [(x,a,1),(shift(x,a,1),b,1),(shift(x,b,1),a,-1),(x,b,-1)]
            words.append([(chords[y,d],sign) for y,d,sign in path if (y,d) in chords])
    B = np.zeros((len(faces),len(chords)),dtype=int)
    for p,word in enumerate(words):
        for e,sign in word:
            B[p,e] += sign
    return faces,words,B


def face_map(primal,dual):
    index = {face:i for i,face in enumerate(dual)}
    transformed = [dual_face(p) for p in primal]
    indices = np.array([index[q] for q,sign in transformed])
    signs = np.array([sign for q,sign in transformed])
    assert sorted(indices)==list(range(len(dual)))
    return indices,signs


def star_sources(faces,origins):
    # A dual vertex corresponding to a primal four-cube begins one index later.
    vertices = [tuple(v+1 for v in pt) for pt in origins]
    return np.array([[int(all(z<=y<=z+int(i in (a,b))
                            for i,(z,y) in enumerate(zip(x,v))))
                      for x,a,b in faces] for v in vertices],dtype=int)


def experiment(shape,origins,reverse=False):
    primal = box(shape,reverse)
    dual = relative_box(shape,reverse)
    indices,signs = face_map(primal[0],dual[0])
    B,G = primal[2],dual[2]
    assert len(B)==B.shape[1]+G.shape[1]
    assert not np.any(B.T @ (signs[:,None]*G[indices]))
    f = cube_sources(primal[0],origins)
    h = star_sources(dual[0],origins)
    assert np.array_equal(h[:,indices],f)
    assert np.all(f.sum(axis=1)==24) and np.max(f.sum(axis=0))==1
    return evaluate_words(*primal,f),evaluate_words(*dual,h)
