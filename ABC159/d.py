# def c2(x):
#     return x * (x - 1) // 2

n = int(input())
a = list(map(lambda i: int(i) - 1, input().split()))
b = list(a.count(i) for i in range(n))
c2 = list((x * (x - 1) // 2) for x in range(n))
# c = list(c2(b[i]) for i in range(n))
# d = list(c2(b[i] - 1) for i in range(n))
c = list(c2[i] for i in b)
d = list(c2[i - 1] for i in b)

s = sum(c)
# for k in range(n):
#     i = a[k]
#     ans = s - c[i] + d[i]
#     print(ans)
for i in a:
    print(s - c[i] + d[i])
