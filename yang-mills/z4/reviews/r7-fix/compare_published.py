"""R2: compare the numbers common to v1's published result and v2's result, value by value.

PREDICATES (fixed before the first run)
 C1 every leaf path present in both files, except the key "program" (whose value names the
    program and must differ), has an identical JSON value (exact string equality; tolerance
    zero, because both programs print the same mpmath expressions at the same precision).
 C2 the number of compared leaves equals the number of leaves of the published file minus 1
    (only "program" excluded), i.e. v2 drops nothing that v1 published.
 C3 the published file is unchanged: sha256 = 24939c8dd0ae5925e27abe30b45936a6a0d38ae9456e326f9a3ba476465a9d0f.
OUTPUT compare_published_result.json, refused if it exists. Exit 0 iff C1, C2, C3 met.
RERUN  python -I compare_published.py input/two_dim_control_result.json two_dim_control_v2_result.json
"""
import hashlib, json, os, sys
OUT = "compare_published_result.json"
if os.path.exists(OUT):
    sys.exit("result exists; refusing to overwrite")
pub, new = sys.argv[1], sys.argv[2]
def leaves(x, path=""):
    if isinstance(x, dict):
        for k in sorted(x): yield from leaves(x[k], path + "/" + str(k))
    elif isinstance(x, list):
        for i, v in enumerate(x): yield from leaves(v, path + "[%d]" % i)
    else:
        yield path, json.dumps(x)
A = dict(leaves(json.load(open(pub, encoding="utf-8"))))
B = dict(leaves(json.load(open(new, encoding="utf-8"))))
common = [p for p in A if p in B and p != "/program"]
diffs = [(p, A[p], B[p]) for p in common if A[p] != B[p]]
only_pub = [p for p in A if p not in B]
sha = hashlib.sha256(open(pub, "rb").read()).hexdigest()
c1 = not diffs; c2 = len(common) == len(A) - 1 and not only_pub
c3 = sha == "24939c8dd0ae5925e27abe30b45936a6a0d38ae9456e326f9a3ba476465a9d0f"
r = {"published_leaves": len(A), "v2_leaves": len(B), "compared": len(common), "differences": diffs,
     "only_in_published": only_pub, "v2_only_leaves": len([p for p in B if p not in A]),
     "published_sha256": sha, "C1": c1, "C2": c2, "C3": c3}
with open(OUT, "x", encoding="utf-8", newline="\n") as f:
    json.dump(r, f, indent=1); f.write("\n")
print(json.dumps({k: v for k, v in r.items() if k != "differences"}), "differences:", len(diffs))
sys.exit(0 if c1 and c2 and c3 else 1)
