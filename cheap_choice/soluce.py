import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Object:
    cat : str
    size: str
    price : int

    def __init__(self, cat, size, price):
        self.cat = cat
        self.size = size
        self.price = price

objects : list[Object] = []
stock = int(input())
command = int(input())
for i in range(stock):
    item = input()
    cat, size, price = item.split(" ")
    objects.append(Object(cat,size,price))
for i in range(command):
    order = input()
    cat, size = order.split(" ")
    cur : Object = None
    for object in objects:
        if object.cat == cat and object.size == size and (cur is None or cur.price > object.price):
            cur = object
    if cur != None:
        objects.remove(cur) 
        print(cur.price)
    else:
        print("NONE")

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


