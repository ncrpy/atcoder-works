a, b, c = list(map(int, input().split()))
from math import sqrt
if sqrt(a)+sqrt(b)<sqrt(c):
    print('Yes')
else:
    print('No')
