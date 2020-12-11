n, k = list(map(int, input().split()))
l = [0 for i in range(k)]
ans = 0
M = 10**9 + 7

# def dev(n):
#     dl = []
#     for i in range(1, int(n**0.5)+1):
#         if n % i == 0:
#             dl.append(i)
#             if i != n // i:
#                 dl.append(n//i)
#     dl.sort()
#     return dl

for i in range(k, 0, -1):
#     a=k//i
#     b=a**n%M
    b=pow(k//i, n, M)
    for j in range(i*2, k+1, i):
        b -= l[j-1]
    l[i-1] = b%M

for i in range(1, k+1):
    ans+=i*l[i-1]

print(ans%M)
