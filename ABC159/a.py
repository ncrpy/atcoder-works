n, m = list(map(int, input().split()))


def c2(x):
    return x * (x - 1) // 2


print(c2(n) + c2(m))
