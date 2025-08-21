class N:
    def __init__(a,d):a.f=[];a.d=d
def p(t):return 1+sum(p(f) for f in t.f)
def a(t,v,r):
    if r>=len(v):return
    for f in t.f:
        if f.d==v[r]:a(f,v,r+1);return
    t.f.append(N(v[r]));a(t.f[-1],v,r+1)
x=N(-1);o=input
for i in range(int(o())):a(x,o(),0)
print(p(x)-1)
