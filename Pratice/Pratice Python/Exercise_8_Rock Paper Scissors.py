'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''
import random
player_input = ""
while player_input not in "rock" or "paper" or "scissors": 
    player_input = input("Enter input (rock/paper/scissors): ").lower()
    if player_input in "rock" or "paper" or "scissors":
        break
    else:
        print("Enter('paper','rock','scissors')")
computer_input = random.randrange(1,3)
if computer_input == 0:
    computer_input = "rock"
elif computer_input == 1:
    computer_input = "scissors"
elif computer_input == 2:
    computer_input = "paper"
if player_input == "rock":
    if computer_input == "rock":
        print("Computer selected " + computer_input )
        print("You drew")
    elif computer_input == "paper":
        print("Computer selected " + computer_input )
        print("You lose")
    elif computer_input == "scissors ":
        print("Computer selected " + computer_input )
        print("You won")
elif player_input == "paper":
    if computer_input == "paper":
        print("The computer selected " + computer_input)
        print("You drew")
    elif computer_input == "rock":
        print("The computer selected " + computer_input)
        print("You won")
    elif computer_input == "scissors":
        print("The computer selected " + computer_input)
        print("You lost")
elif player_input == "scissors":
    if computer_input == "scissors":
        print("The computer selected " +  computer_input)
        print("You drew")
    elif computer_input == "rock":
        print("The computer selected " + computer_input)
        print("You lost")
    elif computer_input == "paper":
        print("The computer selceted " + computer_input)
        print("You won")
