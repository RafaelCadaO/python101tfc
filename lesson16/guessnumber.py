import sys
import random


def gn(name='PlayerOne'):
    game_count  = 0
    player_wins = 0
    pyhton_wins = 0
    accuracy = 0

    def play_gn():
        nonlocal name
        nonlocal player_wins
        nonlocal pyhton_wins


        print("")
        playerchoice = input(f"{name}, guess which number un thinking on 1, 2 or 3\n\n")


        if playerchoice not in ["1","2","3"]:
            print(f"{name}, please enter 1, 2 or 3.")
            return play_gn()


        player = int (playerchoice)
        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print ("")
        print (f"{name} yor chose the number {player}.")
        print (f"Python was thinking the nunmber {computer}.")
        print ("")

        def decide_winner(player,computer):
            nonlocal name
            nonlocal player_wins
            nonlocal pyhton_wins

            if  player ==  computer:
                return f"{name} wins!!"
            else:
                pyhton_wins += 1
                return f"🐍 Python wins! \nSorry, {name}...😢"
            
        game_result = decide_winner(player, computer)

        print (game_result) 
        nonlocal game_count
        nonlocal accuracy
        game_count +=1
        accuracy = player_wins/game_count

        print (f"\nGame count:  {game_count}")
        print (f"\n{name}'s wins: {player_wins}")
        print (f"\nPython wins: {pyhton_wins}")
        print (f"\nAccuracy: {accuracy}%")
        


        
        print(f"\n play again, {name}? ")

        while True:
            
            playagain = input("\nY for yes or \nQ to quit\n") 

            if playagain.lower() not in ["y","q"]:
                continue
            else: 
                break

        if playagain.lower() == "y":
            return play_gn()
        else:
            print ("🥳🥳🥳")
            print ("Thank you")
            sys.exit(f"Bye {name}!")

    return play_gn



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

    guess_number = gn(args.name)
    guess_number()