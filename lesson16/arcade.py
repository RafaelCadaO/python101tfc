import sys
import rps
import guessnumber

def play_game(name='PlayerOne'):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to de Arcade menu.")

            playerchoice = input("\nPlase chose a game: \n1 = Rock Papers Scissors. \n2 = Guess my Number. \nx to exit the Arcade.")

            if playerchoice not in ["1","2","x"]:
                print(f"{name}, please enter 1, 2 or x.")
                return play_game(name)
            
            welcome_back = True

            if playerchoice == "1":
                rpsgame = rps.rps(name)
                rpsgame()
            elif playerchoice == "2":
                gmn_game = guessnumber.gn(name)
                gmn_game()
            else:
                print("\nSee you next time")
                sys.exit(f"Bye {name} 👍.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provides a personalized game experience")
    parser.add_argument('-n','--name',metavar='name',required=True,help='The name of the person playing the game.')