MOD = 998244353

n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
s = 0
for i in range(n):
    s += a[i] * pow(2, i, MOD)

for ai in a:
    s -= ai
    if s % 2:
        s += MOD
    s //= 2
    ans += ai * (ai + s)
    ans %= MOD

print(ans)
