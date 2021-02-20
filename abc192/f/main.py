n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 10 ** 18
for m in range(1, n + 1):
    dp = [[[-1] * m for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        dp[i][0][0] = 0
        for j in range(m):
            for k in range(m):
                k_ = (k + a[i]) % m
                if dp[i][j][k] == -1:
                    dp[i + 1][j + 1][k_] = dp[i][j + 1][k_]
                    continue
                dp[i + 1][j + 1][k_] = max(dp[i][j + 1][k_], dp[i][j][k] + a[i])
    d = dp[-1][-1][x % m]
    if d >= 0:
        ans = min(ans, (x - d) // m)

print(ans)
