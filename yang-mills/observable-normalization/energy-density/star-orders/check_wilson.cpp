// Check the q=2 observable with ordinary SU(2) temporal stars on a periodic 4^4 box.
#define WILSON_CONTACT_LIBRARY
#include "../wilson-contact/check_wilson.cpp"

using Row = std::array<double,8>;
using Results = std::array<double,5>;

struct Quartic {
    const std::array<double,4> radii{.5,1.,2.,4.};
    std::array<double,4> coeff{};
    double offset=0;
    Quartic() {
        const double d=.70662423756, a=d/2, b=(2-d)/3;
        for (int j=0;j<4;++j) {
            const double r=radii[j];
            double w=(-r-1)*(-r-a)*(-r-b);
            for (int k=0;k<4;++k) if (k!=j) w/=radii[k]-r;
            coeff[j]=w*std::pow(1+1/r,1.5)*std::pow(1+a/r,3)*std::pow(1+b/r,4.5);
            offset+=w;
        }
    }
    double raw(double S) const {
        double value=-offset;
        for (int j=0;j<4;++j) value+=coeff[j]*std::exp(-S/radii[j]);
        return value;
    }
    static double Z(double r) { return r==0 ? 1 : 2*std::cyl_bessel_i(1,r)/r; }
    std::array<double,3> conditional(double R,double beta) const {
        const double z=Z(R);
        const double m=R==0 ? 0 : std::cyl_bessel_i(2,R)/std::cyl_bessel_i(1,R);
        const double meanS=6*beta-R*m;
        double value=-offset, mixed=-offset*meanS;
        for (int j=0;j<4;++j) {
            const double t=1/radii[j];
            const double T=(1+t)*R, Zt=Z(T);
            const double J=coeff[j]*std::exp(-6*beta*t)*Zt/z;
            const double tiltedMean=T==0 ? 0 : 2*std::cyl_bessel_i(2,T)/(T*Zt);
            value+=J;
            mixed+=J*(6*beta-R*tiltedMean);
        }
        return {value,meanS,mixed};
    }
};

Results summarize(const Row& r) {
    return {r[0]-r[1],r[4]-r[0]*r[2],r[6]-r[1]*r[3],
            (r[5]-r[0]*r[2])-(r[6]-r[1]*r[3]),r[7]-r[1]*r[3]};
}

void run_orders(double beta) {
    Quartic probe;
    constexpr int grid=10000, blocks=76, length=32;
    const double step=6*beta/grid;
    std::vector<std::array<double,3>> table;
    for (int i=0;i<=grid;++i) table.push_back(probe.conditional(i*step,beta));
    std::vector<Row> bins;
    for (int chain=0;chain<4;++chain) {
        Box box(12390+chain,chain%2==1);
        for (int n=0;n<200;++n) box.sweep(beta);
        for (int block=0;block<blocks;++block) {
            Row row{};
            for (int sample=0;sample<length;++sample) {
                box.sweep(beta);
                std::array<double,sites> S{}, f{}, projectS{}, projectF{}, mixed{};
                for (int x=0;x<sites;++x) {
                    const auto H=box.staple(x,3,beta);
                    const double R=std::sqrt(dot(H,H));
                    const int i=std::min(grid-1,int(R/step));
                    const double a=R/step-i;
                    S[x]=6*beta-dot(box.U[x][3],H);
                    f[x]=probe.raw(S[x]);
                    projectF[x]=(1-a)*table[i][0]+a*table[i+1][0];
                    projectS[x]=(1-a)*table[i][1]+a*table[i+1][1];
                    mixed[x]=(1-a)*table[i][2]+a*table[i+1][2];
                    if (sample==0 && x==0) {
                        const auto truth=probe.conditional(R,beta);
                        if (std::abs(truth[0]-projectF[x])>1e-4 || std::abs(truth[1]-projectS[x])>1e-4 || std::abs(truth[2]-mixed[x])>1e-4)
                            throw std::runtime_error("conditional interpolation check");
                    }
                }
                for (int x=0;x<sites;++x) {
                    const int y=box.up[x][3];
                    Row obs{f[x],projectF[x],S[x],projectS[x],f[x]*S[x],f[x]*S[y],projectF[x]*projectS[y],mixed[x]};
                    for (unsigned i=0;i<row.size();++i) row[i]+=obs[i]/(sites*length);
                }
            }
            bins.push_back(row);
        }
    }
    Row avg{};
    const int count=static_cast<int>(bins.size());
    for (auto row:bins) for (unsigned i=0;i<row.size();++i) avg[i]+=row[i]/count;
    auto values=summarize(avg);
    Results mean{}, var{};
    std::vector<Results> estimates;
    for (auto row:bins) {
        for (unsigned i=0;i<row.size();++i) row[i]=(count*avg[i]-row[i])/(count-1);
        estimates.push_back(summarize(row));
        for (unsigned i=0;i<mean.size();++i) mean[i]+=estimates.back()[i]/count;
    }
    for (auto est:estimates) for (unsigned i=0;i<mean.size();++i)
        var[i]+=std::pow(est[i]-mean[i],2)*(count-1)/count;
    std::cout<<"beta "<<beta<<" mean difference, equal-time mixed, projected one-step mixed, raw minus projected one-step, integrated equal-time mixed\n";
    for (unsigned i=0;i<mean.size();++i) std::cout<<values[i]<<" +/- "<<std::sqrt(var[i])<<"   ";
    std::cout<<"\n";
    for (int i:{0,3}) if (std::abs(values[i])>6*std::sqrt(var[i])+1e-4)
        throw std::runtime_error("conditional expectation identity");
}

int main() {
    run_orders(2.3);
    run_orders(8.);
}
