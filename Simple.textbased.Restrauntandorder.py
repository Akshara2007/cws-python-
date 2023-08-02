menu = {    
    "Burger": 5.00,
    "Pizza": 10.00,
    "Salad": 7.00
}

order = []  

while True:
    print("\nWelcome to the restaurant!")
    print("1. View the menu")
    print("2. Add an item to the order")
    print("3. Calculate the total cost")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("\nMenu:")
        for item, price in menu.items():
            print(f"{item}: ${price:.2f}")
    elif choice == '2':  
        item = input("\nEnter the item you want to add: ")
        if item in menu:
            quantity = int(input("Enter the quantity: "))
            order.append((item, quantity))
            print(f"{quantity} {item}(s) added to the order.")
        else:
            print("Invalid item.")
    elif choice == '3':
        total_cost = 0
        for item, quantity in order:
            if item in menu:
                total_cost += menu[item] * quantity
        print(f"\nTotal cost: ${total_cost:.2f}")  
    elif choice == '4':
        print("Thank you for visiting the restaurant. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
