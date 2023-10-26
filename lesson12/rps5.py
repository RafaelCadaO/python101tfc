#rock paper scissors

import sys
import random
from enum import Enum


def rps():
    game_count  = 0
    player_wins = 0
    pyhton_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal pyhton_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3


        print("")
        playerchoice = input("Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")


        if playerchoice not in ["1","2","3"]:
            print("You must enter 1, 2 or 3.")
            return play_rps()


        player = int (playerchoice)
        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print ("")
        print ("Your choice "+ str(RPS(player)).replace('RPS.','') + ".")
        print ("Python choice "+ str (RPS(computer)).replace('RPS.','') + ".")
        print ("")

        def decide_winner(player,computer):
            nonlocal player_wins
            nonlocal pyhton_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return "🥳You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🥳You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🥳You win!"
            elif player ==  computer:
                return "🫡 Tie game!"
            else:
                pyhton_wins += 1
                return "🐍 Python wins!"  
            
        game_result = decide_winner(player, computer)

        print (game_result)
        
        nonlocal game_count 
        game_count +=1

        print ("\nGame count: " + str(game_count))
        print ("\nPlayer wins: " + str(player_wins))
        print ("\nPython wins: " + str(pyhton_wins))
        
        print("\n play again? ")

        while True:
            
            playagain = input("\nY for yes or \nQ to quit\n") 

            if playagain.lower() not in ["y","q"]:
                continue
            else: 
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print ("🥳🥳🥳")
            print ("Thank you")
            sys.exit("Byeee!")

    return play_rps

play = rps()
play ()