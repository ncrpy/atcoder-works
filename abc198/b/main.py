N = list(input())
flag = False
while len(N) > 1:
    p = N.pop()
    if p != "0":
        flag = True
    if N[0] == p:
        N.pop(0)
    elif flag:
        print("No")
        break
else:
    print("Yes")
