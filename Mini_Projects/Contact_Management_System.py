"""
Contact Management System
Manage contacts (name, phone, email) with persistence via a CSV file.

Features:
  1. Add Contact
  2. Delete Contact  (by ID)
  3. View Contacts
  4. Exit

Data is saved to and loaded from contact.csv in the working directory.

Run:
    python Contact_Management_System.py
"""

import csv
import os

csv_file = "contact.csv"


# Loading file
def load_contacts():
    """Read contacts.csv and return a dict keyed by integer contact ID."""
    contacts = {}  # Initialize as a dictionary
    if os.path.isfile(csv_file):
        with open(csv_file, mode="r") as con_file:
            csv_PADH = csv.reader(con_file)
            next(csv_PADH, None)  # Skip header row
            for line in csv_PADH:
                if line:  # Ensure line is not empty
                    contact_id = int(line[0])
                    contacts[contact_id] = {
                        "name": line[1],
                        "phone": line[2],
                        "email": line[3],
                    }
    return contacts


# Saving contacts
def save_contacts(contacts):
    """Overwrite contact.csv with the current in-memory contacts dict."""
    with open(csv_file, mode="w", newline="") as con_file:
        csv_save = csv.writer(con_file)
        csv_save.writerow(["id", "name", "phone", "email"])
        for contact_id, contact_info in contacts.items():
            csv_save.writerow(
                [
                    contact_id,
                    contact_info["name"],
                    contact_info["phone"],
                    contact_info["email"],
                ]
            )


# Adding contact
def add_contact(contacts):
    """Prompt user for details, assign next available ID, persist and display."""
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email id: ")
    # Correctly get max key or set to 1 if contacts is empty
    contact_id = max(contacts.keys()) + 1 if contacts else 1
    contacts[contact_id] = {"name": name, "phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact {name} added successfully")
    view_contacts(contacts)


# Deleting contact
def delete_contact(contacts):
    """Remove a contact by its numeric ID and update the CSV."""
    contact_id = int(input("Enter the contact id to delete: "))
    if contact_id in contacts:
        del contacts[contact_id]
        save_contacts(contacts)
        print(f"Contact {contact_id} deleted successfully")
        view_contacts(contacts)
    else:
        print(f"Contact {contact_id} not found")


# Viewing contacts
def view_contacts(contacts):
    """Print all contacts with their ID, name, phone, and email."""
    if not contacts:
        print("No contacts found")
    else:
        print("Contact List:")
        # Loop through contacts and print details
        for contact_id, contact_info in contacts.items():
            print(
                f"ID: {contact_id}, "
                f"Name: {contact_info['name']}, "
                f"Phone: {contact_info['phone']}, "
                f"Email: {contact_info['email']}"
            )


# Main area where all functions will work
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. View Contacts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            delete_contact(contacts)
        elif choice == "3":
            view_contacts(contacts)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
