from __future__ import annotations
from itertools import product
import sys
import math
import random
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

    def get_max(self, other: Tyle_Type) -> Tyle_Type:
        if self.get_defense() > other.get_defense():
            return self 
        return other

class Move:
    movement : list[int]
    shoot : int | None
    bomb : list[int] | None
    defense : bool
    agent : Agent 
    amount_attack : int
    prev_pos : list[int]


    def __init__(self, agent = None):
        self.shoot = -1
        self.movement = []
        self.agent = agent
        self.bomb = []
        self.prev_pos = []
        pass

    def add_move(self, line : int, column : int) -> None:
        self.movement = []
        self.movement.append(line)
        self.movement.append(column)
    
    def add_shoot(self, id_other : int) -> None:
        self.shoot = id_other 
    
    def add_bomb(self, line : int, column : int) -> None:
        self.bomb = []
        self.bomb.append(line)
        self.bomb.append(column)

    def is_defense(self):
        self.defense = True

    def to_str(self) -> str:
        result = f"{self.agent.id};"
        if self.movement != []:
            result += f"MOVE {self.movement[1]} {self.movement[0]}"
        if self.bomb != []:
            result += f";THROW {self.bomb[1]} {self.bomb[0]}"
        elif self.shoot != -1:
            result += f";SHOOT {self.shoot}"
        elif self.is_defense:
            result += f";HUNKER_DOWN"
        return result

    def do(self):
        self.prev_pos.append(self.agent.line)
        self.prev_pos.append(self.agent.column)
        self.agent.line = self.movement[0]
        self.agent.column = self.movement[1]
        if self.shoot != -1:
            other = get_agent_by_id(self.shoot)
            self.amount_attack = self.agent.get_amount_attack(other)
            other.wetness += self.amount_attack 
        if self.bomb:
            for agent in drop_bomb(self.bomb[0], self.bomb[1]):
                agent.wetness += 35

        if self.is_defense:
            self.agent.defense = 25
            

    def undo(self):
        self.agent.line = self.prev_pos[0]
        self.agent.column = self.prev_pos[1]
        if self.shoot != -1:
            other = get_agent_by_id(self.shoot)
            other.wetness -= self.amount_attack 
        if self.bomb:
            for agent in drop_bomb(self.bomb[0], self.bomb[1]):
                agent.wetness -= 35
        if self.is_defense:
            self.agent.defense = 0

def drop_bomb(line: int, column : int) -> list[Agent]:
    result : list[Agent] = []
    for agent in all_agent.values():
        if abs(agent.line - line) + abs(agent.column - column) <= 1:
            result.append(agent)
            continue
        if abs(agent.line - line) + abs(agent.column - column) == 2 and line != agent.line and column != agent.column:
            result.append(agent)
    return result

def get_agent_by_id(id : int) -> Agent:
    for values in all_agent.values():
        if values.id == id:
            return values
    return None

class Agent:
    # agent_id: Unique identifier for this agent
    # player: Player id of this agent
    # shoot_cooldown: Number of turns between each of this agent's shots
    # optimal_range: Maximum manhattan distance for greatest damage output
    # soaking_power: Damage output within optimal conditions
    # splash_bombs: Number of splash bombs this can throw this game
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
    defense : int

    def __init__ (self , id : int, player : int, shoot_cooldown : int, optimal_range : int, soaking_power : int, splash_bombs : int):
        self.id = id
        self.player = player
        self.shoot_cooldown = shoot_cooldown
        self.optimal_range = optimal_range
        self.soaking_power = soaking_power
        self.splash_bombs = splash_bombs
        self.defense = 0

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
            if line > self.line:
                if column > self.column:
                    better_defense = grid[self.line + 1][self.column].get_max(grid[self.line][self.column + 1])
                else: # column < self.column
                    better_defense = grid[self.line + 1][self.column].get_max(grid[self.line][self.column - 1])
            else:
                if column > self.column:
                    better_defense = grid[self.line - 1][self.column].get_max(grid[self.line][self.column + 1])
                else: # column < self.column
                    better_defense = grid[self.line - 1][self.column].get_max(grid[self.line][self.column - 1])
        return better_defense.get_defense() + self.defense

    def get_amount_attack(self, other : Agent) -> float:
        other_defense : int = other.get_defense(self.line, self.column)
        multiplicator : float =  0.5 if self.manhattan_distance(other.line, other.column) > self.optimal_range else 1
        if self.manhattan_distance(other.line, other.column) > self.optimal_range * 2:
            multiplicator = 0
        real_defense : float = 1 + (other_defense / 100 ) + (other.defense / 100)

        return self.soaking_power * multiplicator / real_defense 

    def who_attack(self, all_agent : dict[int, Agent], line : int = -1, column : int = -1) -> int: 
        result : int = 0
        maxi_attack : float = -1
        tmp_line : int
        tmp_column : int
        if line != -1:
            tmp_line = self.line
            tmp_column = self.column
            self.line = line
            self.column = column
        for key, agent in all_agent.items():
            if agent.player == self.player:
                continue
            x = self.get_amount_attack(agent)
            if x + agent.wetness >= 100:
                result = key
                break

            if x > maxi_attack:
                maxi_attack = x
                result = key
        if line != -1:
            self.line = tmp_line
            self.column = tmp_column
            
        return result 

    
    def find_best_cell(self) -> list[int]:
        # Make it better !!!
        maybe : list[list[int]] = get_adjacent_cell(self.line, self.column, diagonal = False) 
        for elem  in maybe:
            if grid[elem[0] + 1][elem[1]] == Tyle_Type.HIGH:
                    return elem
            if grid[elem[0] - 1][elem[1]] == Tyle_Type.HIGH:
                    return elem
            if grid[elem[0] ][elem[1] - 1] == Tyle_Type.HIGH:
                    return elem
            if grid[elem[0] ][elem[1] + 1] == Tyle_Type.HIGH:
                    return elem
        return []

    
    def send_bomb(self, line : int = -1, column : int = -1) -> tuple[list[int], int]:
        result : list[int] = []
        if self.splash_bombs <= 0:
            return result, 0 
        tmp_line : int
        tmp_column : int
        if line != -1:
            tmp_line = self.line
            tmp_column = self.column
            self.line = line
            self.column = column
        max_distance : int = 4
        dammage : int = 30
        enemy_positions : list[list[int]] = get_position_of_ennemy() 
        maxi = 0
        for i in range(-4, max_distance):
            for j in range(-4, max_distance):
                if abs(i) + abs(j) > 4:
                    continue
                nb_touch_ennemy = 0
                line_bomb = self.line + i
                column_bomb = self.column + j
                if line_bomb < 0 or line_bomb >= len(grid) or column_bomb < 0 or column_bomb >= len(grid[0]):
                    continue
                accesible_cell = get_adjacent_cell(line_bomb, column_bomb, diagonal = True)
                accesible_cell.append( [line_bomb, column_bomb] )
                need_to_continue = False
                for pos_enemy in enemy_positions:
                    if pos_enemy in accesible_cell:
                        nb_touch_ennemy += 1
                #print(f"{i=} {j=} {nb_touch_ennemy=}", file=sys.stderr, flush=True)
                if nb_touch_ennemy > maxi :
                    need_to_continue = False
                    my_agents : list[list[int]] = get_position_of_my_agent()
                    stop_it = False
                    mine = 0
                    for pos_agent in my_agents:
                        if pos_agent in accesible_cell:
                            mine += 1
                    if mine >= nb_touch_ennemy:
                        continue
                    maxi = nb_touch_ennemy
                    result = [ line_bomb, column_bomb ]
        if line != -1:
            self.line = tmp_line
            self.column = tmp_column
        return result, maxi 

    def get_all_move(self) -> list[Move]:
        result : list[Move] = []
        for cell in get_adjacent_cell(self.line, self.column):
            if not can_move_to_cell(cell[0], cell[1]):
                continue
            result.append(Move(self)) # only move
            result[-1].add_move(cell[0], cell[1])
            result[-1].is_defense()
            if self.shoot_cooldown == 0: # Shoot
                tmp = self.who_attack(all_agent, line = cell[0], column = cell[1])
                if self.get_amount_attack(all_agent[tmp]) > 0:
                    result.append(Move(self)) 
                    result[-1].add_move(cell[0], cell[1])
                    result[-1].add_shoot(all_agent[tmp].id)
            if self.splash_bombs <= 0:
                continue 
            pos, _ = self.send_bomb(cell[0], cell[1])
            if not pos:
                continue
            result.append(Move(self)) # move and shoot
            result[-1].add_move(cell[0], cell[1])
            result[-1].add_bomb(pos[0], pos[1])
                    
        return result

def can_move_to_cell(line : int, column : int) -> bool:
    return grid[line][column] == Tyle_Type.EMPTY

def get_position_of_ennemy() -> list[list[int]]:
    result : list[list[int]] = []
    for agent in all_agent.values():
        if agent.player != my_id:
            result.append([agent.line, agent.column])
    return result

def get_position_of_my_agent() -> list[list[int]]:
    result : list[list[int]] = []
    for agent in all_agent.values():
        if agent.player == my_id:
            result.append([agent.line, agent.column])
    return result


def get_my_agents() -> list[Agent]:
    result : list[Agent] = []
    for agent in all_agent.values():
        if agent.player == my_id:
            result.append(agent)
    return result

def get_ennemy_agents() -> list[Agent]:
    result : list[Agent] = []
    for agent in all_agent.values():
        if agent.player != my_id:
            result.append(agent)
    return result

def get_adjacent_cell(line : int, column: int, diagonal : bool = False) -> list[list[int]]:
    result : list[list[int]] = []
    if line > 0:
        if column > 0 and diagonal:
            result.append([line - 1, column - 1])
        result.append([line - 1, column])
        if column < len(grid[0]) - 1 and diagonal:
            result.append([line - 1, column + 1])
    if column > 0:
        result.append([line, column - 1])
    if column < len(grid[0]) - 1:
        result.append([line, column + 1])
    if line < len(grid) - 1:
        if column > 0 and diagonal:
            result.append([line + 1, column - 1])
        result.append([line + 1, column])
        if column < len(grid[0]) - 1 and diagonal:
            result.append([line + 1, column + 1])
    return result


def init_agent() -> dict[int, Agent] :
    agent_count = int(input())  # Total number of agents in the game

    result : dict[int, Agent] = {}
    for i in range(agent_count):
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

def nearest(line : int, column : int) -> Agent:
    maxi = 100
    result : Agent 
    for agent in all_agent.values():
        distance : int = agent.manhattan_distance(line, column)
        if agent.wetness > 50:
            distance *= 2
        if distance < maxi:
            maxi = distance 
            result = agent
    return result


def amount_of_the_map() -> int:
    me : int = 0
    for line in range(len(grid)):
        for column in range(len(grid[0])):
            if nearest(line, column).player == my_id:
                me+=1
            else:
                me-=1
    return me

def heuristic() -> int :
    score_life : int = 0
    score_defense : int = 0
    them = 0
    us = 0
    total_range = 0
    total_bomb = 0
    bonus = 0
    for agent in all_agent.values():
        if agent.player == my_id:
            if agent.wetness < 100:
                total_range += agent.optimal_range
                total_bomb += agent.splash_bombs
                us += 1
                score_life -= agent.wetness
                mini = 20
                for other in get_ennemy_agents():
                    distance = agent.manhattan_distance(other.line, other.column)
                    if distance < (other.optimal_range * 2):
                        score_defense += agent.get_defense(other.line, other.column) + agent.defense
                    if distance < mini:
                        mini = distance
                        other_good = other
                if mini <= agent.optimal_range and mini > other_good.optimal_range:
                    bonus += 1500
            else:
                score_life -= 200 * 2
        else:
            if agent.wetness < 100:
                total_range -= agent.optimal_range
                total_bomb -= agent.splash_bombs

                them += 1
                score_life += agent.wetness

            else:
                score_life += 200 * 2


    mapi = amount_of_the_map() * 95
    print(f"valeur de la map {mapi}, defense : {score_defense}, score_life : {score_life}, bonus : {bonus}", file=sys.stderr)
    return score_life * 15 + mapi + score_defense  + bonus + total_bomb * 20 + total_range * 10

def run_move(moves, agent):
    for move in moves:
        if move.agent == agent:
            print(move.to_str())
            return

def play_turn(agent : Agent) -> None:
    mini = -math.inf
    good : Move = Move()
    line : int = agent.line
    column : int = agent.column
    true_life = {}
    for move in get_adjacent_cell(agent.line, agent.column):
        agent.line = move[0]
        agent.column = move[1]
        for agent_bis in all_agent.values():
            if agent_bis.player != agent.player:
                if int(agent.get_amount_attack(agent_bis)) < agent.soaking_power:
                    continue
                agent_bis.wetness -= int(agent.get_amount_attack(agent_bis))
                tmp = heuristic()
                if tmp > mini:
                    mini = tmp
                    good.movement = move
                    good.shoot = agent_bis.id
                agent_bis.wetness += int(agent.get_amount_attack(agent_bis))
        tmp = heuristic()
        goto, nb_ennemy = agent.send_bomb()
        if nb_ennemy > 0:
            print(f"{agent.id}; THROW {goto[1]} {goto[0]}")
            return

        if tmp > mini:
            mini = tmp
            good.movement = move
    agent.line = good.movement[0]
    agent.column = good.movement[1]
    print(f"{agent.id}; {good.to_str()}; MESSAGE = {mini}")
    return

def all_moves_possible(me : bool) :
    agents : list[Agent] = []
    result : list[list[Move]] = []
    for agent in all_agent.values():
        if  (agent.player == my_id) == me:
            agents.append(agent)
    for agent in agents:
        result.append(agent.get_all_move())
    x =list(product(*result))
    random.shuffle(x)
    return x


def min_max(depth : int, isMaximizingPlayer : bool, first : bool = True) -> list[Move] | float:
    # If it's the computer's turn (maximizing)
    result : list[Move]
    if depth == 0:
        return float(heuristic())
    if isMaximizingPlayer:
       result = []
       for agent in get_my_agents():
            bestScore = -math.inf
            tmp = []
            for move in agent.get_all_move():
                if move.movement == [x.movement for x in result]:
                    continue
                move.do()
                print(move.to_str(), file=sys.stderr)
                score = min_max(depth - 1, False, False)
                move.undo()
                if bestScore < float(score):
                        bestScore = score
                        tmp = move
            result.append(tmp)
       if not first:
           return float(bestScore)
       print(result, "ici", file=sys.stderr)
       return result
    else:
       bestScore = math.inf
       result = []
       for agent in get_ennemy_agents():
            bestScore = math.inf
            tmp = []
            for move in agent.get_all_move():
                move.do()
                print(move.to_str(), file=sys.stderr)
                score = min_max(depth - 1, True, False)
                move.undo()
                if bestScore > float(score):
                        bestScore = score
                        tmp = move
            result.append(tmp)
       if not first:
           return float(bestScore)
       print(result, "ici", file=sys.stderr)
       for move in result:
        move.do()
       return result

# Win the water fight by controlling the most territory, or out-soak your opponent!
my_id = int(input())  # Your player id (0 or 1)
all_agent : dict[int, Agent] = init_agent()
grid : list[list[Tyle_Type]] = init_map() 
all_moves = {}
while True:
    agent_count = int(input())
    maxi = -1
    to_shoot = -1
    all_id : list[int] = []
    for i in range(agent_count):
        # cooldown: Number of turns before this agent can shoot
        # wetness: Damage (0-100) this agent has taken
        agent_id, x, y, cooldown, splash_bombs, wetness = [int(j) for j in input().split()]
        all_agent[agent_id].set_position(y, x)
        all_id.append(agent_id)
        all_agent[agent_id].shoot_cooldown = cooldown
        all_agent[agent_id].splash_bombs = splash_bombs
        all_agent[agent_id].wetness = wetness 
        if all_agent[agent_id].id != my_id  and all_agent[agent_id].wetness > maxi:
            maxi = all_agent[agent_id].wetness
            to_shoot = all_agent[agent_id].id
            #        if all_agent[i].manhattan_distance(1,6) < maxi:
#            maxi = all_agent[i].manhattan_distance(1,6)
    my_agent_count = int(input())  # Number of alive agents controlled by you
    to_remove : list[int] = []
    for elem in all_agent.keys():
        if elem not in all_id:
            to_remove.append(elem)
    for elem in to_remove:
        del all_agent[elem]
#    _, moves_to_do, _ = min_max_joint(1, True,  alpha=float('-inf'), beta=float('inf'))
    moves_to_do = min_max(1, True)

    for agent in all_agent.values():
        if agent.player != my_id:
            continue
        if False:
            do_move_tutorial(agent)
            do_shot_tutorial(agent, to_shoot)
            do_move_shot_tutorial(agent, all_agent)
            do_bomb_tutorial(agent)
    #    play_turn(agent)
        run_move(moves_to_do, agent)
        # One line per agent: <agentId>;<action1;action2;...> actions are "MOVE x y | SHOOT id | THROW x y | HUNKER_DOWN | MESSAGE text"

####
def do_move_tutorial(x : Agent):
    if x.manhattan_distance(1,6) == maxi:
        goto : list[int] = x.shortest_path(1,6)
        print(f"{x.id};MOVE {goto[1]} {goto[0]}")
    else:
        goto : list[int] = x.shortest_path(3,6)
        print(f"{x.id};MOVE {goto[1]} {goto[0]}")

def do_shot_tutorial(my_agent : Agent, id_other_agent : int):
    print(f"{my_agent.id};SHOOT {id_other_agent}")
    

def do_move_shot_tutorial(my_agent : Agent, all_agent : dict[int, Agent]):
    moves = my_agent.find_best_cell()
    print(f"{my_agent.id};MOVE {moves[1]} {moves[0]}; SHOOT {my_agent.who_attack(all_agent)}")

def do_bomb_tutorial(my_agent : Agent):
    tmp_line = my_agent.line
    tmp_column = my_agent.column
    moves : list[list[int]] = get_adjacent_cell(my_agent.line, my_agent.column, diagonal = False)
    to_remove : list[list[int]] = []
    for move in moves:
        if grid[move[0]][move[1]] != Tyle_Type.EMPTY:
            to_remove.append(move)
    for move in to_remove:
        moves.remove(move)
    goto : list[int]
    nb_ennemy : int = 0 
    prev : int = -1
    real_goto : list[int] = [-1, -1]
    good_move : list[int] = [-1, -1]
    for move in moves:
        my_agent.line = move[0]
        my_agent.column = move[1]
        goto, nb_ennemy = my_agent.send_bomb()
        print(f"{move=} {my_agent.id=} {goto=} {nb_ennemy=}", file=sys.stderr, flush=True)
        if nb_ennemy > prev and f"{my_agent.id},{str(good_move)},{str(real_goto)}" not in all_moves.keys():        
            real_goto = goto
            prev = nb_ennemy
            good_move = move
    if nb_ennemy <= 5:
        mini = 500
        all_ennemy = get_position_of_ennemy()
        my_agents_tmp = get_my_agents()
        good : Agent 
        good_ennemy : list[int]
        for  a in my_agents_tmp:
            if a.id != my_agent.id:
                good = a
        for enemy in all_ennemy:
            if good.manhattan_distance(enemy[0], enemy[1]) > 4:
                good_ennemy = enemy
        for move in moves:
            my_agent.line = move[0]
            my_agent.column = move[1]
            if my_agent.manhattan_distance(good_ennemy[0], good_ennemy[1]) < mini:
                print(f" on a rien donc le plus petit est peut être {move} car posotion ennemy = {good_ennemy}", file=sys.stderr, flush=True)
                good_move = move
                mini = my_agent.manhattan_distance(good_ennemy[0], good_ennemy[1])
    if nb_ennemy > 5:
        print(f"{my_agent.id};MOVE {good_move[1]} {good_move[0]}; THROW {real_goto[1]} {real_goto[0]}; MESSAGE {nb_ennemy}")
        all_moves[f"{my_agent.id},{str(good_move)},{str(real_goto)}"] = 1
    else:
        print(f"{my_agent.id};MOVE {good_move[1]} {good_move[0]}; MESSAGE {nb_ennemy}")
####


