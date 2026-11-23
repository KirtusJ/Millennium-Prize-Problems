/* Independent finite-field inversion of the grounded 8 by 8 surface graph. */
static int patch_aug[64][128];
static int pu[176], pv[176], weight_at[176];

static int minimum(int a, int b) { return a < b ? a : b; }
static int inverse_scalar(int x, int p) {
    int y=1;
    for(int k=p-2;k;k/=2) {
        if(k&1)y=y*x%p;
        x=x*x%p;
    }
    return y;
}
static int inverse_at(int i,int j) {
    return i==64 || j==64 ? 0 : patch_aug[i][64+j];
}
static void surface_readings(int prime, unsigned char result[3]) {
    static const int ground[4][4]={{2,4,5,6},{4,9,14,17},{5,14,22,27},{6,17,27,32}};
    static const int bond[4][4]={{2,4,5,6},{3,7,11,13},{4,9,14,17},{4,10,16,19}};
    int n=0;
    for(int u=0;u<64;++u) {
        int x=u/8,y=u%8,rx=minimum(x,7-x),ry=minimum(y,7-y);
        for(int j=0;j<128;++j)patch_aug[u][j]=0;
        patch_aug[u][64+u]=1;
        pu[n]=u;pv[n]=64;weight_at[n++]=ground[rx][ry];
        if(x<7){pu[n]=u;pv[n]=u+8;weight_at[n++]=bond[minimum(x,6-x)][ry];}
        if(y<7){pu[n]=u;pv[n]=u+1;weight_at[n++]=bond[minimum(y,6-y)][rx];}
    }
    if(n!=176)finish(4);
    for(int j=0;j<n;++j) {
        int u=pu[j],v=pv[j];++patch_aug[u][u];
        if(v<64){++patch_aug[v][v];patch_aug[u][v]=prime-1;patch_aug[v][u]=prime-1;}
    }
    for(int j=0;j<64;++j) {
        int pivot=j;
        while(pivot<64 && patch_aug[pivot][j]==0)++pivot;
        if(pivot==64)finish(4);
        for(int k=j;k<128;++k){int t=patch_aug[j][k];patch_aug[j][k]=patch_aug[pivot][k];patch_aug[pivot][k]=t;}
        int scale=inverse_scalar(patch_aug[j][j],prime);
        for(int k=j;k<128;++k)patch_aug[j][k]=patch_aug[j][k]*scale%prime;
        for(int r=0;r<64;++r)if(r!=j){
            int s=prime-patch_aug[r][j];
            for(int k=j;k<128;++k)patch_aug[r][k]=(patch_aug[r][k]+s*patch_aug[j][k])%prime;
        }
    }
    int norm=0,energy=0;
    for(int i=0;i<n;++i) {
        norm=(norm+weight_at[i]*weight_at[i])%prime;
        for(int j=0;j<n;++j) {
            int a=((i==j)-inverse_at(pu[i],pu[j])+inverse_at(pu[i],pv[j])
                    +inverse_at(pv[i],pu[j])-inverse_at(pv[i],pv[j])+2*prime)%prime;
            int term=(a*a%prime)*(weight_at[i]*weight_at[j]%prime)%prime;
            energy=(energy+6*term)%prime;
        }
    }
    result[0]=inverse_at(0,0); result[1]=norm; result[2]=energy;
}
__attribute__((used,noreturn)) static void run(void) {
    long fd=open_input("request");unsigned char stage;read_exact(fd,&stage,1);
    if(stage=='F') {
        unsigned char code,v[3];read_exact(fd,&code,1);if(code!=12)finish(4);
        surface_readings(101,v);for(int i=0;i<3;++i)emit((char)v[i]);
    }else if(stage=='S'){
        unsigned char first[3],second[3];read_exact(fd,first,3);surface_readings(193,second);
        text("-- BEGIN PCP OS generated surface patch readings\n");
        text("def measured : List Nat := [");
        for(int i=0;i<6;++i){if(i)text(", ");number(i<3?first[i]:second[i-3]);}
        text("]\n\ntheorem modularPatch : measured = expected := by decide\n\n");
    }else if(stage=='A'){
        copy_source("analytic");copy_source("certificate");
        text("#print axioms gramProduct\n#print axioms squaredIncrement\n#print axioms rowEnergy\n");
        text("#print axioms boundaryTrace\n#print axioms countExcess\n#print axioms inverseEquations\n");
        text("#print axioms patchLayout\n#print axioms patchSizes\n#print axioms patchNumerator\n#print axioms surfaceBound\n");
        text("#print axioms edgeBound\n#print axioms cornerBound\n#print axioms modularPatch\n");
        text("#print axioms centralChoose\n#print axioms walkSums\n#print axioms returnWalkBounds\n#print axioms largeSurface\n");
        text("end Millennium.YangMills.D4.BoundarySpectrum\n");
    }else finish(4);
    require_end(fd);if(os(3,fd,0,0))finish(2);flush();finish(0);
}
