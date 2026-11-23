# Scope of the checks and reproduction

The six Lean declarations cover the exponential inequality behind the inherited deficit and the scalar parts of colour averaging, the quadratic floor and the round-sphere score argument. The native PCP OS guests emitted the prepared input in three sections. The hosted supervisor compiled the assembled Lean 4.19/mathlib source, rejected two false mutations, and read back the worker records. The probabilistic inequalities, gauge quotient, cubical chain construction, Gaussian tensor argument and disk analysis are manuscript proofs. The research workers and challengers supply model-assisted checks. [Lean source](Checks.lean) · [Archive](evidence.zip) · [Verifier](verify.py)

Run with Python 3.10 or newer and NumPy. The numerical programs can run without SciPy. The Fourier code uses a full momentum scan in addition to the symmetry-reduced calculation on the two smallest sides. The geometry test reproduced 22,656 spatial plaquettes over five sizes with no same-colour conflict. The score quadrature reproduced all six spectator ratios. The source literature is cited at the corresponding calculation. A separate systematic correction or retraction search was not performed.

~~~text
python checks.py
python retraction.py
python spectrum.py
python disk.py
python pilot.py
python fixed.py
python verify.py --runtime /path/to/PCP_OS_Python --method /path/to/Method
rustc --edition=2021 -O replicas.rs -o replicas
~~~

For the [unweighted pilot](replicas.md), the arguments are beta, seed, hot flag, burn-in cycles, sample count, side and time period. Each design has four streams indexed by $i=0,1,2,3$, hot flag $i\bmod2$ and seed equal to the base below plus $7919i$.

|Archive prefix|Beta|Base seed|Burn|Samples|Side, period|
|---|---:|---:|---:|---:|---|
|b0|0|651731|4|96|6,12|
|haar2|0|1951711|0|384|6,12|
|b3.276133577|3.276133577|651731|192|96|6,12|
|N8|3.399810242|1365713|192|96|8,16|

For the [fixed-skeleton pilot](fixed.md), prepend the mode word and append the sign. The four initial designs used 288 discarded sweeps and 144 samples. In table order the base seeds are 1600451, 1700451, 1800451 and 1900451; add $7919i$ and use the same hot flag as above. Illustrative first commands are

~~~text
./replicas 3.276133577 651731 0 192 96 6 12
./replicas fixed 3.276133577 1700451 0 288 144 6 12 -1
~~~

The independent side-eight sign repeat used base seeds 2100451 (+) and 2200451 (−), 864 discarded sweeps and 256 samples at the same coupling and temporal extent. The same stream offsets and hot flags apply.

The Rust sampler includes the existing Wilson heat bath and quaternion code directly. Each fixed-skeleton path checks its two prescribed coarse holonomies at every observation. The archived streams preserve full run rows. The stopped high-coupling run with the original rejection envelope is retained separately in the evidence, excluded from inference. The opaque worker and native attribution fields record the host's observations and declared roles.
