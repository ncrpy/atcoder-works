n=int(input())
f=n//3
b=n//5
fb=n//15

def sumt(x):
    return x*(x+1)//2

ans = sumt(n)-3*sumt(f)-5*sumt(b)+15*sumt(fb)
print(ans)
