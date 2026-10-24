
import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Error reading contacts file.")
            return {}
    return {}


def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()

    if not name or not phone:
        print("Name and phone cannot be empty.")
    elif name in contacts:
        print("Contact already exists. Use Update instead.")
    else:
        contacts[name] = phone
        save_contacts()
        print("Contact added successfully.")


def search_contact():
    name = input("Enter name to search: ").strip()

    if name in contacts:
        print("Phone number:", contacts[name])
    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter name to update: ").strip()

    if name in contacts:
        phone = input("Enter new phone number: ").strip()

        if phone:
            contacts[name] = phone
            save_contacts()
            print("Contact updated successfully.")
        else:
            print("Phone number cannot be empty.")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        save_contacts()
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def show_contacts():
    if contacts:
        print("\n--- Saved Contacts ---")
        for name, phone in contacts.items():
            print(name, ":", phone)
    else:
        print("No contacts saved.")

contacts = load_contacts()

menu = {
    "1": add_contact,
    "2": search_contact,
    "3": update_contact,
    "4": delete_contact,
    "5": show_contacts
}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "6":
        print("Goodbye!")
        break

    action = menu.get(choice)

    if action:
        action()
    else:
        print("Invalid choice. Please try again.")
