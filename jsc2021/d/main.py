n, p = map(int, input().split())
mod = 10 ** 9 + 7
print((pow(p - 2, n - 1, mod) * (p - 1)) % mod)
