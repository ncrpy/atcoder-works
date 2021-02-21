t = int(input())
for _ in range(t):
    s = input()
    list_a = []
    count_a = 0
    count_b = 0
    last_a = None
    for i in range(len(s)):
        if s[i] == "a":
            last_a = i
            count_a += 1
            if i == len(s) - 1:
                list_a.append(count_a)
                break
            elif s[i + 1] == "b":
                list_a.append(count_a)
                count_a = 0
        else:
            count_b += 1
    count_a = len(s) - count_b
    block_1 = list_a.count(1)
    remove_a = len(list_a) - block_1 // 2 - 1
    if last_a == len(s) - 1:
        ans = "b" * count_b + "a" * (count_a - 2 * remove_a)
    elif count_a % 2 == 0:
        ans = "b" * count_b
    elif last_a == len(s) - 2:
        ans = "b" * (count_b - 1) + "ab"
    elif last_a == len(s) - 3:
        ans = "b" * (count_b - 2) + "abb"
    elif s[0] == "a" and len(list_a) == 1:
        ans = "a" + "b" * count_b
    elif block_1 < len(list_a) and s[0] == "b":
        ans = "b" * (count_b - 2) + "a" * (count_a - 2 * remove_a)
    elif block_1 < len(list_a) - 1 or list_a[0] == 1:
        ans = "b" * (count_b - 2) + "a" * (count_a - 2 * remove_a)
    elif block_1 % 2 == 1:
        ans = "b" * (count_b - 2) + "a" * (count_a - 2 * remove_a)
    else:
        ans = "b" * (count_b - 2) + "a" * (count_a - 2 * remove_a - 2)
    print(ans)
