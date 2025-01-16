def display_menu():
    """Displays the menu options for the Shopping List Manager."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to manage the shopping list."""
    # Define the shopping list as an array (list in Python)
    shopping_list = []  

    while True:
        # Call the display_menu function to show options
        display_menu()

        # Implement choice input as a number
        try:
            choice = int(input("Enter your choice (1-4): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:  # Add item
            item = input("Enter the item to add: ").strip()
            if item:  # Ensure the input is not empty
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Item cannot be empty. Please try again.")

        elif choice == 2:  # Remove item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' is not in the shopping list. Cannot remove.")

        elif choice == 3:  # View list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is empty.")

        elif choice == 4:  # Exit
            print("Goodbye!")
            break

        else:  # Handle invalid choices
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
