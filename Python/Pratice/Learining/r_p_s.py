import random
playing = input("Are you playing (y/n)?: ").lower()
while playing == "y":
        computer_choice = random.choice(["paper","rock","scissors"])
        player_choice = input("(rock/paper/scissors) or (r/p/s): ").lower()
        if player_choice in ["r" , "rock"]:
            player_choice = "rock"
        elif player_choice in ["p" , "paper"]:
                player_choice = "paper"
        elif player_choice in ["s","scissors"]:
                player_choice = "scissors"
        else:
            print("Invaild Choice")
            print("Program closed")
            exit()
        if computer_choice == player_choice:
                print("Its a tie")
        elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or  (player_choice == "scissors" and computer_choice == "paper"):
                print("You won")
        else:
                print("The computer won")
        print(f"The computer choose {computer_choice}")
        playing = input("Are you playing (y/n)?: ").lower()
        if playing == "n":
            break
if playing == "n":
    input("Enter to close: ")
else:
      print("Invaild input")
      print("Program closed")
      exit()