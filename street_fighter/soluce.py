import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.




class Fighter:
    name : str
    life : int
    punch : int
    kick : int
    rage : int 
    hit_made : int
    damage_received : int

    def __init__(self, name, life, punch, kick):
        self.name = name 
        self.life = life
        self.punch = punch
        self.kick = kick
        self.rage = 0
        self.hit_made = 0
        self.damage_received = 0
        
    def kick_method(self, other):
        other.life -= self.kick
        other.damage_received += self.kick
        other.rage += 1
        self.hit_made += 1
    
    def punch_method(self, other):
        other.life -= self.punch
        other.damage_received += self.punch
        other.rage += 1
        self.hit_made += 1
    
    def special_attack_method(self, other):
        match self.name:
            case "KEN":
                other.life -= 3 * self.rage
                other.damage_received += 3 * self.rage
            case "RYU":
                other.life -= 4 * self.rage
                other.damage_received += 4 * self.rage
            case "TANK":
                other.life -= 2 * self.rage
                other.damage_received += 2 * self.rage
            case "VLAD":
                other.life -= 2 * (self.rage + other.rage)
                other.damage_received += 2 * (self.rage + other.rage)
                other.rage = 0
            case "JADE":
                other.life -= self.hit_made * self.rage
                other.damage_received += self.hit_made * self.rage
            case "ANNA":
                other.life -= self.damage_received * self.rage
                other.damage_received += self.damage_received * self.rage
            case "JUN":
                other.life -= self.rage
                other.damage_received += self.rage
                self.life += self.rage
        other.rage += 1
        self.rage = 0
        self.hit_made += 1

    def __str__ (self):
        return f"{self.name} a {self.life} vie"

def champ_factory(name : str) -> Fighter:
    match name:
        case "KEN":
            return Fighter("KEN", 25, 6, 5)
        case "RYU":
            return Fighter("RYU", 25, 4, 5)
        case "TANK":
            return Fighter("TANK", 50, 2, 2)
        case "VLAD":
            return Fighter("VLAD", 30, 3, 3)
        case "JADE":
            return Fighter("JADE", 20, 2, 7)
        case "ANNA":
            return Fighter("ANNA", 18, 9, 1)
        case "JUN":
            return Fighter("JUN", 60, 2, 1)


champion_1, champion_2 = input().split()
champion_1 : Fighter = champ_factory(champion_1)
champion_2 : Fighter = champ_factory(champion_2)
n = int(input())
for i in range(n):
    d, attack = input().split()
    if d == ">":
        champ = champion_1
        other = champion_2
    else:
        champ = champion_2
        other = champion_1
    match attack:
        case "KICK":
            champ.kick_method(other)
        case "PUNCH":
            champ.punch_method(other)
        case "SPECIAL":
            champ.special_attack_method(other)
    if other.life <= 0:
        break
if champion_2.life > champion_1.life:
    winner= champion_2
    loser = champion_1
else:
    winner= champion_1
    loser = champion_2
print(f"{winner.name} beats {loser.name} in {winner.hit_made} hits")
        
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


