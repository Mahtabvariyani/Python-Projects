master_pwd = input("what is the master Password? ")


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user, passw = data.split("|")
            print('User :',user , "Password :", passw)


def add():
    name = input("Account Name: ") 
    pwd = input("password: ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input(
        "Would you like to add a new Password or view existing one ?(view,add),press q to quit "
    ).lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid Mode.")
    continue
