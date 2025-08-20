import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
base,deci=lon.split(',')
lon=int(base)+(int(deci)/10**len(deci))
lat = input()
base,deci=lat.split(',')
lat=int(base)+(int(deci)/10**len(deci))
n = int(input())
min=99999999999
x=0
y=0
for i in range(n):
    defib = input()
    print("Debug messages...",defib, file=sys.stderr, flush=True)

    id,nom,adresse,_,longi,lati=defib.split(';')
    base,deci=longi.split(',')
    longi=int(base)+(int(deci)/10**len(deci))
    base,deci=lati.split(',')
    lati=int(base)+(int(deci)/10**len(deci))

    x=(float(longi)-float(lon))*math.cos((float(lat)+float(lati))/2)
    y=float(lati)-float(lat)
    d=math.sqrt((x**2)+(y**2))*6371
    if d<min:
        min=d
        lebon=nom
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(lebon)

