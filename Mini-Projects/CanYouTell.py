import random


max_range = input("Type a Number")


if max_range.isdigit():
    max_range = int(max_range)

    if max_range <= 0:
        print("Write a number bigger than 0  next Time")
        quit()


num = random.randint( 0, max_range)

guesses = 0
while True:
    guesses += 1
    guess = input("Make a guess")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("please type a number next time ")
        continue

    if guess == num:
        print("You got it ")
        break
    else:
        print("You got it wrong")

print("you got it in the " , guesses , "guessess")