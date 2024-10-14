# Features:
# Main Menu (with loop and if-statements):
#
# Show options like Add Item, Update Stock, Search Item, Display Inventory, Exit.
# Add Item Function:
#
# Add an item with details like name, price, and stock.
# Store this information in a dictionary.
# Update Stock Function:
#
# Update the stock quantity of an item in the inventory.
# Search Item Function:
#
# Search for an item by name and display its details.
# Display Inventory Function:
#
# Display all items in the inventory with their details.

inventory = {}


def add_item(name, price, stock):
    inventory[name] = {'price': price, 'stock': stock}


def update_stock(name, stock):
    if name in inventory:
        inventory[name]['stock'] += stock
        print(f"Updated stock for {name}. New stock: {inventory[name]['stock']}")
    else:
        print(f"Item {name} not found in inventory.")


def search_item(name):
    if name in inventory:
        print(f"Item: {name}")
        print(f"Price: {inventory[name]['price']}")
        print(f"Stock: {inventory[name]['stock']}")
    else:
        print(f"Item {name} not found.")


def display_inventory():
    if inventory:
        for name, details in inventory.items():
            print(f"Item: {name}, Price: {details['price']}, Stock: {details['stock']}")
    else:
        print("Inventory is empty.")


while True:
    print("\n1. Add Item\n2. Update Stock\n3. Search Item\n4. Display Inventory\n5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item_name = input("Enter item name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock: "))
        add_item(item_name, price, stock)
    elif choice == 2:
        item_name = input("Enter item name: ")
        stock = int(input("Enter stock to add: "))
        update_stock(item_name, stock)
    elif choice == 3:
        item_name = input("Enter item name: ")
        search_item(item_name)
    elif choice == 4:
        display_inventory()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Try again.")
