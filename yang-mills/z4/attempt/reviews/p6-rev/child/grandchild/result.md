# Recount of samples in neg:tab-curv vs Observation neg:obs-curv
Source: /home/user/z4-workers/p6-rev/child/input/paper/sec_negative.tex (obs at lines 100-113, table lines 115-145)

## Program 1, periodic rows
- L122: 3^4, beta 4 and 6, "8 each": 2 x 8 = 16
- L123: 3^4, beta 12, 24, 48, "4 each": 3 x 4 = 12
- L124: 4^4, beta 4: 2
- L125: 4^4, beta 6: 2
Program 1 total = 16+12+2+2 = 32

## Program 2, periodic rows
- L126-130: 3^4, beta 4, 6, 12, 24, 48: "not recorded" per row. Caption (L139-140) states 20 periodic samples on 3^4 in total.
- L131: 4^4, beta 6: 2
- L132: 4^4, beta 24: 2
Program 2 total = 20+2+2 = 24

## Sum
32 + 24 = 56. This equals the 56 claimed in the observation (L102-103). The 32/24 split is by program: program 1 contributes 32 explicit counts, and program 2 contributes 20 (caption total) plus 4 explicit = 24.

## Excluded
The open-box rows (L134-136) are not counted: 3 + 3 + 9 = 15. They are non-periodic, and the observation restricts itself to periodic lattices. Their kappa_H is positive at beta >= 6, so including them would break "kappa_H<0 in every sample".

## Caveats
- The 20 for program 2 on 3^4 rests only on the caption, with no per-row breakdown. It cannot be checked against the rows.
- Per-row counts for the 3^4 beta=12,24,48 rows of program 1 are "4 each". Counts were read from the text, not from raw data.
- The caption says the open-box beta=4 count is 6 (beta=4 and 6 together) minus 3 = 3, consistent with L134.
- The per-run range [-2.30,-1.12] is consistent with the rows: min -2.30 at L123, max -1.12 at L128/L129.
