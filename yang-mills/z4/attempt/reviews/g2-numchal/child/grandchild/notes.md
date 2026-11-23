E0 = 3.350533 (sine-DVR radial, Legendre even-l angular, own Lanczos). Table in results_*.txt.
L=8 N=24 nl=4: 3.35065828 | nl=8: 3.35053308 | N=32 nl=4: 3.35065828 | N=32 nl=8: 3.35053307
L=6 N=32 nl=8: 3.35053307 | L=10 N=32 nl=8: 3.35053307 (res 6e-6, P2 fails marginally; Lanczos 600 it cap)
Control: 1.5000000000000158 (control.txt). Runs L=10 N=40, nl=12/14 killed for time; not done.
Rerun: python3 e0.py control; python3 e0.py L N nl (results files are mode 'x'; delete to rerun).
