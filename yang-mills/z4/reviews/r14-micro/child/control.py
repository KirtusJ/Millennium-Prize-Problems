"""Control. Predicate: value = 12*0.1905/(6*0.3690)-1 in percent, 2 decimals, equals 3.25 (arithmetic: 2.286/2.214-1=0.03252)."""
v=round((12*0.1905/(6*0.3690)-1)*100,2)
assert v==3.25
with open("control.txt","x") as f: f.write(f"{v:.2f}\n")
