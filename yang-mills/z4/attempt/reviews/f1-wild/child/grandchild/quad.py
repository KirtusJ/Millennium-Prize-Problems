import numpy as np, math
def I(n,x,N):
    # composite Simpson on [0,pi], N even
    s=np.linspace(0,math.pi,N+1); f=np.exp(x*np.cos(s))*np.cos(n*s)
    h=math.pi/N
    return (h/3*(f[0]+f[-1]+4*f[1:-1:2].sum()+2*f[2:-1:2].sum()))/math.pi
def L(n,x,N): return -math.log(I(n,x,N)/I(0,x,N))
if __name__=="__main__":
    import os
    out=[]
    c0=I(0,0,200); c1=L(1,4,200); c1b=L(1,4,400)
    ok0=abs(c0-1)<1e-12; ok1=f"{c1:.6f}"=="0.146735"
    out.append(f"CONTROL I_0(0) = {c0!r} -> {'PASS' if ok0 else 'FAIL'}")
    out.append(f"CONTROL -ln(I1(4)/I0(4)) = {c1:.8f} (N=200), {c1b:.8f} (N=400); target 0.146735 -> {'PASS' if ok1 else 'FAIL'}")
    if ok0 and ok1:
        for n in (1,2):
            v=[L(n,8,N) for N in (200,400,800)]
            out.append(f"-ln(I{n}(8)/I0(8)): N=200 {v[0]:.10f}; N=400 {v[1]:.10f}; N=800 {v[2]:.10f}; diff(400,800)={abs(v[1]-v[2]):.2e}; value {v[2]:.8f}")
    with open("result.md","x") as f: f.write("\n".join(out)+"\n")
    print("\n".join(out))
