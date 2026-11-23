import numpy as np, itertools
np.random.seed(0)
x0=(1,1,1,1)
def sh(x,m,d=1):
    y=list(x); y[m]+=d; return tuple(y)
free=[(sh(x0,m,-1),m) for m in range(4)]+[(x0,m) for m in range(4)]
pl=[]
for x in itertools.product([0,1],repeat=4):
    for m in range(4):
        for n in range(m+1,4):
            pl.append((x,m,n))
def links(p):
    x,m,n=p
    return [(x,m),(sh(x,m),n),(sh(x,n),m),(x,n)]
con=[p for p in pl if any(l in free for l in links(p))]
def S(U):
    g=lambda l:U.get(l,np.eye(2))
    s=0
    for x,m,n in con:
        P=g((x,m))@g((sh(x,m),n))@g((sh(x,n),m)).T@g((x,n)).T
        s+=1-np.trace(P)/2
    return s
def rot(t): return np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
F=np.diag([1.,-1.])
def gauge(h):
    U={}
    for m in range(4): U[free[m]]=h.T; U[free[4+m]]=h
    return U
out=[]
out.append(f"total plaquettes containing a free link: {len(con)}")
out.append(f"S identity: {S({})}")
for l in free: out.append(f"plaquettes containing link {l}: {sum(l in links(p) for p in con)}")
out.append(f"S gauge h=diag(1,-1): {S(gauge(F))}")
out.append(f"S gauge h=R(0.7)*F: {S(gauge(rot(0.7)@F))}")
out.append(f"S only incoming mu=0 = F: {S({free[0]:F})}")
out.append(f"S only outgoing mu=0 = F: {S({free[4]:F})}")
t="\n".join(out); print(t)
with open("results.txt","x") as f: f.write(t+"\n")
with open("notes.md","a") as f: f.write("## run\ncontrol O(2) components=2\n"+t+"\nrerun: cd /home/user/z4-workers/e2-chalBgen/child/grandchild && python3 gc.py (results.txt opened with x; delete/rename to rerun)\n")
