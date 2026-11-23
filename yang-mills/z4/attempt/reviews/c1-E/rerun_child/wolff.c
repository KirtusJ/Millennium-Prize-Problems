/* wolff.c - Wolff single-cluster MC, 2D Ising torus, K=Kc=ln(1+sqrt2)/2.
 * usage: wolff L nclusters seed outfile   (outfile opened exclusively; refuses to overwrite)
 * PREDICATES fixed before first run (tolerances: my own expectation, not target defects):
 *  P1 (L=4 vs exact 0.6171993184): |U4_MC-U4_exact| <= 3 sigma (jackknife over 20 bins; 3 sigma = usual stat. tolerance)
 *  P2 for each L in {8,16,32,(64)}: U4 > 0.3 (well away from 0; Gaussian value is 0) and U4 within [0.55,0.75]
 *     (expectation: U4* ~ 0.61 from memory, finite-size corrections of order L^-2 small/ up to ~0.02; band is my wide guess)
 *  P3 for consecutive L pairs: |U4(L)-U4(2L)| <= 3 combined sigma + 0.02 (allowance for corrections to scaling, my guess)
 *  P4 fit of ln(<M2>/L^2) vs ln L over L=4..32/64: slope within 0.05 of 7/4 (corrections-to-scaling allowance, my guess)
 * Algorithm: bond prob p=1-exp(-2K); one measurement of M after each cluster flip; first 5% of clusters discarded;
 * 20 equal bins; jackknife error of U4 and of <M2>/L^2. RNG: xorshift64* seeded from seed arg.
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
static uint64_t st;
static inline uint64_t nx(void){st^=st>>12;st^=st<<25;st^=st>>27;return st*2685821657736338717ULL;}
static inline double ur(void){return (nx()>>11)*(1.0/9007199254740992.0);}
int main(int ac,char**av){
 if(ac<5)return 2; int L=atoi(av[1]); long nc=atol(av[2]); st=strtoull(av[3],0,10)*0x9E3779B97F4A7C15ULL+88172645463325252ULL;
 for(int i=0;i<20;i++)nx();
 FILE*f=fopen(av[4],"rb"); if(f){fprintf(stderr,"exists\n");return 3;} f=fopen(av[4],"wx"); if(!f)return 3;
 int N=L*L; double K=0.5*log(1+sqrt(2.0)), p=1-exp(-2*K);
 signed char*s=malloc(N); int*stk=malloc(N*sizeof(int)); for(int i=0;i<N;i++)s[i]=1; long M=N;
 const int NB=20; long disc=nc/20; long per=(nc-disc)/NB;
 double b2[NB],b4[NB]; long cnt[NB]; for(int b=0;b<NB;b++)b2[b]=b4[b]=0,cnt[b]=0;
 double avc=0;
 for(long t=0;t<nc;t++){
  int seed=nx()%N; signed char sv=s[seed]; int sp=0; stk[sp++]=seed; s[seed]=-sv; long cs=1;
  while(sp){int i=stk[--sp]; int x=i%L,y=i/L; int nb[4]={y*L+(x+1)%L,y*L+(x+L-1)%L,((y+1)%L)*L+x,((y+L-1)%L)*L+x};
   for(int k=0;k<4;k++){int j=nb[k]; if(s[j]==sv&&ur()<p){s[j]=-sv;stk[sp++]=j;cs++;}}}
  M-=2*sv*cs;
  if(t>=disc){long b=(t-disc)/per; if(b>=NB)b=NB-1; double m2=(double)M*M; b2[b]+=m2; b4[b]+=m2*m2; cnt[b]++; avc+=cs;}
 }
 double T2=0,T4=0; long TC=0; for(int b=0;b<NB;b++){T2+=b2[b];T4+=b4[b];TC+=cnt[b];}
 double m2=T2/TC,m4=T4/TC,U=1-m4/(3*m2*m2);
 double ju=0,ju2=0,jm=0,jm2=0; double us[NB],ms[NB];
 for(int b=0;b<NB;b++){double a2=(T2-b2[b])/(TC-cnt[b]),a4=(T4-b4[b])/(TC-cnt[b]); us[b]=1-a4/(3*a2*a2); ms[b]=a2/N;}
 double mu=0,mm=0; for(int b=0;b<NB;b++){mu+=us[b];mm+=ms[b];} mu/=NB;mm/=NB;
 for(int b=0;b<NB;b++){ju+=(us[b]-mu)*(us[b]-mu);jm+=(ms[b]-mm)*(ms[b]-mm);}
 double eu=sqrt((NB-1.0)/NB*ju), em=sqrt((NB-1.0)/NB*jm);
 fprintf(f,"L=%d nclusters=%ld seed=%s bins=%d meas=%ld U4=%.6f +- %.6f M2/L2=%.5f +- %.5f meanclus=%.2f\n",L,nc,av[3],NB,TC,U,eu,m2/N,em,avc/TC);
 fclose(f); return 0;}
