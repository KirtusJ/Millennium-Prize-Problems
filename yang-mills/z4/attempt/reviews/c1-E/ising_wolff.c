/*
 ising_wolff.c  --  worker c1-E (task T6). Wolff single-cluster Monte Carlo for the
 nearest-neighbour Ising model on the periodic d-dimensional torus L^d, H = -K sum s_i s_j.

 Usage: ising_wolff d L K ntherm nmeas seed outfile
   ntherm, nmeas are counted in "sweeps" (clusters flipped until ~V spins were flipped).
 Output (outfile opened with fopen mode "wx": never overwritten) one line:
   d L K nmeas <M2> err <M4> err U4 err xi2/L err gR err  nbins
 with M = sum_i s_i, U4 = 1 - <M^4>/(3<M^2>^2),
   F = (1/d) sum_mu <|sum_x s_x exp(i 2pi x_mu/L)|^2>,
   xi2 = sqrt(<M^2>/F - 1) / (2 sin(pi/L))     (second-moment correlation length),
   gR  = -(<M^4> - 3<M^2>^2)/<M^2>^2 * (L/xi2)^d = 3 U4 (L/xi2)^d
 (the standard renormalized four-point coupling g = -u4/(chi^2 xi^d), u4 = (<M^4>-3<M^2>^2)/V,
  chi = <M^2>/V). Errors: jackknife over nbins = 20 consecutive bins.

 PREDICATES (fixed before the first run; evaluated by analyse.py, not here):
  P2a (4D Ising, known answer: marginal triviality, g_R -> 0 like 1/log xi at fixed L/xi):
       at the common value xi2/L = 0.25, interpolated linearly in K between grid points,
       g_R(L) for L = 6, 8, 12 is non-increasing within 2 sigma (each step).
  P2a' (ADDED after the unrecorded pilot in pilot/, before any recorded run: at xi/L = 0.25
       U4 ~ 0.0-0.1 and g = 3 U4 (L/xi)^4 amplifies the noise by 256; P2a is KEPT as written)
       same statement at xi2/L = 0.5 for L = 6, 8, 12, 16.
  P2c  (added with P2a') g_R(16, 0.5) < g_R(6, 0.5) by more than 2 sigma (a decrease is visible).
  P2b  g_R(L=12, xi/L=0.25) > 0 by more than 5 sigma (finite size: the decrease is only
       logarithmic, so at accessible sizes the coupling is still clearly nonzero).
  P3  (2D Ising at K_c = 0.5 ln(1+sqrt 2), periodic square torus) U4(L) within 0.02 of
       0.6107 for L = 16, 32, 64 (tolerance: Salas-Sokal value 0.61069; 0.02 covers
       corrections ~ L^{-7/4} log L at L = 16 plus 3 sigma statistics; from memory, see report).
  Seeds fixed by the caller.
 v2 (after defect found in v1, see notes.md step 7): during thermalisation sweeps end when >= V spins
  were flipped; afterwards the number of clusters per sweep is FIXED to max(1, round(V/<|C|>_therm)),
  so measurement times do not depend on the configuration. Added self-check P0 (Wolff improved
  estimator identity, exact in equilibrium): |<M^2>/V - <|C|>| < 4 sigma(M^2)/V + 1%; printed as P0=0/1.
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <string.h>

static uint64_t s[4];
static inline uint64_t rotl(const uint64_t x, int k){ return (x<<k)|(x>>(64-k)); }
static uint64_t next(void){ const uint64_t r=rotl(s[1]*5,7)*9; const uint64_t t=s[1]<<17;
  s[2]^=s[0]; s[3]^=s[1]; s[1]^=s[2]; s[0]^=s[3]; s[2]^=t; s[3]=rotl(s[3],45); return r; }
static inline double urand(void){ return (next()>>11)*0x1.0p-53; }
static uint64_t splitmix(uint64_t *x){ uint64_t z=(*x+=0x9e3779b97f4a7c15ULL);
  z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL; z=(z^(z>>27))*0x94d049bb133111ebULL; return z^(z>>31);}

int main(int argc, char **argv){
  if(argc!=8){ fprintf(stderr,"usage: d L K ntherm nmeas seed outfile\n"); return 2; }
  int d=atoi(argv[1]), L=atoi(argv[2]); double K=atof(argv[3]);
  long ntherm=atol(argv[4]), nmeas=atol(argv[5]); uint64_t seed=strtoull(argv[6],0,10);
  FILE *out=fopen(argv[7],"wx"); if(!out){ fprintf(stderr,"refusing: %s exists or cannot be created\n",argv[7]); return 3; }
  uint64_t sm=seed; for(int i=0;i<4;i++) s[i]=splitmix(&sm);
  long V=1; for(int i=0;i<d;i++) V*=L;
  int8_t *sp=malloc(V); int *stack=malloc(sizeof(int)*V); long *stride=malloc(sizeof(long)*d);
  stride[0]=1; for(int i=1;i<d;i++) stride[i]=stride[i-1]*L;
  for(long i=0;i<V;i++) sp[i]= (urand()<0.5)?1:-1;
  double p=1.0-exp(-2.0*K);
  double *cosk=malloc(sizeof(double)*L), *sink=malloc(sizeof(double)*L);
  for(int x=0;x<L;x++){ cosk[x]=cos(2*M_PI*x/L); sink[x]=sin(2*M_PI*x/L); }
  double avgc=1.0; long tot=0, ncl=0, nfix=1;
  double *m2=malloc(sizeof(double)*nmeas), *m4=malloc(sizeof(double)*nmeas), *ff=malloc(sizeof(double)*nmeas);
  for(long sweep=0; sweep<ntherm+nmeas; sweep++){
    long flipped=0; long ncs=0;
    if(sweep==ntherm){ nfix=(long)floor(V*(double)ncl/(double)tot+0.5); if(nfix<1) nfix=1; tot=0; ncl=0; }
    while( (sweep<ntherm) ? (flipped<V) : (ncs<nfix) ){ ncs++;
      long site=(long)(urand()*V); int8_t s0=sp[site]; sp[site]=-s0; int top=0; stack[top++]=site; long cs=1;
      while(top){ long x=stack[--top];
        for(int mu=0;mu<d;mu++){ long c=(x/stride[mu])%L;
          long xp = (c==L-1)? x-(L-1)*stride[mu] : x+stride[mu];
          long xm = (c==0)? x+(L-1)*stride[mu] : x-stride[mu];
          if(sp[xp]==s0 && urand()<p){ sp[xp]=-s0; stack[top++]=xp; cs++; }
          if(sp[xm]==s0 && urand()<p){ sp[xm]=-s0; stack[top++]=xm; cs++; }
        }
      }
      flipped+=cs; tot+=cs; ncl++;
    }
    if(sweep>=ntherm){ long k=sweep-ntherm; double M=0; double re[8]={0},im[8]={0};
      for(long x=0;x<V;x++){ M+=sp[x]; for(int mu=0;mu<d;mu++){ int c=(x/stride[mu])%L; re[mu]+=sp[x]*cosk[c]; im[mu]+=sp[x]*sink[c]; } }
      double F=0; for(int mu=0;mu<d;mu++) F+=re[mu]*re[mu]+im[mu]*im[mu]; F/=d;
      m2[k]=M*M; m4[k]=M*M*M*M; ff[k]=F; }
  }
  (void)avgc;
  int nb=20; long bs=nmeas/nb; double A[3][20]; double S[3]={0,0,0};
  for(int b=0;b<nb;b++){ A[0][b]=A[1][b]=A[2][b]=0; for(long i=b*bs;i<(b+1)*bs;i++){ A[0][b]+=m2[i];A[1][b]+=m4[i];A[2][b]+=ff[i]; }
    for(int j=0;j<3;j++){ S[j]+=A[j][b]; } }
  double fullv[5], jk[5][20];
  for(int b=-1;b<nb;b++){ double a2,a4,af; double n=(b<0)? nb*bs : (nb-1)*bs;
    a2=(S[0]-(b>=0?A[0][b]:0))/n; a4=(S[1]-(b>=0?A[1][b]:0))/n; af=(S[2]-(b>=0?A[2][b]:0))/n;
    double U=1-a4/(3*a2*a2); double xi=sqrt(a2/af-1)/(2*sin(M_PI/L)); double g=3*U*pow(L/xi,d);
    double v[5]={a2,a4,U,xi/L,g}; for(int j=0;j<5;j++){ if(b<0) fullv[j]=v[j]; else jk[j][b]=v[j]; } }
  double err[5]; for(int j=0;j<5;j++){ double mb=0; for(int b=0;b<nb;b++) mb+=jk[j][b]; mb/=nb; double e=0;
    for(int b=0;b<nb;b++) e+=(jk[j][b]-mb)*(jk[j][b]-mb); err[j]=sqrt((nb-1.0)/nb*e); }
  double mc=(double)tot/ncl; int P0 = fabs(fullv[0]/V - mc) < 4*err[0]/V + 0.01*mc;
  fprintf(out,"%d %d %.8f %ld %.10g %.3g %.10g %.3g %.6f %.6f %.6f %.6f %.6f %.6f %d meanclus %.2f nfix %ld P0 %d\n",d,L,K,nmeas,
     fullv[0],err[0],fullv[1],err[1],fullv[2],err[2],fullv[3],err[3],fullv[4],err[4],nb,mc,nfix,P0);
  fclose(out); return 0;
}
