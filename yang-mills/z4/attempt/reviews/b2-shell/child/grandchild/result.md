# Shell weights, axis 1

Method: classify sites by j = number of the other two coordinates whose distance equals r; axis 1 gets 1/(1+j). Distance multiplicities: d=0 -> 1 residue, 0<d<m -> 2, d=m -> 1.

- m=1, w_1 (r=m): 1 + 2*(1/2) + 1/3 = 7/3 (claim 7/3) MATCH
- m=2, w_1 (interior): 2 + 8/2 + 8/3 = 26/3 (claim 26/3) MATCH
- m=2, w_2 (r=m): 9 + 6/2 + 1/3 = 37/3 (claim 37/3) MATCH

Confirmed by an independent Fraction-based enumeration: 7/3, 26/3, 37/3.
