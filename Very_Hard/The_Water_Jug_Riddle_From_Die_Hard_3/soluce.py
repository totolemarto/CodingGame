from __future__ import annotations
import queue
import random
from copy import deepcopy
import sys
import math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Botle:
    current : int
    posible : int

    def __init__(self, possible, current = 0):
        self.current = current
        self.posible = possible

    def empty(self) -> None:
        self.current = 0

    def fill(self) -> None:
        self.current = self.posible

    def poor(self, other : Botle) -> int:
        other_size = other.remain()
        if other_size > self.current:
            other.current += self.current
            self.current = 0
        else:
            other.current += other_size 
            self.current -= other_size
        return self.current

    def __lt__(self, other):
        return (self.posible , self.current) < (other.posible , other.current)

    def remain(self) -> int:
        return self.posible - self.current

    def copy(self):
        return Botle(self.posible, self.current)

def get_other(bottles : list[Botle], botles : list[Botle]):
    result : list[Botle] = []
    for bottle in bottles:
        if bottle not in botles:
            result.append(bottle.copy())
    return result

# Faire une file et pas une pile pour faire du largeur d'abord
def find_minimum_steps(bottles : list[Botle], cur_step : int) -> int:
    total = 0
    explore = 0 
    to_calls = queue.PriorityQueue()
    to_calls.put((0, 0, bottles))
    deja_vu = {}
    while not to_calls.empty():
        priority,  index, bottles = to_calls.get()
        # for bottle in bottles:
        #     print(f" bottle contenance {bottle.posible} contient {bottle.current}", end= " ")
        # print("sur profondeur " , index)
        tmp = ""
        for bottle in bottles:
            tmp += str(bottle.current) + " "
            tmp += str(bottle.posible) + " "
            if bottle.current == target:
                print("on coupe ", total)
                print("on explore", explore)
                return index  
        if tmp in deja_vu:
            total += 1
            continue
        explore += 1
        deja_vu[tmp] = 1
        for bottle in bottles:
            if (bottle.current != bottle.posible):
                tmp = get_other(bottles, [bottle])
                tmp.append(Botle(bottle.posible, bottle.posible))
                to_calls.put((0, index + 1, tmp))
            if bottle.current == 0:
                continue
            tmp = get_other(bottles, [bottle])
            tmp.append(Botle(bottle.posible, 0))
            to_calls.put((0, index + 1, tmp))
            for other_bottle in bottles:
                if other_bottle == bottle or other_bottle.current == other_bottle.posible:
                    continue
                tmp = get_other(bottles, [bottle, other_bottle])
                amount_poor = min(other_bottle.posible - other_bottle.current, bottle.current)
                tmp.append(Botle(bottle.posible, bottle.current - amount_poor))
                tmp.append(Botle(other_bottle.posible, other_bottle.current + amount_poor ))
                to_calls.put((0, index + 1, tmp))
    return -1 

target = int(input())
containers_count = int(input())
bottles : list[Botle] = []
state = []
cur_state = []
for i in range(containers_count):
    bottles.append(Botle(possible=int(input()), current=0))
print(find_minimum_steps(bottles, 0))


