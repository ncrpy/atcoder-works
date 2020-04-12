s = input()
n = (len(s) - 1) // 2
ans = "No"
for i in range(n):
    if s[i] != s[-1 - i]:
        break
    elif s[i] != s[n - 1 - i]:
        break
else:
    ans = "Yes"
print(ans)
