#!/usr/bin/env python3


def main():
    n, x = map(int, input().split())
    x *= 100
    alc = 0
    cnt = 0
    for i in range(1, n + 1):
        v, p = map(int, input().split())
        alc += v * p
        if alc > x:
            print(i)
            break
    else:
        print(-1)


if __name__ == "__main__":
    main()
