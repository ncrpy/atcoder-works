a, b, c = map(int, input().split())
a %= 10
b %= 4
if b == 0 or (b == 2 and c > 1):
    d = 4
elif b == 1:
    d = 1
elif b == 2 and c == 1:
    d = 2
else:
    d = (b ** (c % 2)) % 4
print((a ** d) % 10)
