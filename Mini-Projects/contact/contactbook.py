contact = {}


def display_contact():
    print(contact.items())
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key, contact.get(key)))


while True:
    choice = int(
        input(
            "1.Add new Contact \n 2.search contact \n 3. 3.Display contact\n 4. Edit contact \n 5. Delete contact\n 6.Exit\n Enter your choice "
        )
    )
    if choice == 1:
        name = input("Enter The Contact name")
        phone = input("Enter The Mobile Number")
        contact[name] = phone
    elif choice == 2:
        search_name = input("Enter the Contact Name ")
        if search_name in contact:
            print(search_name, "'s contact number is ", contact[search_name])
        else:
            print("Name is not Found inContact book")
    elif choice == 3:
        if not contact:
            print("empty Contact Book ")
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input("Enter the contact to be edited ")
        if edit_contact in contact:
            phone = input("enter Mobile Number")
            contact[edit_contact] = phone
            print("Contact Updated")
            display_contact()
        else:
            print("Name is Not Found in Contact book")
    elif choice == 5:
        del_contact = input("Enter the contact to be deleted")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n?")
            if confirm == "y" or confirm == "Y":
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in  Contact Book ")
    else:
        break
