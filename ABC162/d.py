import collections

n=int(input())
s=input()
m=(n-1)//2
x=0

l=collections.Counter(s)
ans=l['R']*l['G']*l['B']

for i in range(1, m+1):
    for j in range(n-i*2):
        a=j
        b=a+i
        c=b+i
        if s[a] != s[b] != s[c] != s[a]:
            x += 1

print(ans-x)
