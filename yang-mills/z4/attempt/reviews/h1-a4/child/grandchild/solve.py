from decimal import Decimal as D, getcontext
getcontext().prec = 40
def I(n, x):
    h = D(x)/2; h2 = h*h
    t = h**n
    for i in range(2, n+1): t /= i
    s = t; k = 0
    while True:
        t = t*h2/((k+1)*(k+1+n)); k += 1; s += t
        if k > x/2 and t < s*D('1e-45'): break
    return s, k
def control():
    s, k = I(0, 2)  # x=2 -> h=1 ; placeholder, replaced below
    return s
# control: I_0(1), x/2 = 0.5
def I0_1():
    h2 = D('0.25'); t = D(1); s = t; k = 0
    while t > D('1e-50'):
        t = t*h2/((k+1)**2); k += 1; s += t
    return s
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'control':
        c = I0_1(); ref = '1.266065877752008335598244625214717537'
        ok = str(c)[:17] == ref[:17]
        with open('control.txt', 'x') as f: f.write(f"I_0(1)={c}\nref={ref}\nfirst15digits_match={ok}\n")
        print(c, ok)
    else:
        i8, k8 = I(8, 10000); i1, k1 = I(1, 10000)
        lr = (i8/i1).ln(); D_ = lr + (D(8)/8)*(1 + D(8)/10000).ln()
        out = f"I_8(10000)={i8}\nI_1(10000)={i1}\nterms={k8},{k1}\nln(I8/I1)={lr:.25f}\nD={D_:.25f}\nsign={'negative' if D_<0 else 'positive'}\n"
        with open('result.txt', 'x') as f: f.write(out)
        print(out)
