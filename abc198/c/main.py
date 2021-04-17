import math

r, x, y = map(int, input().split())
d2 = x ** 2 + y ** 2
a2 = d2 / (r ** 2)
a = math.sqrt(a2)
if a < 1:
    a = 2
print(math.ceil(a))
