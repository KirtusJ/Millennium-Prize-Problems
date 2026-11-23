"""Matched periodic ensembles: fixed threshold at opposite slices, chain-wise blocks."""
from pathlib import Path
import numpy as np

DATA = Path(__file__).resolve().parents[3] / "z4/reviews/ext-match/predeclared"


def read(side, threshold, block):
    blocks = []
    for p in sorted(DATA.glob(f"meas_L{side}_*.txt")):
        x = np.loadtxt(p)[10:, 2+2*side:2+3*side]
        x = x[:len(x)//block*block]
        b = (x > threshold).astype(float)
        pair = b*np.roll(b, side//2, axis=1)
        lag = x*np.roll(x, 2, axis=1)
        rows = np.column_stack([b.mean(1),pair.mean(1),x.mean(1),lag.mean(1)])
        blocks.extend(rows.reshape(-1,block,4).mean(1))
    return np.array(blocks)


def quantities(row):
    b,p11,mean,lag = row
    off = b-p11
    signed = np.sqrt((1-2*b+p11)*p11)-off
    return np.array([signed,(lag-mean**2)/18])


def controls():
    rng = np.random.default_rng(41)
    for n in (2, 3, 7):
        for _ in range(80):
            e = np.r_[0., np.sort(rng.uniform(.01, 3., n-1))]
            raw = rng.normal(size=(n,n))
            obs = (raw+raw.T)/2
            width = np.ptp(np.linalg.eigvalsh(obs))
            a = obs - obs[0,0]*np.eye(n)
            prob = np.exp(-4*e)
            prob /= prob.sum()
            purity = prob @ prob
            def remainder(t):
                left = np.exp(-(4-t)*e[1:])
                right = np.exp(-t*e[1:])
                return prob[0]*(left @ (a[1:,1:]**2) @ right) - (prob @ a.diagonal())**2
            b0,b1,b2 = map(remainder,(0,1,2))
            assert -1.e-11 <= b2 <= b1+1.e-11 and b1 <= b0+1.e-11
            assert b0 <= width**2*min(.25,(1-purity)/2)+1.e-11
    # Positive symmetric half-kernel with a strict loss on binning.
    k = np.array([[4,1,1],[1,3,1],[1,1,2]], dtype=float)
    joint = k*k/np.sum(k*k)
    true_purity = np.trace(np.linalg.matrix_power(k,4))/np.sum(k*k)**2
    grouped = np.array([[joint[0,0],joint[0,1:].sum()],
                        [joint[1:,0].sum(),joint[1:,1:].sum()]])
    assert true_purity < 1-2*np.linalg.det(np.sqrt(grouped))**2 < 1


if __name__ == "__main__":
    controls()
    for side,threshold,base in [(6,.09,11),(8,.027,17),(12,.0057,25)]:
        for block in (base,base*2):
            blocks = read(side, threshold, block)
            n = len(blocks)
            total = blocks.sum(0)
            point = quantities(total/n)
            replicas = np.array([quantities((total-b)/(n-1)) for b in blocks])
            error = np.sqrt(n-1)*replicas.std(0)
            print(side,block,n,*point,*error,2*point[0]**2)
