"""Finite interacting surface expansion, spatial packing, Gaussian and block checks."""
from itertools import combinations, product
import math
import numpy as np


def z2_surface():
    # Periodic cubic complex. Distinct oriented positive faces survive on sides of length two.
    shape=(4,2,2)
    sites=list(np.ndindex(shape))
    v=len(sites)
    def fid(x,d):
        return 3*int(np.ravel_multi_index(x,shape))+d
    cubes=[]
    for x in sites:
        mask=0
        for d in range(3):
            y=list(x)
            y[d]=(y[d]+1)%shape[d]
            mask|=(1<<fid(x,d))|(1<<fid(tuple(y),d))
        cubes.append(mask)
    # Cube boundaries have one relation; three noncontractible sheets complete H_2.
    basis=cubes[:-1]+[sum(1<<fid(x,d) for x in sites if x[d]==0) for d in range(3)]
    surfaces=np.array([0],dtype=np.uint64)
    for b in basis:
        surfaces=np.concatenate((surfaces,surfaces^np.uint64(b)))
    assert np.unique(surfaces).size==2**(v+2)
    beta=np.array([.31,.46,.53])
    t=np.tanh(beta)
    z=0.
    first=np.zeros((3,v))
    second=np.zeros((3,v,v))
    for chunk in np.array_split(surfaces,64):
        bits=((chunk[:,None]>>np.arange(3*v,dtype=np.uint64))&1).reshape(-1,v,3)
        weights=np.prod(t**bits.sum(axis=1),axis=1)
        z+=weights.sum()
        for d in range(3):
            # Inserting a face toggles its membership in a closed surface.
            factor=np.where(bits[:,:,d],1/t[d],t[d])
            first[d]+=weights@factor
            second[d]+=(factor.T*weights)@factor
    for d in range(3):
        cov=second[d]/z
        np.fill_diagonal(cov,1)
        cov=beta[d]**2*(cov-np.outer(first[d]/z,first[d]/z))
        kernel=cov[0].reshape(shape)
        power=np.fft.fftn(kernel).real
        np.testing.assert_allclose(np.linalg.eigvalsh(cov),np.sort(power.ravel()),atol=1e-13)
        assert abs(power.max()-power[0,0,0])<1e-13
        for axis in range(3):
            c=np.fft.fftn(kernel,axes=tuple(j for j in range(3) if j!=axis))
            assert np.max(abs(c.imag))<1e-13
            seq=np.moveaxis(c.real,axis,0)
            assert seq.min()>-1e-13 and np.max(np.diff(seq[:shape[axis]//2+1],axis=0))<1e-13
            tv=np.sum(abs(seq-np.roll(seq,1,axis=0)),axis=0)
            assert np.all(tv<=2*seq[0]+1e-13)
        contrast=np.array([(-1)**sum(x) for x in sites])/np.sqrt(v)
        assert contrast@cov@contrast<=8*cov[0,0]+1e-13
        print("Z2 flux normal",d,"zero mode",round(power.max(),8))


def geometry():
    # Choose the backward or forward neighboring link adversarially. All potential
    # pair links remain on erased lines. No face can meet two different pairs.
    for n in (8,10,14,16,18,24,34):
        anchors=[x for i in range(n//8) for x in (8*i,8*i+4)]
        groups={}
        for x,y,z in product(anchors,repeat=3):
            for j in (-1,0,1):
                edge=((x+j)%n,(y+1)%n,z)
                assert edge not in groups and edge[1]%2==1
                groups[edge]=(x,y,z)
        for edge,owner in groups.items():
            for d in (1,2):
                nbr=list(edge)
                nbr[d]=(nbr[d]+1)%n
                assert groups.get(tuple(nbr),owner)==owner
        # In a straight segment of length >=2 an edge always has an internal
        # neighbor. Try both possible choices, including partitions crossing zero.
        for x,y,z in product(anchors,repeat=3):
            assert (x,y,z) not in groups
            assert groups[(x,y+1,z)]==(x,y,z)
        for x in anchors:
            for start in range(n):
                offset=(x-start)%n
                for length in range(max(2,offset+1),n+1):
                    other=offset-1 if offset>0 else offset+1
                    assert 0<=other<length
                    neighbor=(start+other)%n
                    assert neighbor in ((x-1)%n,(x+1)%n)
        assert {0,2}.isdisjoint({1,3})  # lag two has no common temporal action plaquette
        assert len(set(groups.values()))==8*(n//8)**3


def gaussian():
    for n in range(2,130,2):
        k=np.arange(n)
        nonpositive=(4*k>=n)&(4*k<=3*n)
        assert np.all(nonpositive | np.roll(nonpositive,n//2))
        good=nonpositive[:,None]|nonpositive[None,:]
        assert 4*good.sum()>=3*n*n
        if n==6:
            assert np.array_equal(np.flatnonzero(nonpositive),[2,3,4])
    for n in (2,4,8,16,32,64):
        s=4*np.sin(np.pi*np.arange(n)/n)**2
        x,y,z=np.meshgrid(s,s,s,indexing="ij")
        tot=x+y+z
        g=np.divide(x+y,np.sqrt(tot*(tot+4)),out=np.zeros_like(tot),where=tot>0)
        e=2*np.arcsinh(np.sqrt(tot)/2)
        c=1.5*np.fft.ifftn(g).real**2
        power=np.fft.fftn(c).real
        chi=1.5*np.mean(g*g)
        lag=1.5*np.mean((g*np.exp(-n*e))**2)
        assert np.max(abs(power.max()-chi))<1e-13 and power.min()>=1/64-1e-13
        if n==2:
            np.testing.assert_allclose(8*chi,3.5,atol=1e-13)
        print("Gaussian N, chi, N^5 physical-time covariance",n, f"{chi:.8f}",f"{lag*n**5:.8g}")


def sharp_blocks():
    for a,g in product((.01,.2,.5,.8,.99),(.01,.3,.8)):
        d=np.diag([1,math.sqrt(1-g)])
        w=np.sqrt([a,1-a])
        s=d@np.outer(w,w)@d
        np.testing.assert_allclose(np.linalg.eigvalsh(s)[-1],1-g*(1-a))
        np.testing.assert_allclose(s[0,1]**2,(1-g)*a*(1-a))
    pattern=np.array([1.,-1.,1.,-1.])
    assert np.sum(abs(pattern-np.roll(pattern,1)))>2*pattern[0]


if __name__=="__main__":
    z2_surface()
    geometry()
    gaussian()
    sharp_blocks()
