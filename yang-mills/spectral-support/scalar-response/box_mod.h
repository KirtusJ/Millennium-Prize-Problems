/* Independent field-arithmetic evaluator on three open four-dimensional boxes.
   A coefficient mask records its three distinct source derivatives. */
enum { prime=101, max_bonds=153, max_faces=236, max_sites=96 };
static int bonds,faces,sites,extent[4],stride[4];
typedef struct { int c[8]; } Jet;
typedef struct { int edge[4], sign[4], length; Jet weight; } Face;
typedef struct { int edge[3], sign; Jet weight; } Triple;
static Face face[max_faces];
static Triple triples[4*max_faces];
static Jet augmented[max_bonds][2*max_bonds];
static int chord[max_sites][4], triple_count;
static int curvature[max_faces][max_faces];

static int residue(int x) {
    int r=x%prime;
    return r<0?r+prime:r;
}
static Jet add(Jet a, int scale, Jet b) {
    for (int k=0;k<8;++k) a.c[k]=residue(a.c[k]+scale*b.c[k]);
    return a;
}
static Jet multiply(Jet a, Jet b) {
    Jet c;
    for (int mask=0;mask<8;++mask) {
        int sum=0,sub=mask;
        for (;;) {
            sum+=a.c[sub]*b.c[mask^sub];
            if (!sub) break;
            sub=(sub-1)&mask;
        }
        c.c[mask]=sum%prime;
    }
    return c;
}
static Jet inverse(Jet a) {
    Jet ans={{0}};
    for (int k=1;k<prime;++k) if (k*a.c[0]%prime==1) ans.c[0]=k;
    if (!ans.c[0]) finish(5);
    for (int mask=1;mask<8;++mask) {
        int sum=0;
        for (int sub=mask;sub;sub=(sub-1)&mask) sum+=a.c[sub]*ans.c[mask^sub];
        ans.c[mask]=residue(-ans.c[0]*sum);
    }
    return ans;
}
static int coord(int x, int axis) {
    return (x/stride[axis])%(extent[axis]+1);
}
static void slot(Face *f,int site,int axis,int sign) {
    int e=chord[site][axis];
    if (e>=0) {
        int k=f->length++;
        f->edge[k]=e;
        f->sign[k]=sign;
    }
}
static int in_cell(int x,int a,int b,int time,int transverse) {
    int origin[4]={time,transverse,0,0};
    for (int d=0;d<4;++d) {
        int site=coord(x,d);
        if (site<origin[d] || site+(d==a || d==b)>origin[d]+1) return 0;
    }
    return 1;
}
static void geometry(int layout,int profile) {
    extent[0]=layout==1?9:5;
    extent[1]=layout==2?3:1;
    extent[2]=extent[3]=1;
    sites=1;
    for (int d=3;d>=0;--d) { stride[d]=sites; sites*=extent[d]+1; }
    const int counts[3][3]={{65,96,124},{113,168,220},{153,236,332}};
    bonds=counts[layout][0]; faces=counts[layout][1]; triple_count=0;
    for (int i=0;i<bonds;++i) for (int j=0;j<2*bonds;++j) augmented[i][j]=(Jet){{0}};
    for (int i=0;i<faces;++i) face[i]=(Face){0};
    int n=0,p=0;
    for (int x=0;x<sites;++x) for (int a=0;a<4;++a) {
        chord[x][a]=-1;
        if (coord(x,a)==extent[a]) continue;
        int y=x+stride[a], parent=0;
        while (!coord(y,parent)) ++parent;
        if (parent!=a) chord[x][a]=n++;
    }
    for (int x=0;x<sites;++x) for (int a=0;a<4;++a) for (int b=a+1;b<4;++b) {
        if (coord(x,a)==extent[a] || coord(x,b)==extent[b]) continue;
        Face *f=&face[p++];
        f->weight.c[0]=1;
        f->weight.c[1]=in_cell(x,a,b,0,0);
        if (layout==0) {
            f->weight.c[2]=in_cell(x,a,b,2,0);
            f->weight.c[4]=in_cell(x,a,b,4,0);
        } else {
            f->weight.c[2]=in_cell(x,a,b,extent[0]-1,0);
            if (layout==1) {
                int t=profile+2;
                f->weight.c[4]=in_cell(x,a,b,t,0)+(t!=4 && in_cell(x,a,b,8-t,0));
            } else f->weight.c[4]=in_cell(x,a,b,2,profile);
        }
        slot(f,x,a,1); slot(f,x+stride[a],b,1);
        slot(f,x+stride[b],a,-1); slot(f,x,b,-1);
        for (int i=0;i<f->length;++i) for (int j=0;j<f->length;++j) {
            Jet *h=&augmented[f->edge[i]][f->edge[j]];
            *h=add(*h,f->sign[i]*f->sign[j],f->weight);
        }
        for (int i=0;i<f->length;++i) for (int j=i+1;j<f->length;++j)
          for (int k=j+1;k<f->length;++k) {
            Triple *v=&triples[triple_count++];
            v->edge[0]=f->edge[i]; v->edge[1]=f->edge[j]; v->edge[2]=f->edge[k];
            v->sign=f->sign[i]*f->sign[j]*f->sign[k]; v->weight=f->weight;
          }
    }
    if (n!=bonds || p!=faces || triple_count!=counts[layout][2]) finish(6);
}
static void invert_hessian(void) {
    for (int r=0;r<bonds;++r) augmented[r][bonds+r].c[0]=1;
    for (int r=0;r<bonds;++r) {
        int pivot=r;
        while (pivot<bonds && !augmented[pivot][r].c[0]) ++pivot;
        if (pivot==bonds) finish(5);
        if (pivot!=r) for (int j=r;j<2*bonds;++j) {
            Jet tmp=augmented[pivot][j];
            augmented[pivot][j]=augmented[r][j]; augmented[r][j]=tmp;
        }
        Jet inv=inverse(augmented[r][r]);
        for (int j=r;j<2*bonds;++j) augmented[r][j]=multiply(augmented[r][j],inv);
        for (int i=0;i<bonds;++i) if (i!=r) {
            Jet a=augmented[i][r];
            int active=0;
            for (int k=0;k<8;++k) active |= a.c[k];
            if (!active) continue;
            for (int j=r;j<2*bonds;++j)
                augmented[i][j]=add(augmented[i][j],-1,multiply(a,augmented[r][j]));
        }
    }
}
static Jet cov(int i,int j) { return augmented[i][bonds+j]; }
static Jet wick(Face *f,int i,int j,int k,int l) {
    int a=f->edge[i],b=f->edge[j],c=f->edge[k],d=f->edge[l];
    Jet z={{0}};
    z=add(z,9,multiply(cov(a,b),cov(c,d)));
    z=add(z,3,multiply(cov(a,c),cov(b,d)));
    z=add(z,3,multiply(cov(a,d),cov(b,c)));
    return add((Jet){{0}},f->sign[i]*f->sign[j]*f->sign[k]*f->sign[l],z);
}
static Jet fourth(Face *f) {
    Jet q={{0}};
    for (int i=0;i<f->length;++i) {
        q=add(q,1,wick(f,i,i,i,i));
        for (int j=i+1;j<f->length;++j) {
            q=add(q,6,wick(f,i,i,j,j));
            q=add(q,4,wick(f,i,j,i,i));
            q=add(q,4,wick(f,i,j,j,j));
            for (int k=0;k<f->length;++k) if (k!=i && k!=j) q=add(q,12,wick(f,i,j,k,k));
        }
    }
    if (f->length==4) {
        q=add(q,24,wick(f,0,1,2,3)); q=add(q,-24,wick(f,0,2,1,3)); q=add(q,24,wick(f,0,3,1,2));
    }
    return q;
}
static Jet cubic_pair(Triple *a,Triple *b) {
    Jet det={{0}};
    for (int i=0;i<3;++i) {
        int j=(i+1)%3,k=(i+2)%3;
        Jet minor=multiply(cov(a->edge[1],b->edge[j]),cov(a->edge[2],b->edge[k]));
        minor=add(minor,-1,multiply(cov(a->edge[1],b->edge[k]),cov(a->edge[2],b->edge[j])));
        det=add(det,1,multiply(cov(a->edge[0],b->edge[i]),minor));
    }
    return multiply(det,multiply(a->weight,b->weight));
}
static int tree_triangle(void) {
    for (int i=0;i<faces;++i) for (int j=0;j<=i;++j) {
        int n=0;
        for (int a=0;a<face[i].length;++a) for (int b=0;b<face[j].length;++b)
            n+=face[i].sign[a]*face[j].sign[b]*cov(face[i].edge[a],face[j].edge[b]).c[0];
        curvature[i][j]=curvature[j][i]=residue(n);
    }
    int sum=0;
    for (int i=0;i<faces;++i) if (face[i].weight.c[1])
      for (int j=0;j<faces;++j) if (face[j].weight.c[2])
        for (int k=0;k<faces;++k) if (face[k].weight.c[4]) {
            int value=curvature[i][j]*curvature[j][k]*curvature[k][i];
            sum=(sum+face[k].weight.c[4]*value)%prime;
        }
    return 3*sum%prime;
}
#ifdef D4_DUAL_SCALAR
#include "../dual-scalar/relative_mod.h"
#endif
static void compute(int layout,int profile,unsigned char out[9]) {
#ifdef D4_DUAL_SCALAR
    if (layout==3) relative_geometry(); else geometry(layout,profile);
#else
    geometry(layout,profile);
#endif
    invert_hessian();
    Jet total={{0}},matched={{0}};
    for (int e=0;e<bonds;++e) total=add(total,-24,cov(e,e));
    for (int p=0;p<faces;++p) {
        Face *f=&face[p];
        Jet v={{0}};
        for (int i=0;i<f->length;++i) for (int j=0;j<f->length;++j)
            v=add(v,f->sign[i]*f->sign[j],cov(f->edge[i],f->edge[j]));
        matched=add(matched,-9,multiply(f->weight,multiply(v,v)));
        total=add(total,1,multiply(f->weight,fourth(f)));
    }
    for (int i=0;i<triple_count;++i) for (int j=0;j<=i;++j) {
        int scale=(i==j?72:144)*triples[i].sign*triples[j].sign;
        total=add(total,scale,cubic_pair(&triples[i],&triples[j]));
    }
    Jet div=inverse((Jet){{24}});
    total=multiply(total,div); matched=multiply(matched,div);
    const int masks[4]={3,5,6,7};
    for (int j=0;j<4;++j) {
        int s=(j==3?-1:1);
        out[j]=(unsigned char)residue(s*total.c[masks[j]]);
        out[4+j]=(unsigned char)residue(s*matched.c[masks[j]]);
    }
    out[8]=(unsigned char)tree_triangle();
}

/* Solve the two calibration equations in the finite field. The midpoint or
   outer transverse cube has coefficient one. Return the Wilson response. */
static void calibrated(int layout,unsigned char out[5]) {
    unsigned char row[3][9];
    for (int i=0;i<3;++i) compute(layout,i,row[i]);
    int c[3];
    for (int i=0;i<3;++i) {
        int j=(i+1)%3,k=(i+2)%3;
        c[i]=residue(row[j][8]*row[k][7]-row[k][8]*row[j][7]);
    }
    int scale=inverse((Jet){{c[2]}}).c[0];
    int tree=0,matched=0,wilson=0;
    for (int i=0;i<3;++i) {
        c[i]=c[i]*scale%prime;
        tree+=c[i]*row[i][8]; matched+=c[i]*row[i][7]; wilson+=c[i]*row[i][3];
    }
    out[0]=(unsigned char)c[0]; out[1]=(unsigned char)c[1];
    out[2]=(unsigned char)residue(tree); out[3]=(unsigned char)residue(matched);
    out[4]=(unsigned char)residue(wilson);
    if (out[2] || out[3] || !out[4]) finish(7);
}
