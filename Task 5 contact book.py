class Contact:
    def __init__(self, store_name, phone, email, address):
        self.store_name = store_name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.store_name} | {self.phone} | {self.email} | {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, store_name, phone, email, address):
        new_contact = Contact(store_name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("Contacts List:")
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index}. {contact.store_name} - {contact.phone}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.store_name.lower() or search_term in contact.phone]
        if results:
            print("Search Results:")
            for contact in results:
                print(contact)
        else:
            print("No contact found.")

    def update_contact(self, index, store_name=None, phone=None, email=None, address=None):
        try:
            contact = self.contacts[index]
            contact.store_name = store_name if store_name else contact.store_name
            contact.phone = phone if phone else contact.phone
            contact.email = email if email else contact.email
            contact.address = address if address else contact.address
            print("Contact updated successfully!")
        except IndexError:
            print("Invalid index, contact not found.")

    def delete_contact(self, index):
        try:
            self.contacts.pop(index)
            print("Contact deleted successfully!")
        except IndexError:
            print("Invalid index, contact not found.")

def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    manager = ContactManager()
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            store_name = input("Enter store name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter physical address: ")
            manager.add_contact(store_name, phone, email, address)

        elif choice == "2":
            manager.view_contacts()

        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)

        elif choice == "4":
            manager.view_contacts()
            try:
                index = int(input("Enter the contact number to update: ")) - 1
                store_name = input("Enter new store name (leave blank to keep current): ")
                phone = input("Enter new phone number (leave blank to keep current): ")
                email = input("Enter new email address (leave blank to keep current): ")
                address = input("Enter new physical address (leave blank to keep current): ")
                manager.update_contact(index, store_name, phone, email, address)
            except ValueError:
                print("Invalid input, please enter a number.")

        elif choice == "5":
            manager.view_contacts()
            try:
                index = int(input("Enter the contact number to delete: ")) - 1
                manager.delete_contact(index)
            except ValueError:
                print("Invalid input, please enter a number.")

        elif choice == "6":
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
