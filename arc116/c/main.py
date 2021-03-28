import numpy as np

n, m = map(int, input().split())
# v1 = [1] * m
# for _ in range(1, n):
#     v2 = [sum(v1[i :: i + 1]) % 998244353 for i in range(m)]
#     v1 = v2
# print(sum(v1) % 998244353)
# arr = np.array([[0 if i % j else 1 for i in range(1, m + 1)] for j in range(1, m + 1)])
# arr = np.ones((m, m), dtype=int)
arr = [[1] * m for _ in range(m)]
for i in range(1, m + 1):
    for j in range(1, m + 1):
        if i % j:
            arr[i - 1][j - 1] = 0
    print(i)
vec = np.ones(m, dtype=int)
# A = np.linalg.matrix_power(arr, n - 1)
# ans = np.dot(A, vec)
# print(sum(ans) % 998244353)
# print(arr)
