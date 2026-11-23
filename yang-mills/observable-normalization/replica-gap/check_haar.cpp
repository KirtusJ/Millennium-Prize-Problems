// Four independent SU(2) electric vacuum slices on a 5^3 spatial torus.
#define WILSON_CONTACT_LIBRARY
#include "../energy-density/wilson-contact/check_wilson.cpp"

namespace {
constexpr int length = 5, volume = length*length*length, faces = 3*volume;
using Links = std::array<Quat, 3*volume>;
using Traces = std::array<double, faces>;

int shift(int x, int direction) {
    const int stride = direction == 0 ? 1 : (direction == 1 ? length : length*length);
    return x + ((x/stride)%length == length-1 ? 1-length : 1)*stride;
}

Traces sample(Box& generator) {
    Links links;
    for (auto& link : links) link = generator.haar();
    Traces traces;
    int p = 0;
    for (int x=0; x<volume; ++x) {
        for (int i=0; i<3; ++i) for (int j=i+1; j<3; ++j) {
            const auto forward = mul(links[3*x+i], links[3*shift(x,i)+j]);
            const auto backward = mul(links[3*x+j], links[3*shift(x,j)+i]);
            traces[p++] = 2*dot(forward, backward);
        }
    }
    return traces;
}
}

int main() {
    Box generator(20261123, false);
    constexpr int blocks=80, draws=250;
    std::array<double, blocks> mean{}, fourth{};
    for (int k=0; k<blocks; ++k) {
        for (int it=0; it<draws; ++it) {
            auto x=sample(generator), y=sample(generator), u=sample(generator), v=sample(generator);
            double j=0;
            for (int p=0; p<faces; ++p) j += (x[p]-y[p])*(u[p]-v[p]);
            const double normalized=j*j/(4*faces);
            mean[k] += normalized/draws;
            fourth[k] += normalized*normalized/draws;
        }
    }
    auto check=[](const auto& block, double exact) {
        double m=0, se=0;
        for (double x : block) m+=x/blocks;
        for (double x : block) se+=(x-m)*(x-m)/(blocks*(blocks-1));
        se=std::sqrt(se);
        std::cout << std::setprecision(9) << "mean " << m << "   block SE " << se
                  << "   target " << exact << '\n';
        if (std::abs(m-exact)>6*se) throw std::runtime_error("moment control failed");
    };
    check(mean, 1.);
    check(fourth, 3.+13./(4*faces));
}
