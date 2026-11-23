import numpy as np, math
def ser(nu,x=1.0):
    return sum((x/2)**(2*k+nu)/(math.factorial(k)*math.factorial(k+nu)) for k in range(30))
ctrl=ser(1)/ser(0)
with open("control.txt","x") as f: f.write("I1(1)/I0(1) = %.6f\n"%ctrl)
def Rz(a): 
    a=np.asarray(a,float); z=np.zeros(a.shape,complex)
    M=np.zeros(a.shape+(2,2),complex); M[...,0,0]=np.exp(-1j*a/2); M[...,1,1]=np.exp(1j*a/2); return M
def Ry(b):
    b=np.asarray(b,float); M=np.zeros(b.shape+(2,2),complex)
    M[...,0,0]=np.cos(b/2);M[...,0,1]=-np.sin(b/2);M[...,1,0]=np.sin(b/2);M[...,1,1]=np.cos(b/2);return M
def inv(U): return np.conj(np.swapaxes(U,-1,-2))
def run(n):
    # U1=Rz(phi) class rep, Weyl density sin^2(phi/2)/(2pi) on [0,4pi) trapezoid
    ph=np.arange(n)*4*np.pi/n; w1=np.sin(ph/2)**2/(2*np.pi)*(4*np.pi/n)
    x,wx=np.polynomial.legendre.leggauss(n); be=np.arccos(x); wb=wx/2
    ga=np.arange(n)*4*np.pi/n; wg=np.full(n,1.0/n)
    P,Bb,G=np.meshgrid(ph,be,ga,indexing='ij')
    W=w1[:,None,None]*wb[None,:,None]*wg[None,None,:]
    U1=Rz(P); U2=Rz(0*Bb)@Ry(Bb)@Rz(G)   # alpha fixed =0 by residual z-conjugation
    M=U1@U2@inv(U1)@inv(U2)
    c=0.5*np.real(M[...,0,0]+M[...,1,1])
    chi=lambda U:(np.real(U[...,0,0]+U[...,1,1]))**2-1
    A=np.sum(W*chi(U1)*chi(U2)*c); B=np.sum(W*np.exp(-4*(1-c)))
    C=np.sum(W*chi(U1)**2); D=np.sum(W*chi(U2)**2); Z=W.sum()
    return A,B,C,D,Z
out=[]
for n in (24,40,64):
    r=run(n); out.append("n=%d A=%.12f B=%.12f int chi^2(U1)=%.12f int chi^2(U2)=%.12f mass=%.12f"%((n,)+r)); print(out[-1])
open("result.txt","x").write("\n".join(out)+"\n")
