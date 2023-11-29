# write a python code that run the game rock paper scissors
# import random module
import random
# create a list of options
options = ["rock", "paper", "scissors"]
# create a variable to count the number of wins
wins = 0
# create a variable to count the number of losses
losses = 0
# create a variable to count the number of ties
ties = 0
# create a variable to store the user's choice
user_choice = ""
# create a variable to store the computer's choice
computer_choice = ""
# create a variable to store the outcome of the game
outcome = ""
# create a while loop that runs as long as the user wants to play
while True:
    # ask the user to choose an option
    user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
    # if the user's choice is not in the list of options
    if user_choice not in options:
        # raise an exception
        raise ValueError("Invalid option. Try again.")
    else:
        # randomly choose rock, paper, or scissors for the computer's choice
        computer_choice = random.choice(options)
        # write a python function that determines the outcome of the game
        if user_choice == computer_choice:
            outcome = "tie"
        elif user_choice == "rock":
            if computer_choice == "paper":
                outcome = "loss"
            else:
                outcome = "win"
        elif user_choice == "paper":
            if computer_choice == "scissors":
                outcome = "loss"
            else:
                outcome = "win"
        elif user_choice == "scissors":
            if computer_choice == "rock":
                outcome = "loss"
            else:
                outcome = "win"
        # print the outcome of the game
        print(f"User: {user_choice}")
        print(f"Computer: {computer_choice}")
        print(f"Outcome: {outcome}")
        # update the number of wins, losses, or ties
        if outcome == "win":
            wins += 1
        elif outcome == "loss":
            losses += 1
        elif outcome == "tie":
            ties += 1
        # ask the user if they want to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        # if the user does not want to play again
        if play_again != "y":
            # print the number of wins, losses, and ties if the user does not want to play again
            print(f"Wins: {wins}")
            print(f"Losses: {losses}")
            print(f"Ties: {ties}")
            # break the loop
            break