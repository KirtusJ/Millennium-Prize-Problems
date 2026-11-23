# Result

```
control integral = 4.60541
exact I0/I1-2/beta = 0.994146369513
exact I2/I1        = 0.994146369513  (diff 3.66e-15)
sample mean cos    = 0.99414085  SE=4.778e-06
|mean-exact|       = 5.517e-06 = 1.15 SE (predicate <=4 SE)
acceptance rate    = 0.998490 (all 1200000 draws incl. surplus) ; exact = 1.412139 raw; /sqrt2 = 0.998490 (sqrt2 factor from sqrt(t(2-t))=sqrt2*sqrt(t)*sqrt(1-t/2)); agrees
verdict: MET
```

Rerun (new dir needed since files open with 'x'; remove control.txt/result.md first):

`cd /home/user/z4-workers/p1-lower2/child/grandchild && python3 run.py`
