s = input()
s1 = s[0 : len(s) : 2]
s2 = s[1 : len(s) : 2]
if s1.islower() and (s2.isupper() or not s2):
    print("Yes")
else:
    print("No")
