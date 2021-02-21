k = int(input())
ans = 0
for i in range(1, k + 1):
    for j in range(1, k // i + 1):
        ans += k // (i * j)
print(ans)
