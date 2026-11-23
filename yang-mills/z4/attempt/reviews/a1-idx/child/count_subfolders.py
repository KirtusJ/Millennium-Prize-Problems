"""Predicate: count directories directly inside target (hidden included, files excluded). Expected 13 (control.txt)."""
import os
t="/home/user/z4-workers/a1-idx/repo/yang-mills/transfer-operator"
print(sum(os.path.isdir(os.path.join(t,e)) for e in os.listdir(t)))
