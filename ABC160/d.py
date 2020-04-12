import collections

n, x, y = list(map(int, input().split()))
lst = [
    min(abs(i - j), (abs(i - x) + abs(j - y) + 1))
    for j in range(2, n + 1)
    for i in range(1, j)
]
dic = collections.Counter(lst)
for k in range(1, n):
    print(dic[k])
