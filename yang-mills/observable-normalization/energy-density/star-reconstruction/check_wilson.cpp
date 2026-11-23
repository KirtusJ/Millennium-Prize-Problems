// Conditional redraws on complete periodic Wilson histories. The lookup table
// is the deterministic Abel inverse, tabulated by check_reconstruction.py.
#define WILSON_CONTACT_LIBRARY
#include "../wilson-contact/check_wilson.cpp"
#include <fstream>

struct Table {
    std::vector<double> values;
    double step;
    explicit Table(const char* file) {
        std::ifstream in(file);
        if (!(in >> step) || !(step>0)) throw std::runtime_error("missing inverse table");
        double h;
        while (in >> h) values.push_back(h);
        if (values.size()<2) throw std::runtime_error("empty inverse table");
    }
    double operator()(double x) const {
        const double index=std::abs(x)/step;
        const auto i=static_cast<std::size_t>(index);
        if (i+1>=values.size()) throw std::runtime_error("star outside table");
        return values[i]+(index-i)*(values[i+1]-values[i]);
    }
};

void run_inverse(double beta,const Table& h) {
    Box box(61061,true);
    for (int n=0;n<90;++n) box.sweep(beta);
    constexpr int blocks=28, redraws=24;
    std::array<std::array<double,4>,blocks> means{};
    for (auto& row:means) {
        box.sweep(beta);
        for (int x=0;x<sites;++x) {
            const auto H=box.staple(x,3,beta);
            const double R=std::sqrt(dot(H,H));
            const double m=std::cyl_bessel_i(2,R)/std::cyl_bessel_i(1,R);
            const double V=R*R*(1-m*m-3*m/R);
            for (int i=0;i<redraws;++i) {
                auto u=box.draw(H);
                // The bounded reading receives just the six ordinary traces.
                double X=0;
                for (int j=0;j<3;++j)
                    X+=beta*(dot(u,box.upper(x,3,j))+dot(u,box.lower(x,3,j)));
                const double resid=h(X)-V;
                const double raw=std::pow(R*m-X,2)-V;
                row[0]+=resid/(sites*redraws);
                row[1]+=raw/(sites*redraws);
                row[2]+=resid*resid/(sites*redraws);
                row[3]+=raw*raw/(sites*redraws);
            }
        }
    }
    std::array<double,4> avg{};
    for (auto row:means) for (int j=0;j<4;++j) avg[j]+=row[j]/blocks;
    for (int j=0;j<2;++j) {
        double v=0;
        for (auto row:means) v+=std::pow(row[j]-avg[j],2)/(blocks*(blocks-1));
        // Conservative allowance for the separate interpolation control.
        if (std::abs(avg[j])>6*std::sqrt(v)+5e-5)
            throw std::runtime_error("fiber conditional-mean check failed");
    }
    std::cout << "beta " << beta << " mean errors " << avg[0] << " " << avg[1]
              << " conditional noise h,W^2 " << avg[2] << " " << avg[3]
              << " beta^4 noise of h " << std::pow(beta,4)*avg[2] << "\n";
}

int main(int argc,char** argv) {
    if (argc!=2) return 2;
    const Table h(argv[1]);
    run_inverse(1.2,h);
    run_inverse(4.,h);
    run_inverse(12.,h);
}
