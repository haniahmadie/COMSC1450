# This is a Inventory Stocking Project
import os

# Define the path to the inventory file
inventory_file = "inventory.txt"


def read_inventory():
    #Reads the inventory from the file and returns it as a list
    inventory = []
    if not os.path.exists(inventory_file):
        return inventory

    with open(inventory_file, "r") as file:
        for line in file.readlines()[1:]:  # Skip the header line
            name, qty, reorder_level = line.strip().split(", ")
            inventory.append({
                'name': name,
                'qty': int(qty),
                'reorder_level': int(reorder_level)
            })

    return inventory


def save_inventory(inventory):
    """Saves the updated inventory back to the file."""
    with open(inventory_file, "w") as file:
        file.write("name, qty, reorder_level\n")  # Write headers
        for item in inventory:
            file.write(f"{item['name']}, {item['qty']}, {item['reorder_level']}\n")


def add_new_item():
    """Adds a new item to the inventory."""
    name = input("Enter the name of the new item: ")

    qty = int(input(f"Enter the initial quantity of {name}: "))
    while qty<0:
       print("\033[31m\nALERT: Quantity cannot be negative.\033[0m")
       qty = int(input(f"Re-Enter quantity of {name}: "))
    else:
        reorder_level = int(input(f"Enter the reorder level for {name}: "))

    inventory = read_inventory()
    # Check if the item already exists
    for item in inventory:
        if item['name'].lower() == name.lower():
            print(f"Item '{name}' already exists in the inventory.")
            return

    # Add the new item to the inventory
    inventory.append({
        'name': name,
        'qty': qty,
        'reorder_level': reorder_level
    })

    save_inventory(inventory)
    print(f"Item '{name}' added successfully to the inventory.")


def update_inventory(item_name, quantity_change):
    #Updates the inventory for a specific item (can be positive for purchase, negative for usage)."""
    inventory = read_inventory()

    for item in inventory:
        if item['name'].lower() == item_name.lower():
            while -quantity_change>item['qty']:
                print("\033[31m\nALERT: Quantity on hand is less. Please renter your selection.\033[0m")
                break
            else:
                item['qty'] += quantity_change
                print(f"Updated {item_name}: New quantity = {item['qty']}")
            break
    else:
        print(f"Item '{item_name}' not found in inventory.")
        return

    save_inventory(inventory)


def purchase_items():
    """Handles purchasing of items (increases inventory)."""
    item_name = input("Enter the item name to purchase: ")
    quantity = int(input(f"Enter the quantity to purchase for {item_name}: "))
    while quantity<0:
       print("\033[31m\nALERT: Quantity cannot be negative.\033[0m")
       quantity = int(input(f"Re-Enter the quantity to purchase for {item_name}: "))
    else:
       update_inventory(item_name, quantity)


def use_items():
    #Handles usage of items (decreases inventory)."""
    item_name = input("Enter the item name to use: ")
    quantity = int(input(f"Enter the quantity to use for {item_name}: "))
    while quantity<0:
       print("\033[31m\nALERT: Quantity cannot be negative.\033[0m")
       quantity = int(input(f"Re-Enter the quantity to use for {item_name}: "))
    else:
       update_inventory(item_name, -quantity)


def check_restocking_needed():
    """Checks which items need restocking and returns a list of those items."""
    inventory = read_inventory()
    restocking_list = []

    for item in inventory:
        if item['qty'] <= item['reorder_level']:
            restocking_list.append(item['name'])

    return restocking_list


def print_restocking_alert():
    #Prints an alert for items that need restocking."""
    restocking_list = check_restocking_needed()

    if restocking_list:
        #print("\033[31mThis is red text\033[0m")
        print("\033[31m\nALERT: These items need restocking:\033[0m")
        for item in restocking_list:
            print(f"- {item}")
    else:
        print("\nNo items need restocking at the moment. \nAll items are above reorder thresholds.")


def display_inventory():
    #Displays the current inventory."""
    inventory = read_inventory()
    field1="Name"
    field2="Quantity"
    field3="Reorder Level"
    #print("\nCurrent Inventory:")
    print(f"\033[1;4m\nCurrent Inventory")
    print(f"\033[1;4m\n{field1:<20}{field2:<20}{field3:<20}\033[0m")
    #print(f"\n{field1:<20}{field2:<20}{field3:<20}")
    for item in inventory:
        #print(f"{item['name']}: Quantity = {item['qty']}, Reorder Level = {item['reorder_level']}")
        print(f"{item['name']:<20}{item['qty']:<20}{item['reorder_level']:<20}")


def main():
    os.system('clear')
    while True:
        
        #os.system('mode con: cols=200 lines=60')
        # add bold and underline to the title
        print("\033[1;4m\nInventory Restocking System\033[0m")
        print("1. List Inventory")
        print("2. Add New Item")
        print("3. Purchase Items")
        print("4. Use Items")
        print("5. Generate Restocking List")
        print("6. Exit")

        choice = input("\033[1m\n Choose an option (1-6): \033[0m")
        
        if choice == "1":
            os.system('clear')
            display_inventory()
        elif choice == "2":
            add_new_item()
        elif choice == "3":
            purchase_items()
        elif choice == "4":
            use_items()
        elif choice == "5":
            os.system('clear')
            print_restocking_alert()
        elif choice == "6":
            print("Exiting the Inventory System.")
            #os.system('mode con: cols=10 lines=1')
            break
        else:
            print("\033[31m\nInvalid choice. Please choose an option (1-6).\033[0m")


if __name__ == "__main__":
    main()
