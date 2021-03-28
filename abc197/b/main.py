h, w, x, y = map(int, input().split())
x -= 1
y -= 1
s = [input() for _ in range(h)]

ans_up = 0
for i in range(x):
    ans_up += 1
    if s[i][y] == "#":
        ans_up = 0
ans_down = 0
for i in range(x + 1, h):
    if s[i][y] == "#":
        break
    ans_down += 1
ans_left = 0
for i in range(y):
    ans_left += 1
    if s[x][i] == "#":
        ans_left = 0
ans_right = 0
for i in range(y + 1, w):
    if s[x][i] == "#":
        break
    ans_right += 1
print(ans_up + ans_down + ans_left + ans_right + 1)
