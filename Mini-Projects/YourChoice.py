Welcome = print(
    "Hello to this game... This is a game where you can make your own chnages and decitions and every desiction will make a diffrence "
)

# Getting input values
name = input("What's your name? ")
age = input("What's your age? ")
choice = input("What do you prefer, jungle or sea? ")
fav_food = input("What's your favorite food? ")

# Creating a dictionary
user_info = {
    "name": name,
    "age": age,
    "preference": choice,
    "favorite_food": fav_food,
}

start = input(
    "as you like the sea story began in a sea, imagine you are in the sea the weather is bad you can to options fishing or eating concerve ,  which one do you perfer? "
).lower()


user_info["start"] = start


if "concerve" in start:
    print("Okay here is the pork concerve")
elif start == "fishing":
    print("Then start fishing :) ")
    fish = input("Tell me  what kind of fish you have got? ")


user_info["fish"] = fish


island = input(
    "after that you ate your fish your ship goes a bit furthur you see a island , what do you do ? will you go to the island ? yes or no ? "
).lower()

user_info["island"] = island

if island == "yes":
    print("You decide to go to the island.")
    print("As you approach the island, you notice a small dock where you can anchor your ship.")
    going_furthur =input("Do you want to explore the island further?")
else:
    print("You choose not to go to the island.")
    print("GAme Ends")
    
print("User Info:", user_info)




    

    

