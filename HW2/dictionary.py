cart = {0: "underwear", 1: "tank top", 2: "jacket"} # Initial items inside

while True:
    action = input("\nChange [R]emove [D]isplay [S]earch or *exit: ").lower()
    
    if action == "d":
        print("\nKey\tValue")
        for k, v in cart.items():
            print(f"{k}\t{v}")
            
    elif action == "s":
        item = input("Enter item to search: ")
        if item in cart.values():
            print(f"Found {item}")
        else:
            print("Item not in the cart")
            
    elif action == "r":
        key = int(input("Enter key to remove: "))
        if key in cart:
            print(f"Removed {cart[key]}")
            del cart[key]
        else:
            print("Key not found")
            
    elif action == "c":
        key = int(input("Enter key to change: "))
        if key in cart:
            cart[key] = input("Enter new value: ")
            print("Item updated")
        else:
            print("Key not found")
            
    elif action == "*":
        print("Bye")
        break
        
    else:
        print("Invalid option")
