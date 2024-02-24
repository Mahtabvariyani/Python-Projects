import random


user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit  ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Its not a Valid input ")
        continue
    randon_number = random.randint(0, 2)
    computer_pick = options[randon_number]
    print("COmputer Pick", computer_pick, ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("you won")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you won")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("you won")
        user_wins += 1
    elif user_input == computer_pick:
        print("You and computer won")
    else:
        print("Computer wind")


print("Your wins:", user_wins)
print("Computer wins:", computer_wins)
print("Goodbye!")
