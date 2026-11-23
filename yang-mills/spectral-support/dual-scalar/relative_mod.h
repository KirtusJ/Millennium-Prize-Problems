/* Boundary links fixed to identity. The remaining forest goes straight to the low time face. */
static int dual_chord[189][4];
static const int ds[4]={27,9,3,1};
static int dc(int x,int d) {return (x/ds[d])%(d==0?7:3);}
static int rel_cell(int x,int mask) {
    for(int d=0;d<4;++d) {
        int k=dc(x,d),end=(d==0?6:2);
        if(k==end || (!(mask&(1<<d)) && !k)) return 0;
    }
    return 1;
}
static void relative_slot(Face *f,int x,int d,int s) {
    int e=dual_chord[x][d];
    if(e<0)return;
    int i=f->length++; f->edge[i]=e; f->sign[i]=s;
}
static void relative_geometry(void) {
    int n=0,p=0;
    faces=96; bonds=31; triple_count=0;
    for(int i=0;i<bonds;++i)for(int j=0;j<2*bonds;++j)augmented[i][j]=(Jet){{0}};
    for(int x=0;x<189;++x)for(int d=0;d<4;++d) {
        dual_chord[x][d]=-1;
        if(!rel_cell(x,1<<d))continue;
        if(d==0 && rel_cell(x+ds[0],0))continue;
        dual_chord[x][d]=n++;
    }
    for(int x=0;x<189;++x)for(int a=0;a<4;++a)for(int b=a+1;b<4;++b) {
        if(!rel_cell(x,(1<<a)|(1<<b)))continue;
        Face *f=&face[p++]; *f=(Face){0};
        f->weight.c[0]=1;
        for(int i=0;i<3;++i) {
            int keep=1;
            for(int d=0;d<4;++d) {
                int k=dc(x,d),v=(d==0?1+2*i:1);
                if(v<k || v>k+(d==a || d==b))keep=0;
            }
            f->weight.c[1<<i]=keep;
        }
        relative_slot(f,x,a,1);relative_slot(f,x+ds[a],b,1);
        relative_slot(f,x+ds[b],a,-1);relative_slot(f,x,b,-1);
        if(f->length>2)finish(6);
        for(int i=0;i<f->length;++i)for(int j=0;j<f->length;++j) {
            Jet *h=&augmented[f->edge[i]][f->edge[j]];
            *h=add(*h,f->sign[i]*f->sign[j],f->weight);
        }
    }
    if(n!=bonds || p!=faces)finish(6);
}
