"""Sign correction: k = 4 dS0/deta is NEGATIVE (S0 depends on pi-2eta). sf1loop.py used +|k| (own defect, found by grandchild).
Predicate: c1_corrected = -dG_rich/k_signed, k_signed==-result_R4.k to 1e-12."""
import json
r=json.load(open("result_R4.json")); k=-r["k"]
out={"k_signed":k,"c1_rich":-r["dG_rich"]/k,"c1_h01":-r["dG_h01"]/k,"c1_h02":-r["dG_h02"]/k}
with open("result_R4_signfixed.json","x") as f: json.dump(out,f,indent=1)
print(out)
