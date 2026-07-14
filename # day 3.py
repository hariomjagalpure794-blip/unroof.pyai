# day 3

import json
import os
import logging

CONTACTS_FILE = "contacts.json"
LOG_FILE = "contact_manager.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ContactNotFoundError(Exception):
    """Raised when a searched/updated contact doesn't exist"""
    pass


class DuplicateContactError(Exception):
    """Raised when adding a contact that already exists"""
    pass


class ContactManager:
    def __init__(self, filename=CONTACTS_FILE):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Load contacts from JSON. Handle missing/corrupted files gracefully."""
        if not os.path.exists(self.filename):
            logging.warning(f"{self.filename} not found. Starting with empty contacts.")
            return {}
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                logging.info("Contacts loaded successfully.")
                return data
        except json.JSONDecodeError:
            # TODO: log an error saying the file is corrupted
            # TODO: return an empty dict so the program doesn't crash
            pass

    def save_contacts(self):
        """Save contacts to JSON, handling write errors."""
        # TODO: wrap the open()+json.dump() in try/except IOError
        # TODO: log success with logging.info, failure with logging.error
        pass

    def add_contact(self, name, phone, email):
        """Add a contact, raising DuplicateContactError if it already exists."""
        # TODO: if name already in self.contacts -> raise DuplicateContactError
        # TODO: else add it, call save_contacts(), log an info message
        pass

    def search_contact(self, query):
        """Search contacts, raising ContactNotFoundError if nothing matches."""
        # TODO: search like Day 2, but if no matches found -> raise ContactNotFoundError
        pass

    def display_all(self):
        # TODO: if self.contacts is empty, log a warning + print a friendly message
        # TODO: otherwise print all contacts
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

        try:
            if choice == "1":
                name = input("Name: ").strip()
                phone = input("Phone: ").strip()
                email = input("Email: ").strip()
                if not name:
                    raise ValueError("Name cannot be empty")
                manager.add_contact(name, phone, email)
                print(f"Contact '{name}' added.")

            elif choice == "2":
                query = input("Search: ").strip()
                results = manager.search_contact(query)
                print(results)

            elif choice == "3":
                manager.display_all()

            elif choice == "4":
                logging.info("Program exited by user.")
                break

            else:
                print("Invalid choice")

        except DuplicateContactError as e:
            print(f"⚠️  {e}")
            logging.error(str(e))
        except ContactNotFoundError as e:
            print(f"⚠️  {e}")
            logging.warning(str(e))
        except ValueError as e:
            print(f"⚠️  Invalid input: {e}")
            logging.error(f"Invalid input: {e}")
        except Exception as e:
            print(f"⚠️  Unexpected error occurred. Check the log for details.")
            logging.critical(f"Unhandled exception: {e}")


if __name__ == "__main__":
    menu()