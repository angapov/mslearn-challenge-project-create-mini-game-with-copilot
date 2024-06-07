# Ask user's input to select from three options: 
# 1. rock
# 2. paper
# 3. scissors
# The computer will randomly select one of the three options.
# The winner is determined by the following rules:
# rock beats scissors
# scissors beats paper
# paper beats rock
# Print the winner.
# The program will continue to ask for user's input until the user types "quit"
# The program should inform the player if the option entered by the player is invalid.
# If the user chooses to quit the program will print the number of games played and the number of games won by the user.

import random

options = ["rock", "paper", "scissors"]
user_wins = 0
games_played = 0

while True:
    user_input = input("Enter your choice (rock, paper, scissors) or quit: ")
    if user_input == "quit":
        print(f"Games played: {games_played}")
        print(f"Games won: {user_wins}")
        break
    elif user_input not in options:
        print("Invalid option")
    else:
        computer_choice = random.choice(options)
        print(f"Computer choice: {computer_choice}")
        if user_input == computer_choice:
            print("It's a tie")
        elif user_input == "rock" and computer_choice == "scissors":
            print("You win!")
            user_wins += 1
        elif user_input == "scissors" and computer_choice == "paper":
            print("You win!")
            user_wins += 1
        elif user_input == "paper" and computer_choice == "rock":
            print("You win!")
            user_wins += 1
        else:
            print("Computer wins!")
        games_played += 1
