"""Compare local interpolants for Ramos, arXiv:1409.1445, Table 3."""
from math import isclose

# N, (u(8), u(10), u(12)), and their published marginal standard errors.
ROWS = (
    (10, (.6455, .48769, .39194), (.0010, .00076, .00060)),
    (18, (.6693, .49945, .39974), (.0010, .00076, .00059)),
    (20, (.6741, .50340, .40162), (.0011, .00076, .00060)),
    (36, (.6987, .51809, .41078), (.0011, .00085, .00063)),
)
TARGET = .55


def mix(a, b, w):
    return a + (b - a) * w


def tuned_beta(u8, u10, u):
    # Assume inverse coupling is linear in beta on this small interval.
    return mix(8, 10, (1 / u - 1 / u8) / (1 / u10 - 1 / u8))


def main():
    tuned = []
    for n, (u8, u10, u12), (s8, s10, s12) in ROWS:
        assert u10 + 3 * s10 < TARGET < u8 - 3 * s8
        assert isclose(tuned_beta(u8, u10, u8), 8)
        assert isclose(tuned_beta(u8, u10, u10), 10)
        beta = tuned_beta(u8, u10, TARGET)
        linear = mix(8, 10, (TARGET - u8) / (u10 - u8))
        heldout = 1 / mix(1 / u8, 1 / u12, .5)
        # First-order propagated scatter, assuming independent beta ensembles.
        s_pred = .5 * heldout**2 * ((s8 / u8**2)**2 + (s12 / u12**2)**2)**.5
        pull = (heldout - u10) / (s_pred**2 + s10**2)**.5
        assert 8 < beta < linear < 10
        print(f'{n:2}  {beta:.5f}  {linear:.5f}  {heldout-u10:+.6f}  {pull:+.2f}')
        tuned.append(beta)
    ratio = (tuned[0] / tuned[-1])**(1 / 3)
    scalar = 2.269639 * TARGET**(1 / 3)
    correction = -.7975278 * TARGET**(2 / 3)
    print(f'bare endpoint ratio {ratio:.6f}')
    print(f'scalar leading {scalar:.6f}, second term {correction:.6f}, sum {scalar+correction:.6f}')


if __name__ == '__main__':
    main()
