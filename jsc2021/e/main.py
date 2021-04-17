from collections import Counter


def spl(s):
    l = len(s)
    return [s[: l // 2], s[l - 1 : (l + 1) // 2 - 1 : -1]]


k = int(input())
s = list(input())
if len(s) < 2 ** (k - 1):
    print("impossible")
    exit()

lst = [s]
for _ in range(k):
    tmp = []
    for t in lst:
        tmp += spl(t)
    lst_old = lst
    lst = tmp

ll = len(lst)
lst = list(zip(*lst))
lt = len(lst)
if lt == 1:
    print("impossible")
    exit()
if lt == 0:
    lst = list(zip(*lst_old))[0]
    c = Counter(lst).most_common()
    print(len(lst) - c[0][1])
    exit()

cnt1 = []
cnt2 = []
finl = []
for i in range(lt):
    c = Counter(lst[i]).most_common()
    cnt1.append(c[0][1])
    finl.append(c[0][0])
    if i == (lt - 1) / 2:
        cnt2.append(1e6)
    elif len(c) > 1:
        cnt2.append(c[0][1] - c[1][1])
    else:
        cnt2.append(1e6)

if finl == finl[::-1]:
    mn = min(cnt2)
    idx = cnt2.index(mn)
    if mn == 1e6:
        cnt1[idx] = 0
    else:
        cnt1[idx] -= cnt2[idx]

print(lt * ll - sum(cnt1))
