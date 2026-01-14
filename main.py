# Contact Management System

contacts = {}

while True:
    print("\nContact Management Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully.")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for name, phone in contacts.items():
                print(f"Name: {name}, Phone: {phone}")

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"Phone number: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Exiting Contact Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
