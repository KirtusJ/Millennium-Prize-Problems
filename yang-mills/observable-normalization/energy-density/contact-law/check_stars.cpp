// Check the oriented pair covariance against exact conditional redraws on 4^4 histories.
#define WILSON_CONTACT_LIBRARY
#include "../wilson-contact/check_wilson.cpp"

void check_stars(double beta) {
    Box box(79079, true);
    for (int n = 0; n < 75; ++n) box.sweep(beta);
    constexpr int blocks = 24;
    std::array<std::array<double, 6>, blocks> errors{};
    for (auto& row : errors) {
        box.sweep(beta);
        for (int x = 0; x < sites; ++x) {
            const auto H = box.staple(x, 3, beta);
            const double R = std::sqrt(dot(H, H));
            const auto axis = scale(H, 1/R);
            const double m = std::cyl_bessel_i(2,R)/std::cyl_bessel_i(1,R);
            std::array<Quat,3> s;
            for (int j = 0; j < 3; ++j) s[j] = add(box.upper(x,3,j),box.lower(x,3,j));
            for (int draw = 0; draw < 24; ++draw) {
                const auto u = box.draw(H);
                const auto diff = add(scale(axis,m), scale(u,-1));
                int t = 0;
                for (int j = 0; j < 3; ++j) for (int k = j; k < 3; ++k) {
                    const double longitudinal = dot(s[j],axis)*dot(s[k],axis);
                    const double prediction = beta*beta*((1-m*m-3*m/R)*longitudinal
                        + (m/R)*(dot(s[j],s[k])-longitudinal));
                    row[t++] += (beta*beta*dot(s[j],diff)*dot(s[k],diff)-prediction)/(24*sites);
                }
            }
        }
    }
    double maximum = 0;
    for (int k = 0; k < 6; ++k) {
        double mean = 0, var = 0;
        for (auto& row : errors) mean += row[k]/blocks;
        for (auto& row : errors) var += std::pow(row[k]-mean,2)/(blocks*(blocks-1));
        maximum = std::max(maximum,std::abs(mean)/std::sqrt(var));
    }
    std::cout << "beta " << beta << " maximum absolute block-standardized covariance residual "
              << maximum << "\n";
    if (!(maximum < 6)) throw std::runtime_error("oriented conditional covariance failed");
}

int main() {
    check_stars(.7);
    check_stars(3.5);
    check_stars(12.);
}
