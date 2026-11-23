"""Sum finite time windows by evolving the set of faces already visited."""
from math import isclose

def cuts(mask):
    bits = [(mask >> i) & 1 for i in range(6)]
    return sum(bits[i] != bits[j] for i in range(6) for j in range(i)
               if i//2 != j//2)

def normalized_sum(q, sink, lag, halo):
    time_slices = range(-halo,lag+halo+1)
    weights = {0:1.0}
    inner = 63 ^ (1 | (1<<sink))
    for t in time_slices:
        next_weights = {}
        forced = (1 if t==0 else 0) | (1<<sink if t==lag else 0)
        for old,weight in weights.items():
            available = inner & ~old
            take=available
            while True:
                new=old|take|forced
                next_weights[new]=next_weights.get(new,0.0)+weight
                if not take: break
                take=(take-1) & available
        weights={s:w*q**(cuts(s)-(4 if 0<=t<lag else 0))
                 for s,w in next_weights.items()}
    return weights[63]

def slope(q,lag):
    def calc(M):
        return -(2*normalized_sum(q,1,M,lag)+8*normalized_sum(q,2,M,lag))/256
    return calc(lag+1)-calc(lag)

if __name__=="__main__":
    for q in (0.25,0.5,0.75,0.875):
        x=q*q
        target=-sum(a*x**i for i,a in enumerate([5,44,143,200,143,44,5]))/(128*(1-x*x)**3)
        measured=slope(q,160)
        print(q,measured,target)
        assert isclose(measured,target,rel_tol=2e-10)
