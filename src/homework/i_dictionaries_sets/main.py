from dictionary import add_inventory

def delete_item(inventory, item):
    if item in inventory:
        del inventory[item]
        print(f"'{item}' has been deleted from the inventory.")
    else:
        print(f"'{item}' not found in the inventory.")

def display_menu():
    print("\nInventory Menu")
    print("1 - Add or Update Item")
    print("2 - Delete Item")
    print("3 - Exit")

def main():
    inventory = {}

    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            item = input("Enter item name: ").strip()
            try:
                quantity = int(input(f"Enter quantity for '{item}': "))
                add_inventory(inventory, item, quantity)
                print(f"Inventory updated: {item} now has quantity {inventory[item]}")
            except ValueError:
                print("Invalid quantity. Please enter an integer.")

        elif choice == '2':
            item = input("Enter item name to delete: ").strip()
            delete_item(inventory, item)

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == '__main__':
    main()




