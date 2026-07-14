# day 2

import json
import os

CONTACTS_FILE = "contacts.json"


class ContactManager:
    def __init__(self, filename=CONTACTS_FILE):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Load contacts from JSON file. Return {} if file doesn't exist."""
        
        pass

    def save_contacts(self):
        """Save self.contacts to the JSON file"""
        
        pass

    def add_contact(self, name, phone, email):
        """Add a new contact (name is the key)"""
        
        pass

    def search_contact(self, query):
        """Search contacts by name OR phone OR email (case-insensitive)"""
       
        pass

    def display_all(self):
        """Print all contacts neatly"""
        
        pass


def menu():
    manager = ContactManager()
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            manager.add_contact(name, phone, email)
        elif choice == "2":
            query = input("Search: ")
            print(manager.search_contact(query))
        elif choice == "3":
            manager.display_all()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()