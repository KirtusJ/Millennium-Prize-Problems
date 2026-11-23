/* vortex.c -- Z2 LGT in D dims, periodic L^D. Heat bath. F = 2*beta*Int_0^1 <sum_stack sigma_P>_s ds
 * Stack: plaquettes in plane (0,1) with base x0=x1=0 (all other coords): L^(D-2) plaquettes.
 * (Task text says L^2 for D=4: same, L^(D-2)=L^2.)
 * Coupling on stack = beta*(1-2s), s=Gauss-Legendre nodes on [0,1] (n nodes given).
 * Two chains per node (hot start, cold start), 2000 therm sweeps, 20000 meas sweeps, 20 bins each.
 * PREDICATES (fixed before first run):
 *  C2: D=2,L=2,beta=0.5 (the control; stack=1 plaquette) gives F within 3 sigma of 0.091272 (exact).
 *  P1: hot/cold chains agree at every node: |m_hot-m_cold| < 3*sqrt(e_h^2+e_c^2); count qualifying nodes (hypothesis tested per case).
 *  P2: quadrature n=5 vs n=8 agree within 3*sqrt(e5^2+e8^2) (and tolerance from errors, no separate trusted exact).
 *  P3: F >= 0 within 3 sigma for each of the 6 cases (expectation, not theorem).
 *  P4: F(L,beta) non-increasing in L: F(L+1)-F(L) <= 1 sigma_diff, for each beta (measured; 2 beta values x 2 steps).
 * usage: vortex D L beta n seedbase outfile  (outfile opened "wx": never overwritten)
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
static int D,L,NS,NL,NP,NPL;
static int *nbp,*nbm; static int8_t *sp; static double *bp;
static int (*lk)[2*(8-1)][3]; static int (*lp)[2*(8-1)]; 
static uint64_t st;
static inline uint64_t rnd(void){uint64_t z=(st+=0x9E3779B97F4A7C15ULL);z=(z^(z>>30))*0xBF58476D1CE4E5B9ULL;z=(z^(z>>27))*0x94D049BB133111EBULL;return z^(z>>31);}
static inline double ur(void){return (rnd()>>11)*(1.0/9007199254740992.0);}
static int pa[32],pb[32];
static void plq(int base,int a,int b,int*o){o[0]=base*D+a;o[1]=nbp[base*D+a]*D+b;o[2]=nbp[base*D+b]*D+a;o[3]=base*D+b;}
static int planeid(int a,int b){for(int i=0;i<NPL;i++)if(pa[i]==a&&pb[i]==b)return i;return -1;}
static int nst; static int *stk;
static void setup(void){
  NS=1;for(int i=0;i<D;i++)NS*=L; NL=NS*D; NPL=D*(D-1)/2; NP=NS*NPL;
  int k=0;for(int a=0;a<D;a++)for(int b=a+1;b<D;b++){pa[k]=a;pb[k]=b;k++;}
  nbp=malloc(sizeof(int)*NL);nbm=malloc(sizeof(int)*NL);
  for(int x=0;x<NS;x++)for(int m=0;m<D;m++){int p=1;for(int i=0;i<m;i++)p*=L;int c=(x/p)%L;
    nbp[x*D+m]=x+(((c+1)%L)-c)*p; nbm[x*D+m]=x+(((c+L-1)%L)-c)*p;}
  sp=malloc(NL);bp=malloc(sizeof(double)*NP);
  lk=malloc(sizeof(int[2*7][3])*NL);lp=malloc(sizeof(int[2*7])*NL);
  for(int x=0;x<NS;x++)for(int m=0;m<D;m++){int l=x*D+m,c=0;
    for(int nu=0;nu<D;nu++){if(nu==m)continue;int a=m<nu?m:nu,b=m<nu?nu:m;int pid=planeid(a,b);
      int bases[2]={x,nbm[x*D+nu]};
      for(int j=0;j<2;j++){int o[4];plq(bases[j],a,b,o);int q=0,found=0;
        for(int t=0;t<4;t++){if(o[t]==l&&!found){found=1;continue;}lk[l][c][q++]=o[t];}
        if(q!=3||!found){fprintf(stderr,"setup bug\n");exit(2);}
        lp[l][c]=bases[j]*NPL+pid;c++;}}}
  nst=0;stk=malloc(sizeof(int)*NS);
  for(int x=0;x<NS;x++){int p=1;int c0=x%L,c1=(x/L)%L;if(c0==0&&c1==0)stk[nst++]=x*NPL+planeid(0,1);}
}
static void sweep(void){
  for(int l=0;l<NL;l++){double h=0;int n=2*(D-1);
    for(int c=0;c<n;c++)h+=bp[lp[l][c]]*(sp[lk[l][c][0]]*sp[lk[l][c][1]]*sp[lk[l][c][2]]);
    sp[l]=(ur()<1.0/(1.0+exp(-2*h)))?1:-1;}
}
static double stacksum(void){double s=0;for(int i=0;i<nst;i++){int x=stk[i]/NPL,pl=stk[i]%NPL;int o[4];plq(x,pa[pl],pb[pl],o);s+=sp[o[0]]*sp[o[1]]*sp[o[2]]*sp[o[3]];}return s;}
#define NTH 2000
#define NME 20000
#define NB 20
static void chain(double beta,double s,int hot,uint64_t seed,double*mean,double*err){
  st=seed;for(int i=0;i<NP;i++)bp[i]=beta;for(int i=0;i<nst;i++)bp[stk[i]]=beta*(1-2*s);
  for(int l=0;l<NL;l++)sp[l]=hot?((rnd()&1)?1:-1):1;
  for(int i=0;i<NTH;i++)sweep();
  double bins[NB]={0};for(int i=0;i<NME;i++){sweep();bins[i/(NME/NB)]+=stacksum();}
  double m=0;for(int b=0;b<NB;b++){bins[b]/=(NME/NB);m+=bins[b];}m/=NB;
  double v=0;for(int b=0;b<NB;b++)v+=(bins[b]-m)*(bins[b]-m);v/=(NB-1);
  *mean=m;*err=sqrt(v/NB);
}
static void gl(int n,double*x,double*w){for(int i=0;i<n;i++){double z=cos(M_PI*(i+0.75)/(n+0.5)),pp=0;
  for(int it=0;it<100;it++){double p1=1,p2=0;for(int j=0;j<n;j++){double p3=p2;p2=p1;p1=((2*j+1)*z*p2-j*p3)/(j+1);}
    pp=n*(z*p1-p2)/(z*z-1);double dz=p1/pp;z-=dz;if(fabs(dz)<1e-15)break;}
  x[i]=0.5*(1-z);w[i]=1.0/((1-z*z)*pp*pp);}}  /* on [0,1]: weight = 2/((1-z^2)pp^2)/2 */
int main(int argc,char**argv){
  D=atoi(argv[1]);L=atoi(argv[2]);double beta=atof(argv[3]);int n=atoi(argv[4]);long sb=atol(argv[5]);
  FILE*f=fopen(argv[6],"wx");if(!f){perror("outfile exists/err");return 3;}
  setup();double x[64],w[64];gl(n,x,w);
  double F=0,V=0;int ok=0;
  fprintf(f,"# D=%d L=%d beta=%g n=%d nstack=%d\n# node s w mean_hot err_hot mean_cold err_cold mean err agree\n",D,L,beta,n,nst);
  for(int i=0;i<n;i++){double mh,eh,mc,ec;
    uint64_t sd=(uint64_t)sb*1000003ULL+L*7919ULL+i*104729ULL+(int)(beta*1000)*31ULL;
    chain(beta,x[i],1,sd*2+1,&mh,&eh);chain(beta,x[i],0,sd*2+2,&mc,&ec);
    double m=0.5*(mh+mc),e=0.5*sqrt(eh*eh+ec*ec);int ag=fabs(mh-mc)<3*sqrt(eh*eh+ec*ec);ok+=ag;
    F+=2*beta*w[i]*m;V+=pow(2*beta*w[i]*e,2);
    fprintf(f,"%d %.8f %.8f %.6f %.6f %.6f %.6f %.6f %.6f %d\n",i,x[i],w[i],mh,eh,mc,ec,m,e,ag);}
  fprintf(f,"RESULT D=%d L=%d beta=%g n=%d F=%.6f err=%.6f agree=%d/%d\n",D,L,beta,n,F,sqrt(V),ok,n);
  printf("RESULT D=%d L=%d beta=%g n=%d F=%.6f err=%.6f agree=%d/%d\n",D,L,beta,n,F,sqrt(V),ok,n);
  fclose(f);return 0;}
