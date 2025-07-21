#Takes input for contacts: name, phone, age, city
#Store in a list of dictionaries
#Use type casting for age and phone
#Create functions: add_contact(), search_contact(), display_all()
#Use conditions to find contacts from specific cities or age > 30
#Check name validity using keyword module
#Use os.getcwd() to show file location
#Convert data to a tuple, then frozenset
#Display each contact's data type
#Log time of contact addition using datetime
import os
import datetime
import keyword
contacts = []
def add_contact():
    name = input("Enter name: ").strip()
    if keyword.iskeyword(name):
        print("Invalid name: It's a Python keyword.")
        return
    phone = (input("Enter phone num: "))
    age = int(input("Enter age: "))
    city = input("Enter city: ").strip()
    added_time = datetime.datetime.now()
    contact = {"name": name, "phone": phone, "age": age, "city": city, "added_time": added_time}
    contacts.append(contact)
    print(f"Contact for {name} added successfully at {added_time}. \n ")
def search_contact():
    search_name = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print("Contact found: ")
            print(contact)
            found = True
            break
    if not found:
        print("Contact not found. \n")
def display_all():
    if not contacts:
        print("No contacts to display. \n")
        return
    for i, contact in enumerate(contacts, 1):
        print(f"Contact {i}: ")
        print(contact)
        contact_tuple = tuple(contact.items())
        contact_frozenset = frozenset(contact_tuple)
        print(f"Frozenset: {contact_frozenset}")
        for key, value  in contact.items():
            print(f"Type of '{key}' is {type(value).__name__}")
def filter_contacts():
    print("Filter: Contacts from specific city or age > 30")
    city =input("Enter city to filter: ").lower()
    found = False
    for contact in contacts:
        if contact["city"].lower() == city or contact["age"] > 30:
            print(contact)
            found = True
    if not found:
        print("No matching contacts found.\n")
print("Current file location: ", os.getcwd())
print("=" *50)
while True:
    print("\n Contact manager menu")
    print("1. Add Contact: ")
    print("2. Search Contact: ")
    print("3. Display All Contacts: ")
    print("4. Filter Contacts (by city or age > 30)")
    print("5. Exit: ")
    choice = input("Enter your choice (1-5): ")
    if choice == '1' :
        add_contact()
    elif choice == '2' :
        search_contact()
    elif choice == '3' :
        display_all()
    elif choice == '4' :
        filter_contacts()
    elif choice == '5':
        print("Exiting Contact Manager.")
        break
    else:
        print("Invalid choice. Try again.")