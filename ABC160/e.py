x, y, a, b, c = list(map(int, input().split()))
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p_ = sorted(p)[-x:]
q_ = sorted(q)[-y:]
s = p_ + q_ + r
s_ = sorted(s)[-(x + y):]

print(sum(s_))
