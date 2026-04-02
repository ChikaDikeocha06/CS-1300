# ============================================
# PIZZA ORDER SYSTEM
# CS 1300 — Lecture 6 Lab
# ============================================
# ----- Menu Data (do not modify) -----

#Exersise 1--Display the Menu
 #Top border
print("=============================")
#Title
print("PIZZA SIZES".center(32))
#Another Border
print("=============================")
#A List of the content on the menu 
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
prices = [6.99, 9.99, 12.99, 16.99]

#A Loop to print list
for i in range(len(sizes)):
    print(i + 1, sizes[i], prices[i]) 
#Last Borderuser_choice
print("=============================")

# EXERCISE 2 — Get a valid size choice

#Pick a size (1-4): pizza
print("Pick Pizza size!")         
#Store the chosen index in a variable called size_choice (0-based) and the base price in base_price
#^^^^^Ask teacher what that means^^^^^
while True:
    user_size = int(input("Enter number 1-4: "))
    
    if 1 <= user_size <= 4:
        user_chosen_size = sizes[user_size - 1]
        print("Order Stored!")
        break
    else:
        print("Invalid Choice: ")
order_size_descriptions= []
order_size_descriptions.append( user_chosen_size)
order_descriptions= []
order_descriptions.append( user_chosen_size)

#Write code to equal the user size choice to the corresponding price and append the price to order_prices
user_size_index = user_size - 1  # Convert to 0-based index
user_size_price = prices[user_size_index]  # Get the base price from the prices list
order_size_prices=[]
order_size_prices.append(user_size_price)
# EXERCISE 3 — Add toppings
#Make a variable to store list of toppings
topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions","Sausage", "Bacon", "Extra Cheese", "Pineapple"]
# Display available toppings using a for loop
print("\nHere's our avaliable toppings!") 
#Another Border
print("=============================")
print("\nAvailable toppings ($1.50 each):")
#Another Border
print("=============================")
for i, topping in enumerate(topping_names, start=1): #enumerate to get index and value, start=1 to start counting from 1
    print(f"{i}. {topping}") #f-string to print the number and the topping name

#Another Border
print("=============================")

order_toppings_descriptions= []
#while loop to get user toppings until they type -1 to stop
user_toppings = 0
order_toppings_descriptions = []

while True:
    try:
        user_toppings = int(input("Add topping # (Type -1 to stop): "))
    except ValueError:
        print("Invalid choice")
        continue

    if user_toppings == -1:
        break

    if 1 <= user_toppings <= len(topping_names):
        chosen = topping_names[user_toppings - 1]
        if chosen in order_toppings_descriptions:
            print("Already added " + chosen + "!")
        else:
            print("✓ Added " + chosen)
            order_toppings_descriptions.append(chosen)
            order_descriptions.append(chosen)
    else:
        print("Invalid choice")
#write code to give the amount of toppings chosen a integer 
topping_price = 1.50 
num_toppings = len(order_toppings_descriptions)

# EXERCISE 4 — Calculate price and store the pizza
# Print the total cost and number of pizzas and toppings($1.50 each).
total= user_size_price + (num_toppings * topping_price)

# EXERCISE 5 — Wrap everything in a multi-pizza loop
# while True:
# (Exercise 1 — display menu)
# (Exercise 2 — choose size)
# (Exercise 3 — add toppings)
# (Exercise 4 — calculate and store)
#
# Ask "Order another?" with validation
#Reject anything else and re-prompt.
# If no, break

while True:
    order_another= input("Order another pizza? (yes/no): ").lower()
    if order_another == "yes" or order_another == "y":
        print("Starting new order...")
        # (Exercise 1 — display menu)
        print("=============================")
        print("PIZZA SIZES".center(32))
        print("=============================")
        for i in range(len(sizes)):
            print(i + 1, sizes[i], prices[i]) 
        print("=============================")
        # (Exercise 2 — choose size)
        while True:
            user_size = int(input("Enter number 1-4: "))
            if 1 <= user_size <= 4:
                print("Order Stored!")
                break
            else:
                print("Invalid Choice: ")
        # (Exercise 3 — add toppings)
        print("\nHere's our avaliable toppings!")
        print("=============================")  
        print("\nAvailable toppings ($1.50 each):")
        print("=============================")
        for i, topping in enumerate(topping_names, start=1):
            print(f"{i}. {topping}")
        print("=============================")
        user_toppings = int(input("Add topping # (Type -1 to stop): "))  
        while user_toppings != -1:
            try: #Try and Except to catch invalid input
                user_toppings = int(input("Add topping # (Type -1 to stop): "))  
            except ValueError:
                print("Invalid choice")
                continue
        if 1 <= user_toppings <= len(topping_names):
            chosen = topping_names[user_toppings - 1]
            if chosen in order_toppings_descriptions and chosen in order_descriptions:
                print("Already added " + chosen + "!")
            else:
                print("✓ Added " + chosen)
                order_toppings_descriptions.append(chosen)
                order_descriptions.append(chosen)
        else:
            print("Invalid choice")
    elif order_another == "no" or order_another == "n":
        print("Thank you for your order!")
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

# EXERCISE 6 — Print receipt
 #Top border
print("=============================")
#Title
print("YOUR ORDER RECEIPT".center(32))
#Another Border
print("=============================")
#Write a code to print all the user's choices appended to order_descriptions and order_prices using a for loop. Format the total price to 2 decimal places.
for i in range(len(order_descriptions)):
    print(f"{i + 1}. {order_size_descriptions[i]}, {order_toppings_descriptions[i]}")
    print(f"Total: ${total:.2f}")
