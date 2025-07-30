from __future__ import annotations
from enum import Enum
import sys
import math

class Owner(Enum):
    me = 0
    ennemy = 1
    neutral = 2
    error = 3

    @staticmethod
    def get_owner(player : int) -> Owner:
        if player == 1:
            return Owner.me
        if player == -1:
            return Owner.ennemy
        if player == 0:
            return Owner.neutral
        return Owner.error


class Factory:
    player : Owner 
    stock : int
    production : int
    distance_from : dict[Factory, int]
    id : int

    def __init__(self, id : int):
        self.id = id
        self.player = Owner.neutral

class Troup:
    player : Owner 
    begin : Factory 
    end : Factory
    nb_cyborg : int
    time_before_end : int
    
    def __init__(self, player : Owner, begin : Factory, end : Factory, nb_cyborg : int, time_before_end : int):
        self.player = player
        self.begin = begin
        self.end = end
        self.nb_cyborg = nb_cyborg
        self.time_before_end = time_before_end

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
all_factories : list[Factory] = []
dicofactdist={}
aquiusine={}
dicorobot={}
nbunitfact={}

factory_count = int(input())  # the number of factories
for i in range(factory_count):
    all_factories.append(Factory(i))

link_count = int(input())  # the number of links between factories
for i in range(link_count):
    
    factory_1, factory_2, distance = [int(j) for j in input().split()]
    all_factories[factory_1].distance_from[all_factories[factory_2]] = distance
    all_factories[factory_2].distance_from[all_factories[factory_1]] = distance
# game loop
while True:
    all_troups : list[Troup] = []
    entity_count = int(input())  # the number of entities (e.g. factories and troops)
    for i in range(entity_count):
        inputs = input().split()
        entity_id = int(inputs[0])
        entity_type = inputs[1]
        arg_1 = int(inputs[2])
        arg_2 = int(inputs[3])
        arg_3 = int(inputs[4])
        arg_4 = int(inputs[5])
        arg_5 = int(inputs[6])
        if entity_type=="FACTORY":
            all_factories[entity_id].player = Owner.get_owner(arg_1)
            all_factories[entity_id].stock = arg_2
            all_factories[entity_id].production  = arg_3
        else:
            all_troups.append(Troup(Owner.get_owner(arg_1), all_factories[arg_2], all_factories[arg_3], arg_4, arg_5))
    min=50000
    lesbon=[0]*4
    lesbon[0]=-522
    for i,j in dicofactdist:
        if aquiusine[i]==1 and aquiusine[j]==0:
            if min>dicofactdist[(i,j)]:
                min=dicofactdist[(i,j)]
                if lesbon[0]==-522:lesbon[0]=i;lesbon[1]=j
                else: lesbon[2]=i;lesbon[3]=j
            elif min*1.5<dicofactdist[i,j] and nbunitfact[i]>nbunitfact[lesbon[0]]:
                if lesbon[0]==-522:lesbon[0]=i;lesbon[1]=j
                else: lesbon[2]=i;lesbon[3]=j
    if min==50000:
        max=0
        for i in range(len(aquiusine)):
            if aquiusine[i]==1:
                if max<nbunitfact[i]:
                    max=nbunitfact[i]
                    lesbon=i
            else:
                if min>nbunitfact[i]:
                    min=nbunitfact[i]
                    attaque=i+2
        print("MOVE",lesbon,attaque,max//2)
    else:
        if lesbon[2]!=0 and lesbon[3]!=0:
            print("MOVE",lesbon[0],lesbon[1],nbunitfact[lesbon[0]]//4,"; MOVE",lesbon[2],lesbon[3],nbunitfact[lesbon[2]]//4)
        else:
            print("MOVE",lesbon[0],lesbon[1],nbunitfact[lesbon[0]]//2)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # Any valid action, such as "WAIT" or "MOVE source destination cyborgs"
    #    print("WAIT")
