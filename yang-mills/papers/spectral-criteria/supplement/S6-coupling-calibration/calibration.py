"""SU(2), c_t=1, Tables 2 and 3 of Francesconi et al., arXiv:2003.13734.
Columns are (Wilson beta, mean g_SF^2(L)). Use the mean of direct and reverse.
"""
TABLE = {
    5: [(3.4564,2.037934),(3.1898,2.390472),(2.9568,2.831995),(2.7124,3.560933)],
    6: [(3.5408,2.032526),(3.2751,2.381590),(3.0379,2.82826),(2.7938,3.54969)],
    7: [(3.6045,2.03583),(3.3428,2.37988),(3.0961,2.84686),(2.8598,3.54741)],
    8: [(3.6566,2.04153),(3.4009,2.37828),(3.1564,2.83853),(2.9115,3.56357)],
    10: [(3.7425,2.05079),(3.5000,2.37012),(3.2433,2.85316),(3.0071,3.54890)],
}
TARGET = 2.38

def tune(points, u=TARGET, inverse=True):
    for (b0,u0),(b1,u1) in zip(points, points[1:]):
        if u0 <= u <= u1:
            f = (1/u - 1/u0)/(1/u1 - 1/u0) if inverse else (u-u0)/(u1-u0)
            return b0 + f*(b1-b0)
    raise ValueError("outside interpolation bracket")

if __name__ == "__main__":
    for n, points in TABLE.items():
        print(n, *(f"{v:.9f}" for v in (tune(points), tune(points,inverse=False),tune([points[0],points[2]]))))
