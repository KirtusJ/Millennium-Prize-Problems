"""Differentiate trial functions in the original five flat coordinates."""
import mpmath as mp


def evaluate(radius, distance, shape, corrected):
    zero = mp.airyaizero(1)
    z0 = radius + distance
    entries = tuple(mp.mpf(i)/mp.sqrt(z0) for i in shape)
    u0 = sum(i*i for i in entries)
    x0 = distance + mp.sqrt(radius**2-u0)
    point = (x0, *entries)

    def trial(x, a, b, c, d):
        u = a*a+b*b+c*c+d*d
        z = x + radius - mp.sqrt(radius**2-u)
        arg = 2*(z-radius) + zero
        f = mp.airyai(arg)
        if corrected:
            f -= (1+2*z/radius)/(4*z)*(u-1/z)*2*mp.airyai(arg, 1)
        return z*mp.exp(-z*u)*f

    def jacobian_root(x, a, b, c, d):
        return mp.sqrt(x**4-x*x*(a*a+b*b+c*c+d*d)+(a*d-b*c)**2)

    def laplacian(function):
        return sum(mp.diff(lambda t: function(*point[:j], t, *point[j+1:]), val, 2)
                   for j,val in enumerate(point))

    a,b,c,d = entries
    potential = 2*x0*x0*u0 + 2*(a*d-b*c)**2 + laplacian(jacobian_root)/(2*jacobian_root(*point))
    residual = -laplacian(trial)/2 + (potential-4*radius+2*zero)*trial(*point)
    g = z0*mp.exp(-z0*u0)
    predicted = (1+2*z0/radius)*(u0-1/z0)*2*mp.airyai(2*distance+zero, 1)
    return residual/g, predicted


if __name__ == '__main__':
    mp.mp.dps = 40
    for radius in (32,64,128,256):
        for distance, shape in [(1,(1,.5,0,-.5)), (2,(.5,-.5,.25,0))]:
            raw, predicted = evaluate(radius, distance, shape, False)
            fixed, _ = evaluate(radius, distance, shape, True)
            print(radius, distance, *(mp.nstr(v, 7) for v in
                                      (radius**2*(raw-predicted), radius**2*fixed)))
            assert abs(radius**2*(raw-predicted)) < 3
            assert abs(radius**2*fixed) < 3
