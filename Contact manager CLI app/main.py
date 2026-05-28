import pprint
import json

def add_contact(contacts_list, name, phone, email):
    """Creates a new contact dictionary and adds it to the list."""
    contact = {"name": name, "phone": phone, "email": email}
    contacts_list.append(contact)
    print("Contact added successfully!")

def view_contacts(contacts_list):
    """Displays all saved contacts."""
    if not contacts_list:
        print("No contacts found.")
    else:
        for contact in contacts_list:
            pprint.pprint(f"Name:{contact['name']}, Phone No.: {contact['phone']}, Email: {contact['email']}")

def delete_contact(contacts_list, name_to_delete):
    """Searches for a contact by name and removes it from the list."""
    for contact in contacts_list:
        if contact['name'].lower() == name_to_delete.lower():
            contacts_list.remove(contact)
            return
    print("Contact not found.")

def main():
    # Try to load existing contacts
    try:
        with open("contacts.json", "r") as file:
            my_contacts = json.load(file)
            print(f"Loaded {len(my_contacts)} saved contacts.")
    except FileNotFoundError:
        # If no file exists yet, start with an empty list
        print("No saved contacts found. Starting fresh.")
        my_contacts = [] 

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            name = input("Enter Contact name: ")
            phone = input("Enter Contact number: ")
            email = input("Enter Contact's Email id: ")
            add_contact(my_contacts, name, phone, email)
        elif choice == '2':
            view_contacts(my_contacts)
        elif choice == '3':
            ask = input("Enter the contact's name whos data you want to delete: ")
            delete_contact(my_contacts, ask)
        elif choice == '4':
            # Save the list of dictionaries to a JSON file
            with open("contacts.json", "w") as file:
                json.dump(my_contacts, file, indent=4) # indent=4 makes the file easily readable!
                
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()