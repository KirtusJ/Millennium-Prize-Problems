// Periodic four-dimensional SU(2) heat-bath check of spatial conditional averaging.
#include <algorithm>
#include <array>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <random>
#include <stdexcept>
#include <vector>

using Quat = std::array<double,4>;
using Sample = std::array<double,11>;
constexpr int side = 4, sites = side*side*side*side;
constexpr double pi = 3.14159265358979323846;
const Quat identity{1,0,0,0};

Quat add(Quat a, const Quat& b) {
    for (int j=0; j<4; ++j) a[j] += b[j];
    return a;
}
Quat scale(Quat a, double k) {
    for (double& x : a) x *= k;
    return a;
}
double dot(const Quat& a, const Quat& b) {
    double value = 0;
    for (int j=0; j<4; ++j) value += a[j]*b[j];
    return value;
}
Quat adj(Quat q) { return {q[0],-q[1],-q[2],-q[3]}; }
Quat mul(const Quat& a, const Quat& b) {
    return {a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3],
            a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2],
            a[0]*b[2]-a[1]*b[3]+a[2]*b[0]+a[3]*b[1],
            a[0]*b[3]+a[1]*b[2]-a[2]*b[1]+a[3]*b[0]};
}

struct Box {
    std::array<std::array<Quat,4>,sites> U;
    std::array<std::array<int,4>,sites> pos, up, down;
    std::mt19937_64 rng;
    std::normal_distribution<double> normal{0,1};
    std::uniform_real_distribution<double> uniform{0,1};
    std::gamma_distribution<double> gamma{1.5,1};

    Box(unsigned seed, bool hot) : rng(seed) {
        for (int site=0; site<sites; ++site) {
            int stride = 1;
            for (int j=0; j<4; ++j, stride*=side) {
                int x = (site/stride)%side;
                pos[site][j] = x;
                up[site][j] = site+(x==side-1 ? 1-side : 1)*stride;
                down[site][j] = site+(x==0 ? side-1 : -1)*stride;
                U[site][j] = hot ? haar() : identity;
            }
        }
    }
    Quat haar() {
        Quat q;
        for (double& x:q) x=normal(rng);
        return scale(q,1/std::sqrt(dot(q,q)));
    }
    Quat upper(int x, int i, int j) const {
        return mul(mul(U[x][j],U[up[x][j]][i]),adj(U[up[x][i]][j]));
    }
    Quat lower(int x, int i, int j) const {
        int y=down[x][j];
        return mul(mul(adj(U[y][j]),U[y][i]),U[up[y][i]][j]);
    }
    Quat staple(int x, int i, double beta) const {
        Quat s{};
        for (int j=0; j<4; ++j) if (j!=i) s=add(s,add(upper(x,i,j),lower(x,i,j)));
        return scale(s,beta);
    }
    Quat draw(Quat force) {
        double R=std::sqrt(dot(force,force));
        if (R==0) return haar();
        if (R<1) {
            for (;;) {
                Quat q=haar();
                if (uniform(rng)<std::exp(dot(q,force)-R)) return q;
            }
        }
        double y;
        do { y=gamma(rng)/R; } while (y>=2 || uniform(rng)>std::sqrt(1-y/2));
        Quat q{0,normal(rng),normal(rng),normal(rng)};
        q=scale(q,std::sqrt(y*(2-y)/dot(q,q)));
        q[0]=1-y;
        return mul(scale(force,1/R),q);
    }
    void sweep(double beta) {
        for (int x=0; x<sites; ++x)
            for (int i=0; i<4; ++i) U[x][i]=draw(staple(x,i,beta));
    }
    double score_pair(int x, int i, int j, double beta) const {
        int opposite=up[x][j];
        auto H=staple(x,i,beta), J=staple(opposite,i,beta);
        auto W=U[x][j];
        double score=0;
        for (int k=1; k<4; ++k) {
            Quat a{};
            a[k]=1;
            auto b=mul(mul(adj(W),a),W);
            score+=dot(mul(a,U[x][i]),H)*dot(mul(b,U[opposite][i]),J)/3;
        }
        return score+beta*dot(U[x][i],upper(x,i,j));
    }
    Sample measure(double beta) const {
        std::array<double,side> raw{}, projected{}, variance{};
        for (int x=0; x<sites; ++x) {
            int t=pos[x][3];
            double w=std::cos(2*pi*(pos[x][0]+.5)/side);
            auto a=upper(x,0,1);
            raw[t]+=w*dot(U[x][0],a);
            if ((pos[x][1]+pos[x][2])%2) continue;
            Quat b=scale(add(a,lower(x,0,1)),w);
            Quat H=staple(x,0,beta);
            double R=std::sqrt(dot(H,H));
            if (R<1e-7) { variance[t]+=dot(b,b)/4; continue; }
            Quat axis=scale(H,1/R);
            double m=std::cyl_bessel_i(2,R)/std::cyl_bessel_i(1,R);
            double longitude=dot(b,axis), trans=dot(b,b)-longitude*longitude;
            projected[t]+=m*longitude;
            variance[t]+=(1-m*m-3*m/R)*longitude*longitude+(m/R)*trans;
        }
        Sample result{};
        for (int t=0; t<side; ++t) {
            int other=(t+2)%side;
            Sample row={raw[t]*raw[t],projected[t]*projected[t],variance[t],
                        raw[t]*raw[other],projected[t]*projected[other],
                        raw[t]*raw[t]-projected[t]*projected[t]-variance[t],
                        raw[t]*raw[other]-projected[t]*projected[other]};
            for (unsigned i=0; i<row.size(); ++i) result[i]+=row[i]/side;
        }
        for (int x=0; x<sites; ++x) {
            double dual=score_pair(x,0,1,beta);
            double face=dot(U[x][0],upper(x,0,1));
            int y=up[x][0];
            double neighbor=dot(U[y][0],upper(y,0,1));
            result[7]+=dual/sites;
            result[8]+=(dual*face-face)/sites;
            result[9]+=dual*neighbor/sites;
            result[10]+=face/sites;
        }
        return result;
    }
};

void run(double beta, int blocks) {
    std::vector<Sample> block_means;
    const int block_size=32;
    for (unsigned chain=0; chain<2; ++chain) {
        Box box(38112+chain,chain==1);
        for (int i=0; i<180; ++i) box.sweep(beta);
        for (int k=0; k<blocks; ++k) {
            Sample mean{};
            for (int step=0; step<block_size; ++step) {
                box.sweep(beta);
                auto x=box.measure(beta);
                for (unsigned j=0;j<x.size();++j) mean[j]+=x[j]/block_size;
            }
            block_means.push_back(mean);
        }
    }
    Sample mean{}, se{};
    double n=block_means.size();
    for (auto x:block_means)
        for (unsigned j=0;j<x.size();++j) mean[j]+=x[j]/n;
    for (auto x:block_means)
        for (unsigned j=0;j<x.size();++j) se[j]+=std::pow(x[j]-mean[j],2)/(n*(n-1));
    for (double& e:se) e=std::sqrt(e);
    std::cout<<"beta "<<beta<<" raw variance, projected variance, conditional variance, raw C(2), projected C(2):";
    for (int j=0;j<5;++j) std::cout<<" "<<mean[j];
    std::cout<<"\npaired residuals and block SE: "<<mean[5]<<" "<<se[5]<<"   "<<mean[6]<<" "<<se[6]<<"\n";
    if (std::abs(mean[5])>6*se[5]+1e-10 || std::abs(mean[6])>6*se[6]+1e-10)
        throw std::runtime_error("paired residual exceeds the empirical check");
    std::cout<<"score mean, diagonal residual, off-diagonal, plaquette mean (and block SE):";
    for (int j=7;j<11;++j) std::cout<<" "<<mean[j]<<" +/- "<<se[j];
    std::cout<<"\n";
    for (int j=7;j<10;++j) if (std::abs(mean[j])>6*se[j]+1e-10)
        throw std::runtime_error("score dual control failed");
    if (beta==0 && (std::abs(mean[0]-8)>6*se[0] || mean[1]!=0))
        throw std::runtime_error("Haar control failed");
}

int main() {
    std::cout<<std::setprecision(8);
    run(0.,12);
    run(2.2,45);
}
