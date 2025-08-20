r=""
def f():
    global i,r;x=b[i];h=1
    while i+1<7 and b[i+1]==x:h+=1;i+=1;x=b[i]
    j="0" if x=="1" else "00"  
    if len(s:=r.split())>=2 and s[-2]==j:r = r[0:-1];r+="0" * h + " "
    else:r+=j+" " + "0" * h + " "
for a in input():
    b=format(ord(a),'07b');i=0
    while i<7:f();i+=1
print(r[:-1])
