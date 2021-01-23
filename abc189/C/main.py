#!/usr/bin/env python3


def main():
    n = int(input())
    a = list(map(int, input().split())) + [0]
    l = [(0, -1)]
    ans = 0
    for i in range(n + 1):
        while l[-1][0] > a[i]:
            b, j = l.pop()
            ans = max(ans, (i - l[-1][1] - 1) * b)
        l.append((a[i], i))
    print(ans)


if __name__ == "__main__":
    main()
