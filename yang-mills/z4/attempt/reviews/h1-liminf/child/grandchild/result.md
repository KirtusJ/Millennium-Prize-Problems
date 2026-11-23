# T92 results

Control I1(1)/I0(1) = 0.446389965897 (known 0.446390)

I0(10)=2815.716628466254 (ref 2815.716628466254)
I1(10)=2670.988303701255 (ref 2670.988303701255)


## Claim (C): -ln kappa_n, kappa_n=I_{n+1}/I_1

beta=1000 n=1: value=0.0015007501869357 lower=0.0014977533699451 upper=0.002 slack_lower(v-lo)=0.0000029968170 slack_upper(hi-v)=0.00049924981 ok=True
beta=1000 n=2: value=0.0040019988268211 lower=0.0039900249376559 upper=0.005 slack_lower(v-lo)=0.000011973889 slack_upper(hi-v)=0.00099800117 ok=True
beta=10000 n=1: value=0.00015000750018744 lower=0.00014997750337449 upper=0.0002 slack_lower(v-lo)=2.9996813e-8 slack_upper(hi-v)=0.000049992500 ok=True
beta=10000 n=2: value=0.00040001999883268 lower=0.00039990002499375 upper=0.0005 slack_lower(v-lo)=1.1997384e-7 slack_upper(hi-v)=0.000099980001 ok=True

## Claim (B): r_nu(x)=I_{nu+1}/I_nu <= x/(nu+1/2+sqrt((nu+1/2)^2+x^2))

nu=0 x=1000: r=0.99949987487480 bound=0.99950012499999 slack_abs=2.5012519e-7 slack_rel=2.5025034e-7 ok=True
nu=0 x=10000: r=0.99994999874987 bound=0.99995000125000 slack_abs=2.5001250e-9 slack_rel=2.5002500e-9 ok=True
nu=1 x=10000: r=0.99985000375038 bound=0.99985001125000 slack_abs=7.4996249e-9 slack_rel=7.5007500e-9 ok=True
nu=2 x=10000: r=0.99975001875188 bound=0.99975003125000 slack_abs=1.2498124e-8 slack_rel=1.2501249e-8 ok=True
nu=3 x=10000: r=0.99965004375437 bound=0.99965006125000 slack_abs=1.7495623e-8 slack_rel=1.7501748e-8 ok=True

Not verified: only these finite cases; no proof; Decimal prec 60 power series only (single method, series truncated at rel 1e-55); no independent continued-fraction cross-check; other nu/x untested.
