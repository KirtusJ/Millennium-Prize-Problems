/* Fourier evaluation over F_193: use a root of order 96 for all periods. */
static const int per[4]={6,2,2,2},st[4]={8,4,2,1};
static const int planes[6][2]={{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
static int phases[96],fcov[48][6][6];
typedef struct { int x[4],plane; } Mark;
static int f193(int x){int z=x%193;return z<0?z+193:z;}
static int fpow(int a,int n) {
    int value=1;
    while(n){if(n&1)value=value*a%193;a=a*a%193;n/=2;}
    return value;
}
static int antiperiodic(int d,int color){return (d==1 && color!=0)||(d==2 && color!=1);}
static int zphase(int e){int i=e%96;return phases[i<0?i+96:i];}
static void build_fourier(int color) {
    for(int x=0;x<48;++x)for(int i=0;i<6;++i)for(int j=0;j<6;++j)fcov[x][i][j]=0;
    for(int k=0;k<48;++k){
        int ex[4],u[4],v[4],den=0;
        for(int d=0;d<4;++d){
            ex[d]=(96*((k/st[d])%per[d])+48*antiperiodic(d,color))/per[d];
            u[d]=f193(zphase(ex[d])-1);v[d]=f193(zphase(-ex[d])-1);den+=u[d]*v[d];
        }
        int norm=f193(den*48);
        if(!norm)finish(9);
        norm=fpow(norm,191);
        for(int i=0;i<6;++i)for(int j=0;j<6;++j) {
            int a=planes[i][0],b=planes[i][1],c=planes[j][0],d=planes[j][1];
            int q=f193((b==d)*u[a]*v[c]-(b==c)*u[a]*v[d]-(a==d)*u[b]*v[c]+(a==c)*u[b]*v[d]);
            for(int x=0;x<48;++x) {
                int e=0;
                for(int z=0;z<4;++z)e+=ex[z]*((x/st[z])%per[z]);
                fcov[x][i][j]=f193(fcov[x][i][j]+q*norm*zphase(e));
            }
        }
    }
}
static int covariance(Mark a,Mark b,int color) {
    int x=0,sign=1;
    for(int d=0;d<4;++d) {
        int diff=a.x[d]-b.x[d];
        if(diff<0){diff+=per[d];if(antiperiodic(d,color))sign=-sign;}
        x+=diff*st[d];
    }
    return f193(sign*fcov[x][a.plane][b.plane]);
}
static void fill_marks(Mark f[3][24],int dual,int skew) {
    for(int i=0;i<3;++i)for(int t=0;t<6;++t) {
        int a=planes[t][0],b=planes[t][1],r=5-t;
        for(int k=0;k<4;++k) {
            Mark m={{2*i,0,0,0},dual?r:t};
            if(skew && i>0){m.x[1]=1;m.x[i==1?2:3]=1;}
            m.x[planes[r][0]]+=k&1;m.x[planes[r][1]]+=(k>>1)&1;
            if(dual){++m.x[a];++m.x[b];}
            for(int d=0;d<4;++d)m.x[d]%=per[d];
            f[i][4*t+k]=m;
        }
    }
}
static void fourier_readings(unsigned char out[5],int skew) {
    for(int i=0;i<96;++i)phases[i]=fpow(25,i);
    if(phases[48]!=192 || phases[32]==1)finish(9);
    int pair[2]={0,0},triangle[2]={0,0},abel=0;
    for(int color=0;color<3;++color) {
        build_fourier(color);
        for(int dual=0;dual<2;++dual) {
            Mark f[3][24];int cross[3][24][24];
            fill_marks(f,dual,skew);
            for(int z=0;z<3;++z)for(int i=0;i<24;++i)for(int j=0;j<24;++j) {
                int u=covariance(f[z][i],f[(z+1)%3][j],color);
                cross[z][i][j]=u;
                if(z==0)pair[dual]=f193(pair[dual]+97*u*u);
            }
            for(int z=0;z<3;++z)for(int i=0;i<24;++i) {
                int jz=(z+1)%3,kz=(z+2)%3,aa=0,bb=0,loop=0;
                for(int j=0;j<24;++j) {
                    int u=cross[z][i][j],v=cross[kz][j][i];
                    aa=f193(aa+u*u);bb=f193(bb+v*v);
                    for(int k=0;k<24;++k)
                        loop=f193(loop+u*cross[jz][j][k]*cross[kz][k][i]);
                }
                if(z==0)triangle[dual]=f193(triangle[dual]+loop);
                if(!dual) {
                    int diagonal=fcov[0][f[z][i].plane][f[z][i].plane];
                    abel=f193(abel+145*(aa*bb-(1-2*diagonal)*loop));
                }
            }
        }
    }
    if(pair[0]!=pair[1] || f193(triangle[0]+triangle[1])!=0)finish(9);
    out[0]=(unsigned char)pair[0];out[1]=(unsigned char)pair[1];
    out[2]=(unsigned char)triangle[0];out[3]=(unsigned char)triangle[1];
    out[4]=(unsigned char)abel;
}
