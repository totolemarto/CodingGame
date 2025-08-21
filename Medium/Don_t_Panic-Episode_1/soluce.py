import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
ascenseur = {}
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    ascenseur[elevator_floor] = elevator_pos
# game loop
if 0 not in ascenseur.keys():
    ascenseur[0] = -1
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])  # floor of the leading clone
    clone_pos = int(inputs[1])  # position of the leading clone on its floor
    direction = inputs[2]  # direction of the leading clone: LEFT or RIGHT
    if clone_floor == -1 :
        print("WAIT")
        continue
    if clone_floor == 0 and ascenseur[0] == -1:
        if clone_pos == width -1:
            print("BLOCK")
        else:
            print("WAIT")
    elif direction == "LEFT" and  clone_floor in ascenseur.keys() and clone_pos < ascenseur[clone_floor]:
        print("BLOCK") 
    elif direction == "RIGHT" and  clone_floor in ascenseur.keys() and clone_pos > ascenseur[clone_floor]:
        print("BLOCK") 
    elif clone_floor not in ascenseur.keys():
        if clone_pos <  exit_pos and direction == "LEFT" or clone_pos >  exit_pos and direction == "RIGHT" :
            print("BLOCK")
        else:
            print("WAIT")
    else:
        print("WAIT")
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # action: WAIT or BLOCK

