n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
x = sorted(list(a ^ b))
print(" ".join([str(y) for y in x]))
