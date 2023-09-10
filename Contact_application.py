def phoneNumberChecker(num):
    # I must keep the return statement, return 0 if the number exists, else return 1
    # use in operator(membership operator) or list slicing

    with open("ContactsList.csv", "r") as f:
        l = f.readlines()  # l is a list

        for i in l:
            if num in i:
                return 0
            else:
                continue
        return 1


def createContact(num, name, email):
    # should not display contact updated successfully after updating the contact
    with open("ContactsList.csv", "a") as f:
        f.write(num + "," + name + "," + email + "\n")


def deleteContact(num):
    # it must return a list of number, name, email before deleting the contact
    # Must not display that contact deleted successfully message after deleting the contact
    l = []  # empty list

    with open("ContactsList.csv", "r") as f:
        l = f.readlines()

    for i in l:
        if num in i:
            ind = l.index(i)  # ind is the index
            num, name, email = i.split(",")
            break

    del l[ind]

    with open("ContactsList.csv", "w") as f:
        for i in l:
            f.write(i)

    return num, name, email


def displayAllContacts():
    # display all contacts
    print("Contact Details are: ")
    print("Mobile Number \t Contact Name \t, Email")
    with open("ContactsList.csv", "r") as f:
        l = f.readlines()
        for i in l:
            print(i)


def displaySingleContact(num):
    # return mobile number, name, email, number
    with open("ContactsList.csv", "r") as f:
        l = f.readlines()
        lst = []  # empty list
        for i in l:
            if num in i:
                lst = i.split(",")
                break

        return lst


# main function
while True:
    s = int(input("Enter your choice: \n1. Create Contact\n2. Update Contact\n3. Delete Contact\n4. Display All contacts\n5. Display single contact\n6. Exit\n"))
    if s == 1:
        # Create contact
        num = input("Enter the mobile number: ")
        check = phoneNumberChecker(num)  # phoneNumberChecker() returns 0 if the number exists, else return 1
        if check == 0:
            print(f"{num} already exists!!")
        elif check == 1:
            name = input("Enter the name: ")
            email = input("Enter the email: ")
            createContact(num, name, email)
            print("Contact created successfully.")

    elif s == 2:
        # Update contact
        num = input("Enter the mobile number: ")
        check = phoneNumberChecker(num)
        if check == 1:
            print(f"{num} contact does not exist to update!!")

        elif check == 0:
            num, name, email = deleteContact(num)  # list packing

            while True:
                n = int(
                    input("Enter your choice: 1. Update name\n2. update email\n3. update mobile number\n4. Exit\n"))
                if n == 1:
                    print(f"Old name: {name}")
                    name = input("Enter new name: ")

                elif n == 2:
                    print(f"Old email: {email}")
                    email = input("Enter new email: ")

                elif n == 3:
                    print(f"Old mobile number: {num}")
                    num = input("Enter new mobile number: ")

                elif n == 4:
                    print(f"Updated successfully for {num}")
                    break

                else:
                    print("Invalid choice!!. please enter the correct choice.")
            createContact(num, name, email)

    elif s == 3:
        # Delete contact
        num = input("Enter the mobile number: ")
        check = phoneNumberChecker(num)

        if check == 1:
            # contact doesn't exist
            print(f"{num} does not exist!!")

        elif check == 0:
            # contact exists
            num, name, email = deleteContact(num)
            print("Your details: \n")
            print(f"Name: {name}\nEmail: {email}\nMobile Number: {num}\n")
            print("Contact is deleted successfully")

    elif s == 4:
        # display all contacts
        displayAllContacts()

    elif s == 5:
        # display single contacts
        num = input("Enter the mobile number: ")
        check = phoneNumberChecker(num)

        if check == 1:
            # contact does not exist
            print(f"{num} does not exist!!")

        elif check == 0:
            # contact exists
            num, name, email = displaySingleContact(num)
            print(f"Contact name: {name}\t")
            print(f"Email: {email}\t")
            print(f"Mobile Number: {num}\n")

    elif s == 6:
        # Exit
        print("Thanks for using the contact file")
        break

    else:
        # invalid choice
        print("Invalid Choice!!. Please enter the correct choice.")
