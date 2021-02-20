x = [int(s) for s in input()]
l = len(x)
d = max(x)
m = int(input())
if l > 1:
    max_n = int((m / x[0]) ** (1 / (l - 1))) + 1
else:
    print(0 if m < d else 1)
    exit()
ans = 0
n = max_n
k = 1e19
while k > m:
    n -= 1
    k = sum([n ** i * x[l - 1 - i] for i in range(l)])
print(max(0, n - d))
