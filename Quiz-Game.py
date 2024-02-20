print("Welcome to My Quiz")

playing = input("Do you want to play a game? ").lower()
if playing != "yes":
    quit()

print("Okay... Let's Play...!!!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    score -= 1

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    score -= 1

answer = input("What is the largest planet in our solar system? ")
if answer.lower() == "jupiter":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    score -= 1

answer = input("Who wrote 'Romeo and Juliet'? ")
if answer.lower() == "william shakespeare":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    score -= 1

answer = input("What is the chemical symbol for water? ")
if answer.lower() == "h2o":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    score -= 1

print("Your final Percentage is:", (score / 4) * 100, "%")
