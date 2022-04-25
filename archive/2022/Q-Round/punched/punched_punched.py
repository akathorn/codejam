# fmt: off
p = print
r = input

for t in range(int(r())):
    p(f"Case #{t+1}:")
    R, C = map(int, r().split())
    o, e = "+-" * C + "+", "|." * C + "|"
    p(".." + o[2:], ".." + e[2:],
    *[o, e] * (R - 1), o, sep="\n")