# notes T64
- control.txt = 0 (slice 3 -> 0 on ring of 4). Matches expectation (3+1 mod 4).
- Hand derivation: (theta tau F)(U)=F(U_{-s-1}) = (tau^-1 theta F)(U); expect C3 to hold. Supp(tau F)=supp+1 (F reads slice s of shifted U = U_{s+1}).
- ran check.py N=6 via pcp check; see result_N6.txt (all MET expected; verify)
