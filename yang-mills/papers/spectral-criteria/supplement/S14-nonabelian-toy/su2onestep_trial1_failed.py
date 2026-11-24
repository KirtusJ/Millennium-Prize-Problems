"""SU(2) ladder toy: calibration of the one-step criterion (Proposition "A one-step criterion", B = 0) in the model
of su2run.py truncated at spin J, done exactly by dense diagonalisation in each of the four sectors of the two
centre flips (y-flip: (-1)^(2 j_c + 2 j_d); x-flip: (-1)^(2 j_a)), which the transfer operator and the coarse
space both respect. H = -log(T / top eigenvalue) on the centred functions (mesh 1). P = projection on the coarse
space generated to degree D = 10 as in su2run.py, without the vacuum; Q = I - P on the centred functions.
Per sector and for the whole centred space:
  Delta = gap;  kappa = ||Q H^-1 Q|| (best constant in Q <= kappa H);  gamma = 1 / ||Q (I - That^2)^-1 Q||;
  b(t) = 1 - ||P exp(-tH) P||;  bound(t) = b(t) / (1 + kappa / t);  true(t) = 1 - exp(-t Delta).
PREDICATES (fixed before the first run).
 Controls (theorems; a failure is an error of the program):
  S1 bound(t) <= true(t) + 1e-10 for every sector, the whole space, every beta and t.
  S2 2 (1/gamma - 1) - 1e-9 <= kappa <= 2 (1/gamma - 1/2) + 1e-9 in every case.
  S3 at J = 5 the sector gaps reproduce the energies of su2cluster_result.txt for the lowest state of the sectors
     (y-odd, x-even), (y-even, x-odd), (y-even, x-even) at beta = 3, 4, 5 to 2e-6 absolute (printed there to 6
     decimals). Tested only when J = 5 is run.
  S4 every column of the coarse basis lies in one sector (its norm restricted to each sector is 0 or 1 to 1e-8).
 Expectations (stipulated, either outcome is kept):
  X1 for beta in {2, 3, 4, 5} and every sector: bound(16)/true(16) >= 0.8 and bound(1)/true(1) >= 0.3.
  X2 in the sector even under both flips, kappa <= 1.5 for beta in {2, 3, 4, 5}; and kappa of that sector changes by
     less than 10 per cent between beta = 3 and beta = 5.
Usage: python3 su2onestep.py OUT J[,J...] [CLUSTER_RESULT]"""
import sys, re, time, numpy as np
from su2ladder import *
TS=(1,2,4,8,16,64,256); D=10
out=[]; S1=S2=S4=True; S3=None; X1=X2=True; x2={}
ref={}
if len(sys.argv)>3:
    cur=None
    for line in open(sys.argv[3]):
        mm=re.match(r"beta ([\d.]+):",line)
        if mm: cur=float(mm.group(1))
        mm=re.match(r"\s+state \d: energy ([\d.]+)\s+y-parity ([+-])\S+\s+x-parity ([+-])",line)
        if mm and cur is not None:
            key=(cur,mm.group(2)+mm.group(3)); ref.setdefault(key,float(mm.group(1)))
for J in [float(x) for x in sys.argv[2].split(',')]:
    t0=time.time(); N=Net(J); mats={k:N.assemble(k) for k in ('W0','W1','C','AB','ABC')}
    py=np.zeros(N.n,dtype=int); px=np.zeros(N.n,dtype=int)
    for (ja,jb,jc,jd),(off,r0,r1) in N.blocks.items():
        py[off:off+r0*r1]=(-1)**(tw(jc)+tw(jd)); px[off:off+r0*r1]=(-1)**tw(ja)
    sectors={sy+sx:np.where((py==(1 if sy=='+' else -1))&(px==(1 if sx=='+' else -1)))[0] for sy in '+-' for sx in '+-'}
    out.append("J = %.0f: %d states; sector sizes (y x): %s"%(J,N.n," ".join("%s %d"%(k,len(v)) for k,v in sectors.items()))); print(out[-1],flush=True)
    for beta in (1.0,2.0,3.0,4.0,5.0):
        m=Model(J,beta,Dg=0,net=N,mats=mats); assert m.real
        eig={}
        for key,I in sectors.items():
            A=m.A[I][:,I].toarray(); assert abs(A-A.T).max()<1e-12
            w,U=np.linalg.eigh(A); M=(U*np.exp(w))@U.T; del A,U
            T=(M*m.K[I])@M.T; del M; T=(T+T.T)/2
            ev,V=np.linalg.eigh(T); del T; eig[key]=(ev[::-1].copy(),V[:,::-1].copy()); del V
        L0=eig['++'][0][0]; Om=np.zeros(N.n); Om[sectors['++']]=eig['++'][1][:,0]
        m.Om=Om; m.L0=L0; m.coarse(D); Q=m.Q
        rows=[]; whole={'kappa':0,'gamma':9,'Delta':9,'b':{t:9 for t in TS}}
        for key,I in sectors.items():
            ev,V=eig[key]; Qs=Q[I,:]; nr=np.linalg.norm(Qs,axis=0)
            S4&=bool(np.all((nr<1e-8)|(abs(nr-1)<1e-8)))
            cols=np.where(nr>0.5)[0]; cols=cols[cols!=0]      # column 0 is the vacuum
            if key=='++': ev=ev[1:]; V=V[:,1:]
            lam=ev/L0; E=-np.log(lam); Qt=V.T@Qs[:,cols]
            def top(d):
                S=-(Qt*d[:,None])@(Qt*d[:,None]).T; S[np.diag_indices_from(S)]+=d*d
                return np.linalg.eigvalsh(S)[-1]
            kappa=top(E**-0.5); gamma=1/top((1-lam**2)**-0.5); Delta=E[0]
            ok2=(2*(1/gamma-1)-1e-9<=kappa<=2*(1/gamma-0.5)+1e-9); S2&=ok2
            line="  J=%.0f beta %.0f sector %s: dim %d coarse %d  Delta %.6f  kappa %.4f  gamma %.4f%s"%(J,beta,key,len(I),len(cols),Delta,kappa,gamma,"" if ok2 else " S2-FAILED")
            whole['kappa']=max(whole['kappa'],kappa); whole['gamma']=min(whole['gamma'],gamma); whole['Delta']=min(whole['Delta'],Delta)
            parts=[]
            for t in TS:
                b=1-np.linalg.eigvalsh((Qt*np.exp(-t*E)[:,None]).T@Qt)[-1]; whole['b'][t]=min(whole['b'][t],b)
                bd=b/(1+kappa/t); tr=1-np.exp(-t*Delta); ok1=bd<=tr+1e-10; S1&=ok1
                if beta>=2 and ((t==16 and bd/tr<0.8) or (t==1 and bd/tr<0.3)): X1=False
                parts.append("t=%d b %.5f bound %.5f true %.5f ratio %.3f%s"%(t,b,bd,tr,bd/tr,"" if ok1 else " S1-FAILED"))
            out.append(line); out.append("      "+" | ".join(parts)); print(line,flush=True)
            if key=='++':
                rows.append((beta,kappa))
                if beta>=2 and kappa>1.5: X2=False
                x2.setdefault(J,{})[beta]=kappa
            if J==5 and ref and beta in (3.0,4.0,5.0) and key in ('-+','+-','++'):
                if (beta,key) in ref:
                    d=abs(Delta-ref[(beta,key)]); S3=(S3 is None or S3) and d<2e-6
                    out.append("      S3: cluster file %.6f, here %.6f, difference %.1e"%(ref[(beta,key)],Delta,d))
        kappa=whole['kappa']; Delta=whole['Delta']; ok2=(2*(1/whole['gamma']-1)-1e-9<=kappa<=2*(1/whole['gamma']-0.5)+1e-9); S2&=ok2
        parts=[]
        for t in TS:
            b=whole['b'][t]; bd=b/(1+kappa/t); tr=1-np.exp(-t*Delta); ok1=bd<=tr+1e-10; S1&=ok1
            parts.append("t=%d b %.5f bound %.5f true %.5f ratio %.3f"%(t,b,bd,tr,bd/tr))
        out.append("  J=%.0f beta %.0f WHOLE centred space: Delta %.6f  kappa %.4f  gamma %.4f"%(J,beta,Delta,kappa,whole['gamma'])); out.append("      "+" | ".join(parts)); print(out[-2],'(%.0fs)'%(time.time()-t0),flush=True)
for J,d in x2.items():
    r=abs(d[5.0]/d[3.0]-1); out.append("X2 detail J=%.0f: kappa(++) at beta 3, 5: %.4f %.4f, relative change %.3f"%(J,d[3.0],d[5.0],r))
    if r>=0.10: X2=False
for nm,v in (("S1",S1),("S2",S2),("S3",S3),("S4",S4)): out.append("%s %s"%(nm,"NOT TESTED" if v is None else "MET" if v else "FAILED"))
for nm,v in (("X1",X1),("X2",X2)): out.append("%s %s"%(nm,"as expected" if v else "NOT as expected"))
open(sys.argv[1],'x').write("\n".join(out)+"\n"); print("\n".join(out[-6:]))
