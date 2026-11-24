# Results

## Control
E[a^4] for Haar SU(2)=S^3: 3/(n(n+2)), n=4 -> 0.125000 (control.txt). MC check: 0.125244

## MC estimates (N=400000, seed 12345)

|quantity|MC|SE|exact (indep Haar)|z|
|-|-|-|-|-|
|E[f1^2]|0.250770|0.000396|0.250000|1.94|
|E[f4^2]|0.062408|0.000131|0.062500|-0.71|
|E[spread]|0.750273|0.000242|0.750000|1.13|

## Exact derivations (g_k independent Haar)
- f1=Re(i g1)=-b1; E[b^2]=1/4 -> E[f1^2]=1/4.
- f4=-mean of 4 indep b's: Var=(1/16)*4*(1/4)=1/16.
- E|gbar|^2=(1/16)(4*1+cross terms 0)=1/4 -> E[spread]=3/4.

## Agreement
MC agrees with the independent-Haar values within 3 sigma: YES

Correlation of b-components of g1..g4 (diagnostic):
```
[[ 1.0e+00  2.0e-04  2.0e-04 -3.0e-03]
 [ 2.0e-04  1.0e+00 -1.8e-03  1.5e-03]
 [ 2.0e-04 -1.8e-03  1.0e+00 -2.1e-03]
 [-3.0e-03  1.5e-03 -2.1e-03  1.0e+00]]
```
