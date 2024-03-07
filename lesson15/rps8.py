#rock paper scissors

import sys
import random
from enum import Enum


def rps(name='PlayerOne'):
    game_count  = 0
    player_wins = 0
    pyhton_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal pyhton_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3


        print("")
        playerchoice = input(f"{name}, please enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")


        if playerchoice not in ["1","2","3"]:
            print(f"{name}, please enter 1, 2 or 3.")
            return play_rps()


        player = int (playerchoice)
        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print ("")
        print (f"{name} your choice  {str(RPS(player)).replace('RPS.','')}.")
        print (f"Python choice {str (RPS(computer)).replace('RPS.','')}.")
        print ("")

        def decide_winner(player,computer):
            nonlocal name
            nonlocal player_wins
            nonlocal pyhton_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return f"🥳 {name}, you win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🥳 {name}, you win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🥳 {name}, you win!"
            elif player ==  computer:
                return "🫡 Tie game!"
            else:
                pyhton_wins += 1
                return f"🐍 Python wins! \nSorry, {name}...😢"  
            
        game_result = decide_winner(player, computer)

        print (game_result)
        
        nonlocal game_count 
        game_count +=1

        print (f"\nGame count:  {game_count}")
        print (f"\n{name}'s wins: {player_wins}")
        print (f"\nPython wins: {pyhton_wins}")
        
        print(f"\n play again, {name}? ")

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
            sys.exit(f"Bye {name}!")

    return play_rps



if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience"
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True, help= "The name of the person playing the game"
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()