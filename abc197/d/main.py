import math

n = int(input())
x, y = map(int, input().split())
z, w = map(int, input().split())
r = math.hypot((x - z) / 2, (y - w) / 2)
theta = math.atan2((y - w) / 2, (x - z) / 2)
theta += 2 * math.pi / n
p = (x + z) / 2 + r * math.cos(theta)
q = (y + w) / 2 + r * math.sin(theta)
print(p, q)
