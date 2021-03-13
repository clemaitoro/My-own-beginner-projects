contacts = {
    "marco": "+4073352110",
    "cristian": "+40727236332",
    "mama": "+40724686994",

}


def add_contacts(location=dict, name=str, number=int):
    """Adds a new contact to a specified `location`, `name` and phone
    `number`"""
    location[name] = number


while True:
    print("Your list consists of:")
    for key, value in contacts.items():
        print(key, value, sep=": ")
    print()
    call = input("Do you want to call, add or delete someone on your list \n"
                 "for a call press 1 \nto add someone press 2\nto delete someone "
                 "press 3\nto close the app press 0\n")

    if call == "1":
        who_to_call = input("Who do you want to call: ").casefold()
        if who_to_call in contacts:
            print(f"Calling {who_to_call}...")
            print()
        else:
            print("This person is not in your contact list, ")
            print()

    elif call == "2":
        person = input("What is the name of the contact: ")
        phone_number = int(input("What is the phone number of the person"
                                 "you want to add: "))
        add_contacts(contacts, person, phone_number)
        print()

    elif call == "3":
        contacts_to_delete = input("Who do you want to delete: ")
        if contacts_to_delete in contacts:
            contacts.pop(contacts_to_delete)
            print(f"{contacts_to_delete} has been removed from your list")
        else:
            print("The contact you want to delete is not on your list")
        print()

    elif call == "0":
        print("Thanks for using my app")
        break
