n = int(input())
lst = ["a"]
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
for i in range(n - 1):
    lst_ = lst
    lst = []
    for s in lst_:
        for t in abc[: len(set(s)) + 1]:
            lst.append(s + t)
for s in lst:
    print(s)
