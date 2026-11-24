# REPLAY (z1-mix8, side 8, time period 16, beta 3.399810242)

All commands from /home/user/z4-workers/z1-mix8. Result files are created with mode "x" (create_new): remove or rename
an output directory before replaying into it, or compare against a fresh copy elsewhere.

## Build
```
mkdir -p build/g4/full-complement build/g4/full-attempt/two-site-gap build/g4/mix8
cp g4/full-complement/replicas.rs build/g4/full-complement/            # sha256 b77a90246367084c367b7091903dfb91feeab1450e55c568e70c59652a35f67a (unchanged)
cp /home/user/Millennium-Prize-Problems/yang-mills/g4/full-attempt/two-site-gap/wilson_mc.rs build/g4/full-attempt/two-site-gap/   # sha256 5366fd10de5e8588ac538a53561170a9abd999c07c8722e6e2fd42d5a86ff75f
(cd build/g4/full-complement && rustc --edition=2021 -O replicas.rs -o replicas)       # rustc 1.97.0
(cd build/g4/mix8 && rustc --edition=2021 -O mix8.rs -o mix8)
```
mix8.rs = G4's replicas.rs verbatim plus new modes `mix`, `clear`, `gen` (functions inserted before `pub fn run`; the
`fixed` path, `draw`, `colours`, `conditional_sweep`, `face` are untouched). In `mix` with delta=0 its first five
output columns are byte-identical to G4's `fixed ... -1` for the same seed (checked on 4 streams).

Note: bit-for-bit replay of G4's ARCHIVED csv files is NOT obtained on this machine (first rows agree to ~1e-6,
trajectories then diverge; floating-point/libm difference). Replays on the same build are deterministic.

## Control
```
python3 control.py          # G4 binary, seeds 1800451+7919 i, hot=i%2, 288 burn, 144 samples, side 8, period 16, sign -1
python3 control_reduce.py
```
## Perturbed backgrounds (8 streams each)
`python3 run_mix.py` runs, for k=0..3, c in (0, 0.5, 1, 2), delta=c/3.399810242, i=0..7:
```
build/g4/mix8/mix8 mix 3.399810242 <3000451+100000*k+7919*i> <i%2> 864 512 8 16 <delta>
```
(delta printed with Python repr: 0, 0.14706703151346057, 0.29413406302692113, 0.5882681260538423) -> results/mix/d<k>-c<c>-s<i>-<hot|cold>.csv (+ .meta: background, smallest angle, command)
## Clear backgrounds
`python3 run_clear.py`:
```
build/g4/mix8/mix8 gen 3.399810242 4000451 200 30 10 8 16 results/clear/skeletons/chainA
build/g4/mix8/mix8 gen 3.399810242 4100451 200 30 10 8 16 results/clear/skeletons/chainB
build/g4/mix8/mix8 clear 3.399810242 <5000451+100000*m+7919*i> <i%2> 864 256 8 16 <skeleton file>   (m = kept skeleton 0..2, i=0..7)
```
selection in results/clear/selection.json.
## Reduction
```
python3 reduce.py <label> <csv files...>
python3 analyze_all.py <new tag>      # writes results/summary_<tag>.json
```
Output columns: single=Re(Bhat g1), average=Re(Bhat gbar), spread=1-|gbar|^2, j_single, j_average (two-copy loss averaged over 24
colours, as G4), single_raw/average_raw/j_*_raw (B = raw xz holonomy, G4's code literally; identical for fixed backgrounds since
the holonomy is i), c<k>_single / c<k>_average = (fA-fB)^2/2 for colour k (k = 8*o + px + 2py + 4pz; o 0=xy,1=xz,2=yz); mean_k c_k = j.
## Child rerun
```
cd child && rustc -O -o mc_rerun mc.rs && ./mc_rerun 3.276133577 4 288 500 6 2026 rerun_main.csv && python3 analyze.py rerun_main.csv
```
