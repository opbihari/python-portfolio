import csv
import os

csv_file = "contact.csv"

# Loading file
def load_contacts():
    contacts = {} # Initialize as a dictionary
    if os.path.isfile(csv_file):
        with open(csv_file, mode="r") as con_file:
            csv_PADH = csv.reader(con_file)
            next(csv_PADH, None) # Skip header row
            for line in csv_PADH:
                if line and len(line) == 4: # Ensure line is not empty
                    try:
                        contact_id = int(line[0])
                        contacts[contact_id] = {
                            "name": line[1],
                            "phone": line[2],
                            "email": line[3]
                        }
                    except ValueError:
                        print(f"skipping corrupt line {line}")
    return contacts

# Saving contact
def save_contacts(contacts):
    with open(csv_file, mode="w", newline="") as con_file:
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
    print(f"Contact {name} added successfully")
    view_contacts(contacts)

# Deleting contact
def delete_contact(contacts):
    try:
        contact_id = int(input("Enter the contact id to delete: "))
    except ValueError as val:
        print("ENTER NUMBER ONLY")
        return
    except Exception as e:
        print(e)
        return
    if contact_id in contacts:
        del contacts[contact_id]
        save_contacts(contacts)
        print(f"Contact {contact_id} deleted successfully")
        view_contacts(contacts)
    else:
        print(f"Contact {contact_id} not found")

# Viewing contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found")
    else:
        print("Contact List:")
        # Loop through contacts and print details
        for contact_id, contact_info in contacts.items():
            print(f"ID: {contact_id}, Name: {contact_info['name']}, Phone: {contact_info['phone']}, Email: {contact_info['email']}")

#finding contact
def find_contact(contacts):
    while True:
        
        print("how do you want to find contact  ")
        print("1. id")
        print("2. name")
        print("3. phone number")
        print("4. email ")
        print("5. return to main")
        try:   
            way_to_find = int(input("...."))
        except ValueError:
            print("enter only numbers from 1 to 5")
            continue
        if way_to_find == 1:
          while True:
                try:
                    contact_id = int(input("contact id  "))
                    break
                except ValueError:
                    print('try again')
          id_found = False
          if contact_id in contacts:
           info = (contacts[contact_id])
           print(f"\nFound -> ID: {contact_id}, Name: {info['name']}, Phone: {info['phone']}, Email: {info['email']}")
           id_found = True
          if not id_found:
              print(f"{contact_id} not found in contact")
        elif way_to_find == 2:
          name = input("enter the contact name").strip().lower()
          name_found = False
          for contact_id,info in contacts.items():
              if name in info['name'].lower():
                  print(f"id..{contact_id} \nname..{info['name']} \nphone number..{info['phone']} \nemail..{info['email']}")
                  name_found = True
          if not name_found:
              print(f"{name} not found in contact")
        elif way_to_find == 3:
            while True:
                
                phone_number = (input("phone number")).strip()
                if phone_number.isdigit():
                    break
                else: 
                    print("enter only digits ")
            phone_found = False
            for contact_id,info in contacts.items():

                if phone_number in info['phone']:
                    print("contact found")
                    print(f"id..{contact_id} \nname..{info['name']} \nPhone number..{info['phone']} \nemail..{info['email']}")
                    phone_found = True
            if not phone_found:
                print(f"{phone_number} not in contact")
        elif way_to_find == 4:
            email = input("enter the email").strip().lower()
            email_found = False
            for contact_id,info in contacts.items():
                if email in info['email'].lower():
                    print(f"{contact_id} \nname..{info['name']} \nPhone number..{info['phone']} \nemail..{info['email']}")
                    email_found = True
            if not email_found:
                print(f"{email} not found in contact")
        elif way_to_find == 5:
            print("returning to main menu")
            break
        else:
            continue


# Main area where all function will work
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. View Contacts")
        print("4. find contact")
        print("5. Exit")

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
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select from 1,2,3,4 ")
        except ValueError:
            print("enter the numbers only")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
