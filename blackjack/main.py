import random 
from art import logo
from play_the_game_function import play_the_game as game       
is_game_on = True
while is_game_on:
    print(logo)
    game()
    is_on = input("Want to play again ? y/n")
    if is_on == "y":
        is_game_on = True
    elif is_on == "n":
        break
    else:
        print("Invalid key entered exiting the game")
        break
    