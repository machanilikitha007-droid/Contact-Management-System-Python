contacts = {}


def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n===== CONTACT LIST =====")

    for name, contact in contacts.items():
        print("Name:", name)
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("-----------------------")


def search_contact():
    name = input("Enter Name to search: ")

    if name in contacts:
        contact = contacts[name]

        print("\nContact Found!")
        print("Name:", name)
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter Name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


while True:
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
