"""Step 0 control. Predicate: I_0(1) series matches 1.266066 to 6 decimals."""
s=0.0;t=1.0;k=0
while t>1e-20:
    s+=t;k+=1;t*=0.25/(k*k)
with open("control.txt","x") as f: f.write("%.6f\n"%s)
print("%.6f"%s, "PASS" if "%.6f"%s=="1.266066" else "FAIL")
