from __future__ import annotations
import sys
import math
from enum import Enum
from typing import Tuple
from copy import deepcopy
from typing import Optional


class Direction(Enum):
    NORTH = "N"
    NORTH_EAST = "NE"
    EAST = "E"
    SOUTH_EAST = "SE"
    SOUTH = "S"
    SOUTH_WEST = "SW"
    WEST = "W"
    NORTH_WEST = "NW"

    def getX(self):
        if "E" in self.value:
            return 1
        elif "W" in self.value:
            return -1
        return 0
    
    def getY(self):
        if "S" in self.value:
            return 1
        elif "N" in self.value:
            return -1
        return 0

    @staticmethod
    def create(x: str) -> 'Direction':
        try:
            return Direction(x)
        except ValueError:
            raise ValueError(f"Invalid direction: {x}")

    def __str__(self):
        return f"{self.value}"

class Unit:
    line: int
    column: int
    index : int

    def __init__(self, x, y, i):
        self.line = y
        self.column = x
        self.index = i

    def __str__(self):
        return f"{self.index}"

class Player:
    point : int
    who : int 

    def __init__(self, who : int):
        self.point = 0
        self.who = who

class Action:

    player : Player
    typeAction : str
    unit : Unit
    dir_movement : Direction 
    dir_construction : Direction 
    value : float = -1
    def __init__(self, t : str,u : Unit,d : Direction ,d2 : Direction, who : Player):
        self.typeAction = t
        self.unit = u
        self.dir_movement = d
        self.dir_construction = d2
        self.player = who

    def __str__(self):
        return f"ACTION(type={self.typeAction}, unit={self.unit}, move={self.dir_movement}, build={self.dir_construction})"

    def play_by_print(self) -> str:
        return (f"{self.typeAction} {self.unit} {self.dir_movement} {self.dir_construction}")
    
    def play(self, mat : list[list[str]]):
        if self.typeAction == "MOVE&BUILD":
            line, column = get_next_cell(self.unit, self.dir_movement)
            self.move(line, column)
            line, column = get_next_cell(self.unit, self.dir_construction)

        elif self.typeAction == "PUSH&BUILD":
            line, column = get_next_cell(self.unit, self.dir_movement)
            self.push(self.get_list_other_player())
        else:
            return

        increase_cell(mat, line, column) 
        return

    def undo(self, mat : list[list[str]]):
        if self.typeAction == "MOVE&BUILD":
            line, column = get_next_cell(self.unit, self.dir_construction)
            line1 = self.unit.line
            column1 = self.unit.column
            self.unmove(line1, column1)
        elif self.typeAction == "PUSH&BUILD":
            self.unpush(self.get_list_other_player())
            line, column = get_next_cell(self.unit, self.dir_movement)
        else:
            return

        increase_cell(mat, line, column, -1) 

    def move(self, line : int, column : int):
        
        self.unit.line = line
        self.unit.column = column
        return

    def unmove(self, line : int, column : int):
        self.unit.line -= self.dir_movement.getY()
        self.unit.column -= self.dir_movement.getX()
        return


    def get_list_other_player(self):
        if self.player.who == 0:
            return opponent_units
        return my_units

    def compute_value(self, mat : list[list[str]]) -> float:
        if self.typeAction == "MOVE&BUILD":
            return self.compute_value_construct(mat)
        elif self.typeAction == "PUSH&BUILD":
            return self.compute_value_push(mat)
        return -1

    def push(self, other_unit : list[Unit]):
        arrive_line, arrive_column = get_next_cell(self.unit, self.dir_movement)
        for unit in other_unit:
            if unit.line == arrive_line and unit.column == arrive_column:
                unit.line = arrive_line + self.dir_construction.getY()
                unit.column = arrive_column + self.dir_construction.getX()
                return

    def unpush(self, other_unit : list[Unit]):
        arrive_line, arrive_column = get_next_cell(self.unit, self.dir_movement)
        for unit in other_unit:
            if unit.line == arrive_line + self.dir_construction.getY() and unit.column == arrive_column + self.dir_construction.getX():
                unit.line = arrive_line
                unit.column = arrive_column
                return

    def compute_value_push(self, mat : list[list[str]]) -> float:

        arrive_line, arrive_column = get_next_cell(self.unit, self.dir_movement)
        value_arrive = get_value(mat, arrive_line, arrive_column)
        up_line, up_column = get_next_cell(self.unit, self.dir_construction)
        value_up = get_value(mat, up_line, up_column)

        self.value += value_arrive * mult_cell_next_value 
        self.value += value_arrive * mult_cell_next_up 
        self.value += len(get_cell_arround(mat,self.unit)) * mult_nb_cell_possible 
        self.value += get_value(mat, self.unit.line, self.unit.column) * mult_cell_current
        if len(get_cell_arround(mat, self.unit)) == 0:
            self.value -= 100
        if self.player.who == 0:
            other_unit = opponent_units
        else:
            other_unit = my_units
        
        self.look_other_pieces(mat, other_unit)
        if debug:
            print(f"on commence sur la case {self.unit.line} {self.unit.column}", file=sys.stderr, flush=True)
            print(f"on grandit la case {arrive_line} {arrive_column} de valeur {value_arrive} ", file=sys.stderr, flush=True)
            print(self.play_by_print(), self.value, file=sys.stderr, flush=True)
        self.value += 5 
        return self.value

    def compute_value_construct(self, mat : list[list[str]]) -> float:

        arrive_line, arrive_column = self.unit.line, self.unit.column
        value_arrive = get_value(mat, arrive_line, arrive_column)
        up_line, up_column = get_next_cell(self.unit, self.dir_construction)
        value_up = get_value(mat, up_line, up_column)

        self.value += value_arrive * mult_cell_next_value 
        self.value += value_up * mult_cell_next_up 
        self.value += len(get_cell_arround(mat,self.unit)) * mult_nb_cell_possible 
        if get_value(mat, self.unit.line, self.unit.column) == 3:
            self.value += 15
        self.look_other_pieces(mat)
        if debug:
            print(f"on commence sur la case {self.unit.line} {self.unit.column}", file=sys.stderr, flush=True)
            print(f"on est sur la case {arrive_line} {arrive_column} de valeur {value_arrive} ", file=sys.stderr, flush=True)
            print(self.play_by_print(), self.value, file=sys.stderr, flush=True)
        return self.value


    def look_other_pieces(self, mat, other_unit : list[Unit] = []):
        if self.player.who == 0:
            if other_unit == []:
                other_unit = opponent_units
            current_units = my_units
        else:
            if other_unit == []:
                other_unit = my_units
            current_units = opponent_units



        for unit in current_units:
            if unit == self.unit:
                continue
            self.value += len(get_cell_arround(mat, unit)) * mult_nb_cell_possible 
            self.value += get_value(mat, unit.line, unit.column) * mult_cell_current
            if (len(get_cell_arround(mat, unit)) * mult_nb_cell_possible) == 0:
                self.value -= 30

        for unit_ennemy in other_unit:
            if unit_ennemy == self.unit:
                continue
            self.value -= len(get_cell_arround(mat, unit_ennemy)) * mult_nb_cell_possible 
            self.value -= get_value(mat, unit_ennemy.line, unit_ennemy.column) * mult_cell_current * 3
            if (len(get_cell_arround(mat, unit_ennemy)) * mult_nb_cell_possible) == 0:
                self.value += 100

    def miniMax(self, depth, alpha, beta, maximize, mat) -> float:
        global my_units, opponent_units, x

        if depth == 0:
            if x % 100 == 0:
                print(f"je regarde pour la {x=} eme fois", file=sys.stderr, flush=True)
            x+= 1
            return self.compute_value(mat)


        next_actions = self.create_succesor(mat)
        if not next_actions:
            return self.compute_value(mat)

        if maximize:
            value = -math.inf
            for action in next_actions:
                action.play(mat)
                value = max(value, action.miniMax(depth - 1, alpha, beta, False, mat))
                action.undo(mat)
                alpha = max(alpha, value)
                if beta <= alpha:
                    break  # CUT

            return value
        else:
            value = math.inf
            for action in next_actions:
                action.play(mat)
                value = min(value, action.miniMax(depth - 1, alpha, beta, True, mat))
                action.undo(mat)
                beta = min(beta, value)

                if beta <= alpha:
                    break  # CUT

            return value


    def create_succesor(self, mat : list[list[str]]) -> list[Action]:
        units : list[Unit] = []
        if self.player.who == 0:
            units = opponent_units
        else:
            units = my_units
        
        next_action : list[Action] = []
        for unit in units:
            for move in Direction:
                if not can_move(mat, unit, move):
                    continue
                for create in Direction:
                    if can_up(mat, unit, create):
                        player_tmp = Player(1 - self.player.who)
                        next_action.append(Action("MOVE&BUILD", unit, move, create, player_tmp))
                        break
        return next_action      



def increase_cell(mat : list[list[str]], line : int, column : int, value = 1) -> None:
    if not is_valid_cell(line, column):
        return
    if mat[line][column] == '.':
        return 
    mat[line][column] = str(int(mat[line][column]) + value)


def get_cell_arround(mat: list[list[str]], unit : Unit) -> list[Tuple[int, int]]:
    result = []
    for move in Direction:
        if can_move(mat, unit, move):
            result.append([unit.line + move.getY(), unit.column + move.getX()])
            break
    return result
                                


def get_next_cell( unit : Unit, dir : Direction) -> Tuple[int, int]:
    cur_column = unit.column
    cur_line = unit.line
    move_line = dir.getY()
    move_column = dir.getX()
     
    arrive_line = cur_line + move_line
    arrive_column = cur_column + move_column
    return arrive_line, arrive_column

def is_valid_cell(line : int, column : int) -> bool:
    if column < 0 or line < 0 or line >= size or column >= size:
        return False
    return True

def can_move(mat : list[list[str]], unit : Unit, move : Direction) -> bool:
    arrive_line, arrive_column = get_next_cell(unit, move)
    if arrive_column < 0 or arrive_line < 0 or arrive_line >= size or arrive_column >= size:
        return False
    if get_value(mat, arrive_line, arrive_column) > 3:
        return False
    
    for other_unit in my_units:
        if arrive_line == other_unit.line and arrive_column == other_unit.column:
            return False
    for other_unit in opponent_units:
        if arrive_line == other_unit.line and arrive_column == other_unit.column:
            return False
    
    if get_value(mat, arrive_line, arrive_column) > get_value(mat, unit.line, unit.column) + 1:
        return False
    return get_value(mat, arrive_line, arrive_column) != -1


def can_up(mat : list[list[str]], unit : Unit, creat : Direction) -> bool:

    create_line, create_column = get_next_cell(unit, creat)    
    if create_column < 0 or create_line < 0 or create_line >= size or create_column >= size:
        return False
    if get_value(mat, create_line, create_column) > 3:
        return False
    for other_unit in my_units:
        if create_line == other_unit.line and create_column == other_unit.column:
            return False
    for other_unit in opponent_units:
        if create_line == other_unit.line and create_column == other_unit.column:
            return False

    return True

def can_play(mat : list[list[str]], unit : Unit, move : Direction, creat : Direction) -> bool:
    return can_move(mat, unit, move ) and can_up(mat, unit, creat)

def get_value(mat : list[list[str]], line : int, column : int) -> int:
    if not is_valid_cell(line, column) or mat[line][column] == '.':
        return -1
    return int(mat[line][column])


def init() -> int:
    global size
    size = int(input())
    units_per_player = int(input())
    return units_per_player


def main():
    units_per_player = init()
    launch_game(units_per_player)
    


def launch_game(units_per_player : int):
    global opponent_units, my_units, me
    opponent_units = []
    while True:
        board_game = []
        my_units = []
        for i in range(size):
            board_game.append(list(input()))
        for i in range(units_per_player):
            line = input().split()
            my_units.append(Unit(int(line[0]), int(line[1]), i))
        for i in range(units_per_player):
            line = input().split()
            if line[0] == "-1":
                continue
            else :
                if i == 0:
                    opponent_units = []
            opponent_units.append(Unit(int(line[0]), int(line[1]), i))
        nb_possible_actions = int(input())
        print("Debug messages...",nb_possible_actions, file=sys.stderr, flush=True)
        all_actions : list[Action] = []
        current_action: Optional[Action] = None
        for i in range(nb_possible_actions):
            inputs = input().split()
            all_actions.append(Action(inputs[0],my_units[int(inputs[1])],Direction.create(inputs[2]), Direction.create(inputs[3]), me))
            #all_actions[i].value = all_actions[i].miniMax(1, -math.inf, math.inf, True, board_game)
            all_actions[i].play(board_game)
            all_actions[i].value = all_actions[i].compute_value(board_game)
            all_actions[i].undo(board_game)

            if i == 0:
                current_action = all_actions[i]
            else:
                if current_action.value < all_actions[i].value:
                    current_action = all_actions[i]

        print(current_action.play_by_print())


mult_nb_cell_possible = 3
mult_cell_next_value = 6
mult_cell_next_up = -2
mult_cell_current = 3
debug = True
x = 0

size : int = 0
opponent_units : list[Unit] = []
me : Player = Player(0)
other : Player = Player(1)
my_units : list[Unit] = []
main()
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)






