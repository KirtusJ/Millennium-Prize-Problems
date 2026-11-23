Control: trapezoid sin on [0,pi], N=2000 -> 1.9999996 (control.txt: 2.000000).
Method: ive1(z)=mean over N equispaced nodes on full period of exp(z(cos t-1))cos t (periodic trapezoid); N doubled until |N vs 2N|<1e-15 (start 1024). Power series cross-check for z<=20.
Grid: 30 log pts 1e-6..0.5, 50 linear 0.5..100, plus 100,200,300,500,700 and 13 linear 100..700 (91 unique pts).
Predicate: margin>=-1e-12 at all points. Large z use scaled form with -0.5*exp(-z).
Result: see results.txt. Margin is positive everywhere; min at z=700 (~2.7e-6), decaying like ~1/(8z sqrt(2 pi z)), so it tends to 0 but stays positive.
