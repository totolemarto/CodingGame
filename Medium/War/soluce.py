import sys
import math

def defiler(liste):
    x=liste[0]
    liste.remove(x)
    return x

def main():
    player1=[]
    player2=[]
    n = int(input())  # the number of cards for player 1
    for i in range(n):
        cardp_1 = input()  # the n cards of player 1
        cardp_1=cardp_1[:-1]
        player1.append(cardp_1)
    m = int(input())  # the number of cards for player 2
    for i in range(m):
        cardp_2 = input()  # the m cards of player 2
        cardp_2=cardp_2[:-1]
        player2.append(cardp_2)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
    liste=[1,2]
    manche=0
    cards = ["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    while len(player1)!=0 and len(player2)!=0:
        manche+=1
        card1=defiler(player1)
        card2=defiler(player2)
        if len(liste)==2:
            liste=[card1,card2]
        else:
            liste.insert(len(liste)//2,card1)
            liste.append(card2)
        if card1==card2:
            manche-=1
            x=len(liste)//2
            for i in range(3):
                liste.insert(x+i,defiler(player1))
                if len(player1)==0:
                    print("PAT")
                    return

            for i in range(3):
                liste.append(defiler(player2))
                if len(player2)==0:
                    print("PAT")
                    return

        elif cards.index(card1) > cards.index(card2):
            for elem in liste:
                player1.append(elem)
            if len(liste)!=2:
                liste=[1,2]

        else:
            for elem in liste:
                player2.append(elem)
            if len(liste)!=2:
                liste=[1,2]        

    if len(player1)==0:
        print(2,manche)
    else : print(1,manche)
main()
