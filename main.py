
from app.db import Database
from app.controllers import GroceryManager

def main():
    db = Database("sqlite:///grocery.db")
    manager = GroceryManager(db)

    while True:
        print("\nMenu:")
        print("1. Add Category")
        print("2. Add Item")
        print("3. Delete Category")
        print("4. Delete Item")
        print("5. Display All Categories")
        print("6. Display All Items")
        print("7. Find Item by Name")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter category name: ")
            manager.add_category(name)
        elif choice == "2":
            name = input("Enter item name: ")
            category_id = int(input("Enter category ID: "))
            manager.add_item(name, category_id)
        elif choice == "3":
            category_id = int(input("Enter category ID to delete: "))
            manager.delete_category(category_id)
        elif choice == "4":
            item_id = int(input("Enter item ID to delete: "))
            manager.delete_item(item_id)
        elif choice == "5":
            print("All Categories:")
            manager.display_all_categories()
        elif choice == "6":
            print("All Items:")
            manager.display_all_items()
        elif choice == "7":
            name = input("Enter item name to find: ")
            manager.find_item_by_name(name)
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
