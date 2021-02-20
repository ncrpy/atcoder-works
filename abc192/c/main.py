n, k = map(int, input().split())


def func(x):
    s = sorted(str(x))
    g1 = int("".join(reversed(s)))
    g2 = int("".join(s))
    print(g1, g2)
    return g1 - g2


fi = n
for i in range(k):
    fi = func(fi)
    if fi == 0:
        break
print(fi)
