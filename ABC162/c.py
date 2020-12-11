from math import gcd

k=int(input())
l = [[gcd(i,j) for j in range(1, k+1)] for i in range(1, k+1)]

ans = 0
for i in range(k):
    for j in range(k):
        n = l[i][j]
        ans += sum(l[n-1])

print(ans)
