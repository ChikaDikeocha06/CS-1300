# ============================================
# PIZZA ORDER SYSTEM
# CS 1300 — Lecture 6 Lab
# ============================================
# ----- Menu Data (do not modify) -----

#Exersise 1--Display the Menu
 #Top border
width = 36
print("=" * width)
#Title
print("PIZZA SIZES".center(width))
#Another Border
print("=" * width)
#A List of the content on the menu 
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
prices = [6.99, 9.99, 12.99, 16.99]
 # ----- Order Storage -----
order_descriptions = [] # e.g., "Large Pepperoni, Mushrooms"
order_prices = [] # e.g., 15.99

#A Loop to print list
for i in range(len(sizes)):
    print(f"{i + 1}. ", f"{sizes[i]}", "\t" f"{prices[i]}") 
#Last Borderuser_choice
print("=" * width)

# EXERCISE 2 — Get a valid size choice

#Pick a size (1-4): pizza
print("Pick Pizza size!")         
#Store the chosen index in a variable called size_choice (0-based) and the base price in base_price
order_size_descriptions= []
order_descriptions= []

user_size= 0
while True:
    user_size = int(input("Enter number 1-4: "))
    if 1 <= user_size <= 4:
        user_chosen_size = sizes[user_size - 1]
        print("Order Stored!")
        order_size_descriptions.append(user_chosen_size)
        #Write code to equal the user size choice to the corresponding price and append the price to order_prices
        user_size_index = user_size - 1  # Convert to 0-based index
        user_size_price = prices[user_size_index]  # Get the base price from the prices list
        order_size_prices=[]
        order_size_prices.append(user_size_price)
        break
    else:
        print("Invalid Choice: ")

# EXERCISE 3 — Add toppings
#Make a variable to store list of toppings
topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions","Sausage", "Bacon", "Extra Cheese", "Pineapple"]
# Display available toppings using a for loop
print("\nHere's our avaliable toppings!") 
#Another Border
print("=" * width)
print("Available toppings ($1.50 each):")
#Another Border
print("=" * width)
for i, topping in enumerate(topping_names, start=1): #enumerate to get index and value, start=1 to start counting from 1
    print(f"{i}. {topping}") #f-string to print the number and the topping name

#Another Border
print("=" * width)

#while loop to get user toppings until they type -1 to stop
user_toppings = []
order_toppings_descriptions = []
topping_price = 1.50
total_toppings = 0
while True:
    try:
        user_toppings = int(input("Add topping # (Type -1 to stop): "))
    except ValueError:
        print("Invalid choice")
        continue
    if user_toppings == -1:
        total_toppings == total_toppings
        break
    if 1 <= user_toppings <= len(topping_names):
        chosen = topping_names[user_toppings - 1]
        if chosen in order_toppings_descriptions:
            print("Already added " + chosen + "!")
        else:
            print("✓ Added " + chosen)
            order_toppings_descriptions.append(chosen)
            total_toppings +=1
    else:
        print("Invalid choice")
#write code to give the amount of toppings chosen a integer 
        user_size_index = user_size - 1
        user_size_price = prices[user_size_index]

# EXERCISE 4 — Calculate price and store the pizza
# Print the total cost and number of pizzas and toppings($1.50 each).
total_toppings = len(order_toppings_descriptions)
total = user_size_price + (total_toppings * topping_price)
toppings_str = ", ".join(order_toppings_descriptions) if order_toppings_descriptions else "No toppings"

pizza_description = f"{sizes[user_size_index]}\n{toppings_str}"

order_descriptions.append(pizza_description)
order_prices.append(total)
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
        print("=" * width)
        print("PIZZA SIZES".center(32))
        print("=" * width)
        for i in range(len(sizes)):
            print(i + 1, sizes[i], prices[i]) 
        print("=" * width)
        # (Exercise 2 — choose size)
        while True:
            user_size = int(input("Enter number 1-4: "))
            if 1 <= user_size <= 4:
                print("Order Stored!")
                break
            else:
                print("Invalid Choice: ")
        # (Exercise 3 — add toppings)
        user_toppings = 0
        order_toppings_descriptions = []
        print("Here's our avaliable toppings!")
        print("=" * width)  
        print("Available toppings ($1.50 each):")
        print("=" * width)
        for i, topping in enumerate(topping_names, start=1):
            print(f"{i}. {topping}")
        print("=" * width)
        
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
                    total_toppings += 1
            else:
                print("Invalid choice")
        user_size_index = user_size - 1
        user_size_price = prices[user_size_index]

        topping_price = 1.50
        num_toppings = len(order_toppings_descriptions)

        total = user_size_price + (num_toppings * topping_price)

        toppings_str = ", ".join(order_toppings_descriptions) if order_toppings_descriptions else "No toppings"

        pizza_description = f"{sizes[user_size_index]} - {toppings_str}"

        order_descriptions.append(pizza_description)
        order_prices.append(total)
    elif order_another == "no" or order_another == "n":
        print("Thank you for your order!")
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
#Exercise 10 — Code a post reciept that prints "No pizza ordered" and skips the rest if the user doesn't order any pizzas.
if len(order_descriptions) == 0:
    print("No pizza ordered.")
else:
    #Exercise 8 — Discount code with attempt limit
    subtotal = 0
    for price in order_prices:
        subtotal += price
    tax= subtotal * 0.07
    total_1= subtotal + tax
    #Before printing the final total, ask the customer if they have a discount code. 
    #Valid codes: "STUDENT10" → 10% off, "HALFOFF" → 50% off.
    attempt= 0
    while attempt < 3:
        user_discount= input("Type discount code (type 'none' to skip): ").upper()
        if not user_discount == "none" or "None":
            attempt += 1
        print(f"amount of attempts: {attempt} out of 3".center(width))
        if user_discount == "STUDENT10":
                print("10 percent discount applied!")
                discount= (subtotal + tax) * .10
                break
        if user_discount == "HALFOFF":
                print("50 percent discount applied!")
                discount= (subtotal + tax) * .50
                break
        if user_discount == "NONE":
                discount = 0
                break
        if attempt == 3:
                print("Discount code NOT applied.")
                discount= 0
                break
        else:
                print("Invalid code")
    final_total = total_1 - discount    
        # (Exercise 6 — print receipt)
    print("=" * width)
    print("YOUR ORDER RECEIPT".center(width))
    print("=" * width)
    for i in range(len(order_descriptions)):
        print(f"{i + 1}. {order_descriptions[i]}")
        print(f"\t\t\t${order_prices[i]:.2f}")
        print("-" * width)
        subtotal = 0
        for sum in order_prices:
            subtotal += sum
        print(f"{'Subtotal:':<23}\t${subtotal:.2f}")
        tax = subtotal * 0.07
        print(f"{'Tax(7%):':<23}\t${tax:.2f}")
        print(f"{'Total:':<23}\t${final_total:.2f}")
    # EXERCISE 7 — Find most expensive pizza
    #write loop to find the most expensive pizza and print it out with its price
    max_expensive_price = 0
    max_expensive_index = 0
    for i in range(len(order_prices)):
        if order_prices[i] > max_expensive_price:
            max_expensive_price = order_prices[i]
            max_expensive_index = i
    print("The most expensive pizza is: ")
    for max_expensive_index in order_descriptions:
        print(f"{max_expensive_index} at\t{max_expensive_price:.2f}")
    # EXERCISE 9 — Count pizzas by size
    # Print a summary showing how many pizzas of each size were ordered.
    size_counts = {size: 0 for size in sizes}
    for description in order_descriptions:
        for size in sizes:
            if size in description:
                size_counts[size] += 1
                print("-"*width)
                print("Pizza Size Summary: ")
                print(f"{size_counts[size]} {size} pizza(s)")
                print("-=" * 16)
                print("\n")
                print("***********THANK YOU***********")
                break
