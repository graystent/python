#Rock paper scissors
import random

user_score = 0
computer_score = 0

print("\nWelcome to the Rock, Paper, Scissors game!\nGood luck!\n")

while computer_score < 3 and user_score < 3:
    user_guess = input("rock, paper, scissors?\n")
    computer_guess = random.choice(["rock", "paper", "scissors"])
    print(computer_guess)
    if user_guess == computer_guess:
        print("Draw!")
        computer_score += 0
    elif user_guess == "rock" and computer_guess == "paper":
        print("Unlucky!")
        computer_score += 1
    elif user_guess == "scissors" and computer_guess == "rock":
        print("Unlucky!")
        computer_score += 1
    elif user_guess == "paper" and computer_guess == "scissors":
        print("Unlucky!")
        computer_score += 1
    elif user_guess == "scissors" and computer_guess == "paper":
        print("Winner!")
        user_score += 1
    elif user_guess == "paper" and computer_guess == "rock":
        print("Winner!")
        user_score += 1
    elif user_guess == "rock" and computer_guess == "scissors":
        print("Winner!")
        user_score += 1
    else:
        input("not an option, pick again")
    continue
if user_score == 3:
    print("\nYou are the Winner")
elif computer_score ==3:
    print("\nBoo, You are a Loser")
print("Game Over: User Score = " + str(user_score) + " Computer Score = " + str(computer_score))