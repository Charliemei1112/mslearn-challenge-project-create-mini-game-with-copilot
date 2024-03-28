import random

rounds = 0
score = 0
options = ['rock', 'paper', 'scissors']

while True:

    # Get the user's choice
    user_choice = input("Enter rock, paper, or scissors: ")
    user_choice = user_choice.lower()  # Convert the user's choice to lowercase
    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue

    # Get the computer's choice
    computer_choice = random.choice(options)

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print("You win!")
        score += 1
    elif user_choice == 'paper' and computer_choice == 'rock':
        print("You win!")
        score += 1
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print("You win!")
        score += 1
    else:
        print("You lose!")

    # Increment the number of rounds
    rounds += 1

    # Print the score
    # print(f"Score: {score}")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (Y/n) ")
    if play_again.lower() != 'y':
        print(f"Thanks for playing! You played {rounds} rounds and scored {score} points.")
        break