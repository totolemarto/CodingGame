from __future__ import annotations
import sys
import math
from enum import Enum

class Tyle_Type(Enum):
    EMPTY = 0,
    LOW = 1,
    HIGH = 2

    @staticmethod
    def to_tile(x : int):
        match x:
            case 0:
                return Tyle_Type.EMPTY
            case 1:
                return Tyle_Type.LOW
            case 2:
                return Tyle_Type.HIGH
        return Tyle_Type.EMPTY
    
    def get_defense(self) -> int:
        match self:
            case Tyle_Type.EMPTY:
                return 0
            case Tyle_Type.LOW:
                return 50
            case Tyle_Type.HIGH:
                return 75

class Agent:
    id : int 
    player : int
    shoot_cooldown : int
    optimal_range : int
    soaking_power : int
    splash_bombs : int
    line : int
    column : int
    cooldown : int
    wetness : int

    def __init__ (self , id : int, player : int, shoot_cooldown : int, optimal_range : int, soaking_power : int, splash_bombs : int):
        self.id = id
        self.player = player
        self.shoot_cooldown = shoot_cooldown
        self.optimal_range = optimal_range
        self.soaking_power = soaking_power
        self.splash_bombs = splash_bombs

    def set_position(self, line : int, column : int) -> None:
        self.line = line
        self.column = column

    def manhattan_distance(self, line : int, column : int) -> int:
        return abs(self.line - line) + abs(self.column - column)
    
    def shortest_path(self, line : int, column : int) -> list[int] :
        result = [self.line, self.column]
        if self.line != line:
            result[0] += (line - self.line)
        else:
            result[1] += (column - self.column)
        return result
   
    def get_defense(self, line : int, column : int) -> int:
        better_defense : Tyle_Type = Tyle_Type.EMPTY 
        if self.line == line:
            if abs(self.column - column) <= 2 :
                return 0
            if self.column > column:
                better_defense = grid[self.line][self.column - 1]
            else:
                better_defense =  grid[self.line][self.column - 1]
        elif self.column == column:
            if abs(self.line - line) <= 2 :
                return 0
            if self.line > line:
                better_defense = grid[self.line - 1][self.column]
            else:
                better_defense =  grid[self.line + 1][self.column]
        else:
            pass 
        return better_defense.get_defense()

    def get_amount_attack(self, other : Agent) -> int:
        other.get_defense(self.line, self.column)
        return 0

    def who_attack(self, all_agent : dict[int, Agent]) -> int: 
        result : int = 0
        maxi_attack : int = -1
        for key, agent in all_agent.items():
            if agent.player == self.player:
                continue
            x =  self.get_amount_attack(agent)
            if x > maxi_attack:
                maxi_attack = x
                result = key
        return result 

    def find_best_cell(self) -> None:
        maybe : list[Tyle_Type] = []
        maybe.append(grid[self.line -1][self.column])
        maybe.append(grid[self.line][self.column + 1])
        maybe.append(grid[self.line + 1][self.column])
        maybe.append(grid[self.line][self.column - 1])
        pass

def init_agent() -> dict[int, Agent] :
    agent_count = int(input())  # Total number of agents in the game

    result : dict[int, Agent] = {}
    for i in range(agent_count):
        # agent_id: Unique identifier for this agent
        # player: Player id of this agent
        # shoot_cooldown: Number of turns between each of this agent's shots
        # optimal_range: Maximum manhattan distance for greatest damage output
        # soaking_power: Damage output within optimal conditions
        # splash_bombs: Number of splash bombs this can throw this game
        agent_id, player, shoot_cooldown, optimal_range, soaking_power, splash_bombs = [int(j) for j in input().split()]
        result[agent_id] = Agent(agent_id, player, shoot_cooldown, optimal_range, soaking_power, splash_bombs)
    return result

def init_map() -> list[list[Tyle_Type]] :
    result : list[list[Tyle_Type]] = []
    width, height = [int(i) for i in input().split()]
    for i in range(height):
        result.append([])
        inputs = input().split()
        for j in range(width):
            # x: X coordinate, 0 is left edge
            # y: Y coordinate, 0 is top edge
            x = int(inputs[3*j])
            y = int(inputs[3*j+1])
            result[i].append(Tyle_Type.to_tile(int(inputs[3*j+2])))
    return result

def do_move_tutorial(x : Agent):
    if x.manhattan_distance(1,6) == maxi:
        goto : list[int] = x.shortest_path(1,6)
        print(f"{x.id};MOVE {goto[1]} {goto[0]}")
    else:
        goto : list[int] = x.shortest_path(3,6)
        print(f"{x.id};MOVE {goto[1]} {goto[0]}")

def do_shot_tutorial(my_agent : Agent, id_other_agent : int):
    print(f"{my_agent.id};SHOOT {id_other_agent}")
    

# Win the water fight by controlling the most territory, or out-soak your opponent!

my_id = int(input())  # Your player id (0 or 1)
all_agent : dict[int, Agent] = init_agent()
grid : list[list[Tyle_Type]] = init_map() 
while True:
    agent_count = int(input())
    maxi = -1
    to_shoot = -1
    for i in range(agent_count):
        # cooldown: Number of turns before this agent can shoot
        # wetness: Damage (0-100) this agent has taken
        agent_id, x, y, cooldown, splash_bombs, wetness = [int(j) for j in input().split()]
        while all_agent[i].id != agent_id:
            all_agent.pop(i)
        all_agent[i].set_position(y, x)
        all_agent[i].cooldown = cooldown
        all_agent[i].splash_bombs = splash_bombs
        all_agent[i].wetness = wetness 
        if all_agent[i].id != my_id  and all_agent[i].wetness > maxi:
            maxi = all_agent[i].wetness
            to_shoot = all_agent[i].id
            #        if all_agent[i].manhattan_distance(1,6) < maxi:
#            maxi = all_agent[i].manhattan_distance(1,6)
    my_agent_count = int(input())  # Number of alive agents controlled by you
    for i in range(my_agent_count):
        if False:
            do_move_tutorial(all_agent[i])
            do_shot_tutorial(all_agent[i], to_shoot)


        # One line per agent: <agentId>;<action1;action2;...> actions are "MOVE x y | SHOOT id | THROW x y | HUNKER_DOWN | MESSAGE text"

