'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right.
'''
import random
while True:
    try:
        start = int(input("Enter start: "))
        break
    except ValueError:
        print("Enter int")
while True:
    try:
        end = int(input("Enter End num: "))
        if start > end:
            print("End to small")
            print("End = start + 10")
            end = start + 10
        break
    except ValueError:
        print("Enter int")
random_num = random.randrange(start,end+1)
while True:
    try:
        player_input = int(input(f"Enter number ({start}-{end}): "))
        if player_input > end :
            player_input = end
            print("Input was to high")
            print("Input set to end number")
        elif 1 > player_input:
            player_input = 1 
            print("Player input to small")
            print("Play input set to start number")
        break
    except ValueError:
        print("Enter int")
def Guess():
    if player_input == random_num:
        return "You won"
    elif player_input > random_num:
        return "Play input was greater than random number"
    else:
        return "Player input was less than random number"
print(Guess())
