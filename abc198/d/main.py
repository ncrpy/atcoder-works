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
perm = permutations(range(10), n)
for p in perm:
    table = str.maketrans({k: str(v) for k, v in zip(lst, p)})
    #    num = s[:]
    #    for i in range(3):
    #        for j in range(n):
    #            num[i] = num[i].replace(lst[j], str(p[j]))
    num = [si.translate(table) for si in s]
    if int(num[0]) + int(num[1]) != int(num[2]):
        continue
    elif num[0][0] == "0" or num[1][0] == "0" or num[2][0] == "0":
        continue
    else:
        for m in num:
            print(m)
        exit()
print("UNSOLVABLE")
