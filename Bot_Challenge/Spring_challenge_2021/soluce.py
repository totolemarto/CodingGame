from __future__ import annotations
from enum import Enum
from random import randint
import sys
import math

liste_voisins = {
    0:[1,2,3,4,5,6],
    1:[0,2,6,7,8,18],
    2:[0,1,3,8,9,10],
    3:[0,2,4,10,11,12],
    4:[0,3,5,12,13,14],
    5:[0,5,6,14,15,16],
    6:[0,1,5,16,17,18],
    7:[1,8,18,19,20,36],
    8:[1,2,7,9,20,21],
    9:[2,8,10,21,22,23],
    10:[2,3,9,11,23,24],
    11:[3,10,12,24,25,26],
    12:[3,4,11,13,26,27],
    13:[4,12,14,27,28,29],
    14:[4,5,13,15,29,30],
    15:[5,14,16,30,31,32],
    16: [5, 6, 15, 17, 32, 33],
    17: [6, 16, 18, 33, 34, 35],
    18: [1, 6, 7, 17, 35, 36],
    19: [7, 20, 36],
    20: [7, 8, 19, 21],
    21: [8, 9, 20, 22],
    22: [9, 21, 23],
    23: [9,10, 22, 24],
    24: [10, 11, 23, 25],
    25: [11, 24, 26],
    26: [11, 12, 25, 27],
    27: [12, 13, 26, 28],
    28: [13, 27, 29],
    29: [13, 14, 28, 30],
    30: [14, 15, 29, 31],
    31: [15, 30, 32],
    32: [15, 16, 31, 33],
    33: [16, 17, 32, 34],
    34: [17, 33, 35],
    35: [17, 18, 34, 36],
    36: [7, 18, 19, 35]
}


class GameState:
    my_score : int
    opponent_score : int
    day : int
    nutrients : int
    my_sun : int
    opponent_sun : int
    number_of_trees : int
    opponent_is_waiting : bool

    def __init__(self, day : int, nutrients : int, sun : int, score : int,
                 opp_sun : int, opp_score : int, number_of_trees : int, waiting : bool):
        self.my_score = score
        self.opponent_score = opp_score
        self.day = day
        self.nutrients = nutrients
        self.my_sun = sun
        self.opponent_sun = opp_sun
        self.number_of_trees = number_of_trees
        self.opponent_is_waiting = waiting
    

class Cell():
    richness : int
    neigh : list[int]
    accessible_by_2 : list[int]
    accessible_by_3 : list[int]
    index : int

    def __init__(self, richness : int, neigh : list[int], index : int):
        self.richness = richness
        self.neigh = neigh
        self.accessible_by_3 = []
        self.accessible_by_2 = []
        self.index = index

    def compute_neigh_far(self, other : list[Cell]) -> None:
        for index in self.neigh:
            if index == -1:
                continue
            for neight_2 in other[index].neigh:
                if neight_2 == -1:
                    continue
                if neight_2 != self.index and neight_2 not in self.neigh and neight_2 not in self.accessible_by_2:
                    self.accessible_by_2.append(neight_2)
        for index in self.accessible_by_2:
            if index == -1:
                continue
            for neight_3 in other[index].neigh:
                if neight_3 == -1:
                    continue
                if neight_3 != self.index and neight_3 not in self.neigh and neight_3 not in self.accessible_by_2 and neight_3 not in self.accessible_by_3:
                    self.accessible_by_3.append(neight_3)

    def get_points_complete(self) -> int:
        match self.richness:
            case 0:
                return 0
            case 1:
                return 0
            case 2:
                return 2
            case 3:
                return 4
        return 0

class Tree():
    is_mine : bool
    cell : Cell
    size : int
    is_dormant : bool
    shadow_cell : None | list[int]

    def __init__(self, is_mine : bool, cell : Cell, size : int, is_dormant : bool):
        self.is_mine = is_mine
        self.cell = cell
        self.size = size
        self.is_dormant = is_dormant
        self.shadow_cell = None
    
    def set_shadow_cell(self):
        if self.shadow_cell is not None:
            return
        cur_day = current_state.day % 6
        self.shadow_cell = []
        if self.size > 0:
            self.shadow_cell.append(self.cell.neigh[cur_day])
        if self.size > 1:
            self.shadow_cell.append(all_cell[self.cell.neigh[cur_day]].neigh[cur_day])
        if self.size > 2:
            self.shadow_cell.append(all_cell[all_cell[self.cell.neigh[cur_day]].neigh[cur_day]].neigh[cur_day])
   

class Move():
    type : str
    tree : int
    seed : int
    cost : int
    tmp_seed : Tree
    tree_class : Tree | None

    def __init__(self, type_move : str, tree : int, cost : int, seed : int = 0, tree_class = None):
        self.type = type_move
        self.tree = tree
        self.seed = seed
        self.cost = cost
        self.tree_class = tree_class

    def __str__(self) -> str:
        return f"{self.type=} {self.tree=} {self.seed=} {self.cost=}"

    def play_by_print(self):
        match(self.type):
            case "GROW" | "COMPLETE":
                print(f"{self.type} {self.tree}")
            case "SEED":
                print(f"{self.type} {self.tree} {self.seed}")
            case "WAIT":
                print("WAIT")


    def do(self) -> None:
        match(self.type):
            case "GROW":
                self.tree_class.shadow_cell = None
                self.tree_class.size+= 1
                self.tree_class.is_dormant = True
            case "SEED":
                self.tree_class.is_dormant = True
                self.tmp_seed = Tree(self.tree_class.is_mine, all_cell[self.seed], 0, True)
                trees.append(self.tmp_seed)
            case "WAIT":
                return 
            case "COMPLETE":
                trees.remove(self.tree_class)
                if (self.tree_class.is_mine):
                    current_state.my_score += current_state.nutrients + self.tree_class.cell.get_points_complete()
                else:
                    current_state.opponent_score += current_state.nutrients + self.tree_class.cell.get_points_complete()
                current_state.nutrients -= 1

        if (self.tree_class.is_mine):
            current_state.my_sun -= self.cost
        else:
            current_state.opponent_sun -= self.cost

    def undo(self) -> None:
        match(self.type):
            case "GROW":
                self.tree_class.shadow_cell = None
                self.tree_class.is_dormant = False 
                self.tree_class.size -= 1
                pass
            case "SEED":
                self.tree_class.is_dormant = False 
                trees.remove(self.tmp_seed)
                pass
            case "WAIT":
                return
            case "COMPLETE":
                trees.append(self.tree_class)
                current_state.nutrients+= 1
                if (self.tree_class.is_mine):
                    current_state.my_score -= current_state.nutrients + self.tree_class.cell.get_points_complete()
                else:
                    current_state.opponent_score -= current_state.nutrients + self.tree_class.cell.get_points_complete()

        if (self.tree_class.is_mine):
            current_state.my_sun += self.cost
        else:
            current_state.opponent_sun += self.cost


def get_amount_of_sun_win(is_me : bool) -> int:
    result : int = 0
    shadow_cell : list[int] = []
    for tree in trees: 
        if tree.is_mine != is_me:
            tree.set_shadow_cell()
            shadow_cell.extend(tree.shadow_cell)
    for tree in trees:
        if tree.is_mine == is_me and tree.cell.index not in shadow_cell:
            result += tree.size 
    return result

def is_empty_cell(index : int) -> bool:
    if all_cell[index].richness == 0:
        return False
    for other_tree in trees:
        if other_tree.cell.index == index:
            return False
    return True

def has_enought_sun(is_me : bool, cost : int) -> bool:
    if  (is_me and cost > current_state.my_sun) or (not is_me and cost > current_state.opponent_sun) :
        return False
    return True

def seed_move(tree : Tree, is_me : bool) -> list[Move]:
    result : list[Move] = []  
    cost = get_number_tree_by_size(0, is_me) 
    if not has_enought_sun(is_me, cost): 
        return []
    if tree.size > 0:
        for index in tree.cell.neigh:
            if index == -1:
                continue
            if is_empty_cell(index):
                result.append(Move("SEED", tree.cell.index, cost, seed=index, tree_class=tree))
    if tree.size > 1:
        for index in tree.cell.accessible_by_2:
            if is_empty_cell(index):
                result.append(Move("SEED", tree.cell.index, cost, seed=index, tree_class=tree))
    if tree.size > 2:
        for index in tree.cell.accessible_by_3:
            if is_empty_cell(index):
                result.append(Move("SEED", tree.cell.index, cost, seed=index, tree_class=tree))
    result = sorted(result, key=lambda t: t.tree_class.cell.richness)
    return result

def grow_move( tree : Tree, is_me : bool) -> list[Move]:
    result : list[Move] = []
    if tree.size == 3:
        return result
    cost : int = get_number_tree_by_size(tree.size + 1, is_me)
    match tree.size:
        case 0:
            cost+= 1
        case 1:
            cost+= 3
        case 2:
            cost+= 7
    if not has_enought_sun(is_me, cost):
        return []
    return [Move("GROW", tree.cell.index, cost, tree_class=tree)]

def complete_move(tree: Tree, is_me : bool) -> list[Move]:
    result : list[Move] = []
    if tree.size != 3 or not has_enought_sun(is_me, 4):
        return result 
    return [Move("COMPLETE", tree.cell.index, 4, tree_class=tree)]

def get_number_tree_by_size(size: int, is_me: bool) -> int:
    result : int = 0
    for tree in trees:
        if tree.is_mine == is_me:
            if tree.size == size:
                result+= 1
    return result


def get_all_move(is_me : bool) -> list[Move]:
    result : list[Move] = []
    result.append(Move("WAIT",0,0))
    for tree in trees:
        if tree.is_dormant or tree.is_mine != is_me:
            continue
        result.extend(complete_move(tree, is_me))
        result.extend(seed_move(tree, is_me))
        result.extend(grow_move(tree, is_me))
    return result

def less( best : float, cur : float) -> bool: return best < cur
def more( best : float, cur : float) -> bool: return best > cur

def min_max(depth : int, isMaximizingPlayer : bool, first : bool = True,  alpha: float = -math.inf, beta: float = math.inf ) -> Move | float:
    if depth == 0:
        return float(heuristic())
    if isMaximizingPlayer:
        bestScore = -math.inf
        comparator = less
    else:
        bestScore = math.inf
        comparator = more 
    tmp : Move 
    for move in get_all_move(isMaximizingPlayer):
        move.do()
        #print(move, file=sys.stderr)
        score = min_max(depth - 1, not isMaximizingPlayer, False, alpha, beta)
        move.undo()
        if comparator(bestScore, float(score)):
            bestScore = score
            tmp = move
        if isMaximizingPlayer:
            alpha = max(alpha, bestScore)
        else:
            beta = min(beta, bestScore)
        if beta <= alpha:
            break 
    if not first:
       return float(bestScore)
    return tmp 

def heuristic() -> int:
    result : int  = 0
    result += current_state.my_score * (current_state.day + 11)
    result -= current_state.opponent_score  * (current_state.day + 11)
    result += (get_amount_of_sun_win(True) * 75) + current_state.my_sun
    result -= (get_amount_of_sun_win(False) * 75) + current_state.opponent_sun
    if current_state.day == 23:
        result += (current_state.my_sun // 3) * 24
        result -= (current_state.opponent_sun // 3) * 24
    if current_state.day > 18:
        result -= get_number_tree_by_size(0, True) * 7
        result += get_number_tree_by_size(0, False) * 7
    if current_state.day > 20:
        result -= get_number_tree_by_size(1, True) * 7
        result += get_number_tree_by_size(1, False) * 7
    if current_state.day > 22:
        result -= get_number_tree_by_size(2, True)  * 7
        result += get_number_tree_by_size(2, False) * 7
    for tree in trees:
        mult = 5 * tree.cell.richness
        if tree.cell.richness == 3:
            mult = 8 * tree.cell.richness
        if tree.is_mine:
            if tree.size == 0 and current_state.day > 20:
                continue
            if tree.size == 1 and current_state.day > 21:
                continue
            if tree.size == 2 and current_state.day > 22:
                continue
            result += mult * (tree.size + 1)
        else:
            if tree.size == 0 and current_state.day > 20:
                continue
            if tree.size == 1 and current_state.day > 21:
                continue
            if tree.size == 2 and current_state.day > 22:
                continue
            result -= mult * (tree.size + 1)
     
    #print(f" dans heuristique {result=}", file=sys.stderr)
    return result


def init_map() -> list[Cell]:
    number_of_cells = int(input())  # 37
    result : list[Cell] = [None] * number_of_cells
    for i in range(number_of_cells):
        # index: 0 is the center cell, the next cells spiral outwards
        # richness: 0 if the cell is unusable, 1-3 for usable cells
        # neigh_0: the index of the neighbouring cell for each direction
        index, richness, *neigh = [int(j) for j in input().split()]
        result[index] = Cell(richness, neigh, index)  
    for elem in result:
        elem.compute_neigh_far(result)
    return result

def get_game_state() -> GameState:
    day = int(input())  # the game lasts 24 days: 0-23
    nutrients = int(input())  # the base score you gain from the next COMPLETE action
    # sun: your sun points
    # score: your current score
    sun, score = [int(i) for i in input().split()]
    inputs = input().split()
    opp_sun = int(inputs[0])  # opponent's sun points
    opp_score = int(inputs[1])  # opponent's score
    opp_is_waiting = inputs[2] != "0"  # whether your opponent is asleep until the next day
    number_of_trees = int(input())  # the current amount of trees
    result : GameState = GameState(day, nutrients, sun, score, 
                                   opp_sun, opp_score, number_of_trees, opp_is_waiting)
    return result


def get_trees(number_of_trees : int) -> list[Tree]:
    result : list[Tree] = []
    for _ in range(number_of_trees):
        inputs = input().split()
        cell_index = int(inputs[0])  # location of this tree
        size = int(inputs[1])  # size of this tree: 0-3
        is_mine = inputs[2] != "0"  # 1 if this is your tree
        is_dormant = inputs[3] != "0"  # 1 if this tree is dormant
        result.append(Tree(is_mine, all_cell[cell_index], size, is_dormant))
    return result


all_cell : list[Cell] = init_map()
while True:
    current_state : GameState = get_game_state()
    trees : list[Tree] = get_trees(current_state.number_of_trees)
    
    trees = sorted(trees, key=lambda tree: tree.cell.richness)
    number_of_possible_actions = int(input())  # all legal actions
    for i in range(number_of_possible_actions):
        input()  # try printing something from here to start with
    if current_state.day < 8:
        min_max(3, True).play_by_print()
    else:
        min_max(2, True).play_by_print()
    # GROW cellIdx | SEED sourceIdx targetIdx | COMPLETE cellIdx | WAIT <message>



