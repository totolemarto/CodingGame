l,c,n=[int(i) for i in input().split()]
t=[0]*n
for i in range(n):t[i]=int(input())
s=0
i=0
connu= [0]*n
for _ in range(c):
    h=0;j=0
    tmp=i
    if (connu[i] == 0):
        while h+t[i]<=l and j<n:h+=t[i];i+=1;i=i%n;j+=1
        connu[tmp] = [i,h]
    else:
        i,h = connu[i]
    s+=h
print(s)

