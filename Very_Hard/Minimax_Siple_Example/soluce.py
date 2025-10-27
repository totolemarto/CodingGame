import sys
import math
from typing import Tuple
import traceback

class Player:
    letters : dict[str, int]
    name : int

    def __init__(self, letters, name):
        self.letters = letters
        self.name = name

def can_construct(player : dict[str, int], word : str) -> bool:
    for letter in word:
        if word.count(letter) > player[letter]:
            return False
    return True 

def my_heuristic(player_1 : dict[str, int], player_2 : dict[str, int], words : dict[str, int]) -> list[int]:
    result = [0, 0]
    for word, value in words.items():
        if  can_construct(player_1, word):
            result[0] +=  value
        if  can_construct(player_2, word):
            result[1] += value 
    all_result[result[0] * 100 + result[1] * 10] = [player_1.copy(), player_2.copy()]
    return result 


def mini(heuristic, heuristic_bis) -> bool:
    return not maxi(heuristic, heuristic_bis) 

def maxi(heuristic, heuristic_bis) -> bool:
    return heuristic[0] - heuristic[1] >= heuristic_bis[0] - heuristic_bis[1]

def other_func(a): 
    return maxi if a == mini else mini 

def minimax(words: dict[str, int], letters : list[str], player1: Player, player2: Player, alpha : list[float], beta : list[float], func, depth : int ) -> Tuple[int, list[int]]:
    player_current = player1.letters
    player_other = player2.letters
    if len(letters) == 1:
        player_current[letters[0]] += 1
        if player1.name == 1:
            tmp = my_heuristic(player_current, player_other, words)
        else:
            tmp = my_heuristic(player_other, player_current, words)
        player_current[letters[0]] -= 1
        return 0, tmp
    player_current[letters[0]] += 1
    _, heuristic = minimax(words, letters[1:], player2 , player1, alpha, beta, other_func(func), depth + 1)
    player_current[letters[0]] -= 1
    if func == mini:
        if maxi(alpha, heuristic):
            return 0, heuristic
        if maxi(beta, heuristic):
            beta = heuristic 
    else:
        if mini(beta, heuristic):
            return 0, heuristic
        if maxi(heuristic, alpha):
           alpha = heuristic 


     
    player_current[letters[1]] += 1
    tmp = letters.copy()
    tmp.pop(1)
    _, heuristic_bis = minimax(words, tmp, player2, player1, alpha, beta, other_func(func), depth + 1)
    player_current[letters[1]] -= 1
    if func(heuristic, heuristic_bis):
        return 0, heuristic
    else:
        return 1, heuristic_bis


def get_value() -> str:
    _, q = [int(i) for i in input().split()]
    letter_order : list[str] = []
    player_1 : dict[str, int] = {}
    player_2 : dict[str, int] = {}

    for letter in input().split():
        letter_order.append(letter)
        player_2[letter] = 0
        player_1[letter] = 0
        
    words : dict[str, int] = {}
    for i in range(q):
        inputs = input().split()
        words[inputs[0]] = int(inputs[1])
    Player1 = Player(player_1, 1)
    Player2 = Player(player_2, 2)
    letter, score = minimax(words, letter_order, Player1, Player2, [-math.inf, math.inf], [math.inf, -math.inf], maxi, 0)
    return f"{letter_order[letter]} {score[0]}-{score[1]}"

all_result : dict[int, list[dict[str, int]]] = {}
print(get_value())
