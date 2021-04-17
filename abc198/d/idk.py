from itertools import permutations

s = [input() for _ in range(3)]
lst = []
for c in s[0] + s[1] + s[2]:
    lst.append(c)
lst = list(set(lst))
n = len(lst)
if n > 10:
    print("UNSOLVABLE")
    exit()
sn = [[lst.index(c) for c in si] for si in s]
perm = permutations(range(10), n)
for p in perm:
    # num = s[:]
    # for i in range(3):
    #     for j in range(n):
    #         num[i] = num[i].replace(lst[j], str(p[j]))
    #
    # table = str.maketrans({k: str(v) for k, v in zip(lst, p)})
    # num = [si.translate(table) for si in s]
    flag = False
    num = [0] * 3
    for i in range(3):
        for j in sn[i][::-1]:
            num[i] *= 10
            num[i] += p[j]
            if p[j] == 0 and j == len(sn[i]):
                flag = True
                break
        if flag:
            break
    if flag:
        continue
    elif num[0] + num[1] != num[2]:
        continue
    else:
        for m in num:
            print(m)
        exit()
print("UNSOLVABLE")
