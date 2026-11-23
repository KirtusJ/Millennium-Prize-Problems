# Homology of the lattice shell S_N in Z^4 (N=1,2)
Control: sites of Z^4 with sup-norm exactly 1 = 80 (control.txt).

| | N=1 | N=2 |
|---|---|---|
| V | 80 | 544 |
| E | 208 | 1568 |
| F | 192 | 1536 |
| components c | 1 | 1 |
| E-V+1 | 129 | 1025 |
| rank d2, GF(2) | 129 | 1025 |
| rank d2, mod 2^31-1 (=Q unless that prime divides an elementary divisor) | 129 | 1025 |
| rank by integer elimination with +-1 pivots | 129 | 1025 |
| b1 GF(2) / Q / Z-elim | 0 / 0 / 0 | 0 / 0 / 0 |

d1*d2 = 0 verified. For (d), every pivot in the integer elimination was +-1 and it exhausted the matrix, so all nonzero elementary divisors are 1: H_1 = 0 over Z, with no torsion, for **N=1 and N=2**. The 2-skeleton of each shell is homologically simply connected (H_1 only; I did not check pi_1).

Failed predicates: none. (Predicates P0-P6 are in the docstring of shell_h1.py. The tolerance is none: all arithmetic is exact integer, and the mod-p rank is only a cross-check.)

Not checked: pi_1 itself, H_2 or higher, and exact Q-rank by rational elimination. The Q conclusion rests on the Z unit-pivot elimination, which is exact. Plaquettes inside a face x_i=+-N are included, as the task states. I did not separately enumerate which plaquettes "wrap" an edge.

Delegated check: a sub-agent in grandchild/ had control Z^3 sup-norm-1 sites = 26 (correct). It independently reported N=1: V=80, E=208, F=192, c=1, r=129, b1=0 over GF(2). It reported no failed predicates. I reread its code output and reran its shell.py in a copy (/tmp/gc), and the rerun gave the same numbers. It is registered in the PCP register as check grandchild_rerun. Its result_raw.txt uses mode 'x', so a rerun in place needs the old file removed.

Rerun (from this directory; res_N.txt are mode 'x', so delete them first):
    rm -f res_1.txt res_2.txt; python3 shell_h1.py 1; python3 shell_h1.py 2
    (cd grandchild && cp -r . /tmp/gc2 && cd /tmp/gc2 && rm -f result_raw.txt && python3 shell.py)
PCP: $P check --ws pcp --name shell_N1 --expect-exit 0 -- python3 shell_h1.py 1  (likewise N2)
