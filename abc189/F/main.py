#!/usr/bin/env python3

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (n+m)
    dp[0] = 1
    for i in range(1, m+1):
        dp[i] = sum(dp[:i])

    for i in range(n):
        dp[i+1] =


if __name__ == '__main__':
    main()
