#!/usr/bin/env python3


def main():
    n = int(input())
    ans = 1
    for i in range(1, n + 1):
        if input() == "OR":
            ans = ans * 2 + (2 ** i - ans)
    print(ans)


if __name__ == "__main__":
    main()
