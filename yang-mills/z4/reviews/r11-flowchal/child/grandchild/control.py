import math
s=sum(math.cos(2*math.pi*l/16) for l in range(16))
with open('control.txt','x') as f: f.write(repr(s)+"\n")
print(s)
