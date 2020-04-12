def c2(x):
    return x * (x - 1) // 2


n = int(input())
a = list(map(lambda i: int(i) - 1, input().split()))
# b = list(a.count(i) for i in range(n))
# c = list(c2(b[i]) for i in range(n))
# d = list(c2(b[i] - 1) for i in range(n))
s = sum(c2(a.count(i)) for i in range(n))

# for k in range(n):
#     i = a[k]
#     ans = s - c[i] + d[i]
#     print(ans)
for i in a:
    print(s - a.count(i) + 1)
