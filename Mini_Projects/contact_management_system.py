import csv
import os

csv_file = "contact.csv"

# Loading file
def load_contacts():
    contacts = {} # Initialize as a dictionary
    if os.path.isfile(csv_file):
        with open(csv_file, mode="r", encoding="utf-8") as con_file:
            csv_PADH = csv.reader(con_file)
            next(csv_PADH, None) # Skip header row
            for line in csv_PADH:
                if line and len(line) == 4: # Ensure line is not empty and has all columns
                    try:
                        contact_id = int(line[0])
                        contacts[contact_id] = {
                            "name": line[1],
                            "phone": line[2],
                            "email": line[3]
                        }
                    except ValueError:
                        print(f"Skipping corrupt line {line}")
    return contacts

# Saving contact
def save_contacts(contacts):
    with open(csv_file, mode="w", newline="", encoding="utf-8") as con_file:
        csv_save = csv.writer(con_file)
        csv_save.writerow(["id", "name", "phone", "email"])
        for contact_id, contact_info in contacts.items():
            csv_save.writerow([
                contact_id,
                contact_info["name"],
                contact_info["phone"],
                contact_info["email"]
            ])

# Adding contact
def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email id: ")
    
    # Correctly get max key or set to 1 if contacts is empty
    contact_id = max(contacts.keys()) + 1 if contacts else 1
    contacts[contact_id] = {"name": name, "phone": phone, "email": email}
    
    save_contacts(contacts)
    print(f"\nContact '{name}' added successfully!")
    view_contacts(contacts)

# Deleting contact
def delete_contact(contacts):
    try:
        contact_id = int(input("Enter the contact ID to delete: "))
    except ValueError:
        print("Please enter numbers only.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
        
    if contact_id in contacts:
        del contacts[contact_id]
        save_contacts(contacts)
        print(f"\nContact ID {contact_id} deleted successfully.")
        view_contacts(contacts)
    else:
        print(f"\nContact ID {contact_id} not found.")

# Viewing contacts
def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
    else:
        print("\n--- Contact List ---")
        for contact_id, contact_info in contacts.items():
            print(f"ID: {contact_id} | Name: {contact_info['name']} | Phone: {contact_info['phone']} | Email: {contact_info['email']}")
        print("--------------------")

# Finding contact
def find_contact(contacts):
    while True:
        print("\nHow do you want to find a contact?")
        print("1. ID")
        print("2. Name")
        print("3. Phone number")
        print("4. Email")
        print("5. Return to main menu")
        
        try:   
            way_to_find = int(input("Enter choice: "))
        except ValueError:
            print("Please enter only numbers from 1 to 5.")
            continue
            
        # Option 1: ID
        if way_to_find == 1:
            while True:
                try:
                    contact_id = int(input("Enter contact ID: "))
                    break
                except ValueError:
                    print("Try again. Enter a valid number.")
            
            if contact_id in contacts:
                info = contacts[contact_id]
                print(f"\nFound -> ID: {contact_id}, Name: {info['name']}, Phone: {info['phone']}, Email: {info['email']}")
            else:
                print(f"\nID {contact_id} not found in contacts.")
                
        # Option 2: Name
        elif way_to_find == 2:
            name = input("Enter the contact name: ").strip().lower()
            name_found = False
            
            for contact_id, info in contacts.items():
                if name in info['name'].lower():
                    print(f"\nID: {contact_id} \nName: {info['name']} \nPhone number: {info['phone']} \nEmail: {info['email']}")
                    name_found = True
                    
            if not name_found:
                print(f"\nName '{name}' not found in contacts.")
                
        # Option 3: Phone
        elif way_to_find == 3:
            while True:
                phone_number = input("Enter phone number: ").strip()
                if phone_number.isdigit():
                    break
                else:
                    print("Please enter only digits.")
                    
            phone_found = False
            for contact_id, info in contacts.items():
                if phone_number in info['phone']:
                    print(f"\nID: {contact_id} \nName: {info['name']} \nPhone number: {info['phone']} \nEmail: {info['email']}")
                    phone_found = True
                    
            if not phone_found:
                print(f"\nPhone number '{phone_number}' not found in contacts.")
                
        # Option 4: Email
        elif way_to_find == 4:
            email = input("Enter the email: ").strip().lower()
            email_found = False
            
            for contact_id, info in contacts.items():
                if email in info['email'].lower():
                    print(f"\nID: {contact_id} \nName: {info['name']} \nPhone number: {info['phone']} \nEmail: {info['email']}")
                    email_found = True
                    
            if not email_found:
                print(f"\nEmail '{email}' not found in contacts.")
                
        # Option 5: Exit
        elif way_to_find == 5:
            print("Returning to main menu...")
            break
            
        else:
            print("Invalid choice. Please select from 1 to 5.")

#updating contacts
def update_contact(contacts):
    try:
        contact_id = int(input("Enter the contact ID to update:  "))
    except ValueError:
        print("Please enter numbers only.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    if contact_id in contacts:
        info = contacts[contact_id]
        print(f"id..{contact_id} \nname..{info['name']} \nphone number..{info['phone']} \nemail..{info['email']}")
        new_name = input("enter the name or press enter to move forward  ").strip().lower()
        new_number = input("enter phone number  or press enter to move forward  ").strip()
        new_email = input("enter email or press enter to move forward  ").strip()
        if new_name:
            info['name'] = new_name
        if new_number.isdigit():
            info['phone'] = new_number
        if new_email:
            info['email'] = new_email
        save_contacts(contacts)
        view_contacts(contacts)
    else:
        print(f"{contact_id} not found")
# Main loop
def main():
    contacts = load_contacts()
    while True:
        print("\n=== Contact Management System ===")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. View Contacts")
        print("4. Find Contact")
        print("5. update contact")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_contact(contacts)
            elif choice == 2:
                delete_contact(contacts)
            elif choice == 3:
                view_contacts(contacts)
            elif choice == 4:
                find_contact(contacts)
            elif choice == 5:
                update_contact(contacts)
            elif choice == 6:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select from 1, 2, 3, 4, 5.")
        except ValueError:
            print("Please enter numbers only.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()