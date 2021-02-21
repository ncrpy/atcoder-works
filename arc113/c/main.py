from copy import copy

s = input()[::-1]
count_init = {chr(i): 0 for i in range(97, 123)}
count = copy(count_init)
ans = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        ans += i - count[s[i]]
        count = copy(count_init)
        count[s[i]] = i
    count[s[i]] += 1
print(ans)
