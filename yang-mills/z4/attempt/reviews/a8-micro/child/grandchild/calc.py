R0 = [3.751e-2, 3.615e-2, 3.233e-2]
R1 = [1.012e-2, 1.166e-2, 1.245e-2]
S = [0.3690, 0.2660, 0.1905]
lines = []
for k in range(3):
    q = R1[k] / R0[k]
    xi = 1 / (3.74 * S[k])
    lines.append(f"k={k+1} q={q:.3f} xi={xi:.3f}")
out = "\n".join(lines) + "\n"
with open("result.txt", "x") as f:
    f.write(out)
print(out, end="")
