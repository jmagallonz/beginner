# THIS PROJECT IS A GAME OF "ROCK, PAPER, SCISSORS, LIZARD, SPOCK"
# RULES:
# The game is an expansion on the game Rock, Paper, Scissors.
# Each player picks a variable and reveals it at the same time.
# The winner is the one who defeats the other. In a tie, the process is repeated until a winner is found.
# So:
#       Scissors cuts Paper
#       Paper covers Rock
#       Rock crushes Lizard
#       Lizard poisons Spock
#       Spock smashes Scissors
#       Scissors decapitates Lizard
#       Lizard eats Paper
#       Paper disproves Spock
#       Spock vaporizes Rock
#       (and as it always has) Rock crushes Scissors

import random

Options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]  # Options to choose from to play

Win_Statement = ["Scissors cuts Paper",
                 "Paper covers Rock",
                 "Rock crushes Lizard",
                 "Lizard poisons Spock",
                 "Spock smashes Scissors",
                 "Scissors decapitates Lizard",
                 "Lizard eats Paper",
                 "Paper disproves Spock",
                 "Spock vaporizes Rock",
                 "Rock crushes Scissors"]  # Winning statements go from 0 to 9 when you call them below.
# Also used for rules

Computer = random.choice(Options)  # Computer randomly selects an option to play

print("The rules are simple;", "\n".join(Win_Statement))  # Rules to play

print("Player, type one of the following options to play: ")

while True:  # Player to choose an option included in the "Options" list
    try:
        Player = input(Options).lower().title()  # Player to choose option from the list to play against computer
        # and put it in the right case.
        if Player in Options:  # If Player doesn't select an option included in the list, will have to choose again.
            print("Great, you chose", Player, "to play against the computer")
            break
        else:
            print("Please type an option from the list")
    except:
        break

while Computer == Player:  # If there's a draw, continue playing
    print("The computer also used", Player, ". It's a draw!")
    print("Try again")
    Computer = random.choice(Options)  # Computer randomly selects another option
    Player = input(Options)

if Computer != Player:  # Different options, who wins?
    print("Computer chose", Computer)
    if Player == "Rock":  # What happens if player chooses Rock
        if Computer == "Lizard" or "Scissors":
            if Computer == "Lizard":
                print(Win_Statement[2])
                print("You win!")
            if Computer == "Scissors":
                print(Win_Statement[9])
                print("You win!")
        if Computer == "Spock":
            print(Win_Statement[8])
            print("You lose!")
        if Computer == "Paper":
            print(Win_Statement[1])
            print("You lose!")
    if Player == "Paper":  # What happens if player chooses Paper
        if Computer == "Rock" or "Spock":
            if Computer == "Rock":
                print(Win_Statement[1])
                print("You win!")
            if Computer == "Spock":
                print(Win_Statement[7])
                print("You win!")
        if Computer == "Scissors":
            print(Win_Statement[0])
            print("You lose!")
        if Computer == "Lizard":
            print(Win_Statement[6])
            print("You lose!")
    if Player == "Scissors":  # What happens if player chooses Scissors
        if Computer == "Paper" or "Lizard":
            if Computer == "Paper":
                print(Win_Statement[0])
                print("You win!")
            if Computer == "Lizard":
                print(Win_Statement[5])
                print("You win!")
        if Computer == "Spock":
            print(Win_Statement[4])
            print("You lose!")
        if Computer == "Rock":
            print(Win_Statement[9])
            print("You lose!")
    if Player == "Lizard":  # What happens if player chooses Lizard
        if Computer == "Spock" or "Paper":
            if Computer == "Spock":
                print(Win_Statement[3])
                print("You win!")
            if Computer == "Paper":
                print(Win_Statement[6])
                print("You win!")
        if Computer == "Rock":
            print(Win_Statement[2])
            print("You lose!")
        if Computer == "Scissors":
            print(Win_Statement[5])
            print("You lose!")
    else:  # What happens if player chooses Spock
        if Computer == "Scissors" or "Rock":
            if Computer == "Scissors":
                print(Win_Statement[4])
                print("You win!")
            if Computer == "Rock":
                print(Win_Statement[8])
                print("You win!")
        if Computer == "Lizard":
            print(Win_Statement[3])
            print("You lose!")
        if Computer == "Paper":
            print(Win_Statement[7])
            print("You lose!")
