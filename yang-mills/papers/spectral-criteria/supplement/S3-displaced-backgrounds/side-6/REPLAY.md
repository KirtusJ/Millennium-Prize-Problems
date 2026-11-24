# REPLAY — z1-mix6 (side 6, time period 12, beta = 3.276133577)

All commands from `/home/user/z4-workers/z1-mix6`. Results directories must not exist beforehand (files are created with create_new / mode "x").

## Build
```
mkdir -p build/g4/full-attempt/two-site-gap build/src/ctl
cp /home/user/Millennium-Prize-Problems/yang-mills/g4/full-attempt/two-site-gap/wilson_mc.rs build/g4/full-attempt/two-site-gap/   # sha256 5366fd10de5e8588ac538a53561170a9abd999c07c8722e6e2fd42d5a86ff75f
cp g4/full-complement/replicas.rs build/src/ctl/replicas.rs                                                                # sha256 b77a90246367084c367b7091903dfb91feeab1450e55c568e70c59652a35f67a (unchanged)
cd build
rustc --edition 2021 -O -o g4_replicas src/ctl/replicas.rs      # G4's sampler; edition 2015 (rustc default) fails to compile it
rustc --edition 2021 -O -o z1m6 src/mine/z1m6.rs               # own sampler (rustc 1.97.0)
cd ..
```

## Control (G4 sampler unchanged)
`python3 ctl.py` — runs, for i = 0..3, hot = i%2:
```
build/g4_replicas fixed 3.276133577 <base+7919 i> <i%2> 288 144 6 12 -1
```
with base 1700451 (G4's seeds; results/ctl_g4seeds) and base 7700451 (new; results/ctl_newseeds). Summary results/ctl_summary.json.

Cross-check of own sampler (P4): 
```
build/z1m6 fixed 3.276133577 1700451 0 288 144 6 6 12 skeletons/d0.txt results/p4/s0
build/z1m6 fixed 3.276133577 1708370 1 288 144 6 6 12 skeletons/d0.txt results/p4/s1
```
first five columns byte-identical to results/ctl_g4seeds/minus6-s{0,1}.csv.

## Own sampler
```
build/z1m6 fixed <beta> <seed> <hot 0|1> <burn sweeps> <measurements> <spacing sweeps> <side> <time period> <skeleton file> <output prefix>
build/z1m6 gen   <beta> <seed> <hot 0|1> <burn cycles> <count> <gap cycles> <side> <time period> <output prefix>
```
Outputs: `<prefix>.csv` columns single, average, spread, j_single, j_average (B = full xz holonomy, G4's definition), single_tl, average_tl, j_single_tl, j_average_tl (B = normalised traceless part of the xz holonomy), mean_tries (pair proposals per accepted pair draw); `<prefix>.colours.csv` per-measurement (f'-f'')^2/2 for each of 24 colours and 4 tests (J = mean over colours); `<prefix>.meta.txt` arguments, min angle from -I over the 81 coarse spatial faces, all 81 angles.
Colour index = 8*plane + px + 2*py + 4*pz, plane 0 = xy, 1 = xz, 2 = yz, (px,py,pz) = parity of the base site.

## Skeletons
`python3 mkskel.py` (d0, d0.5, d1, d2) and `python3 mkskel_d4.py` (d4, extra): W_delta = (-cos d, 0, 0, sin d) on the y-link at site 2 = (2,0,0), B = (0,1,0,0) on the z-link at site 2, every other frozen link = I.
`python3 clear.py`: `build/z1m6 gen 3.276133577 4100001 1 300 60 10 6 12 results/gen/chain` and selection (theta = pi/4 rule; kept chain.skel0, skel2, skel4).

## Production
Each `python3 run.py <tag> <skeleton> <base>` runs 8 streams `build/z1m6 fixed 3.276133577 <base+7919 i> <i%2> 576 576 6 6 12 <skeleton> results/<tag>/s<i>`; `run_big.py` the same with 24 streams and 1152 measurements. Exact command lines are in results/<tag>/commands.txt.

| tag | skeleton | base seed | design |
|---|---|---|---|
| d0 | skeletons/d0.txt | 3100001 | 8 x 576 |
| d0.5 | skeletons/d0.5.txt | 3200001 | 8 x 576 |
| d1 | skeletons/d1.txt | 3300001 | 8 x 576 |
| d2 | skeletons/d2.txt | 3400001 | 8 x 576 |
| clear0 | results/gen/chain.skel0.txt | 5100001 | 8 x 576 |
| clear2 | results/gen/chain.skel2.txt | 5200001 | 8 x 576 |
| clear4 | results/gen/chain.skel4.txt | 5300001 | 8 x 576 |
| L-d0 | skeletons/d0.txt | 6100001 | 24 x 1152 |
| L-d0.5 | skeletons/d0.5.txt | 6200001 | 24 x 1152 |
| L-d1 | skeletons/d1.txt | 6300001 | 24 x 1152 |
| L-d2 | skeletons/d2.txt | 6400001 | 24 x 1152 |
| L-d4 | skeletons/d4.txt | 6500001 | 24 x 1152 |

Reduction: `python3 reduce.py <tag> ...` -> results/<tag>/summary.json.
