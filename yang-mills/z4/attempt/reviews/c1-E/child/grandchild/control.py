import itertools
n=sum(1 for s in itertools.product([1,-1],repeat=4) if sum(s)==0)
open('control.txt','x').write(f"{n}\n")
print(n)
