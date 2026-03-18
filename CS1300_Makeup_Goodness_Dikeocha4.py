# Ask for viewer information
age = int(input("Enter age: "))
showtime = input("Enter showtime (matinee/evening): ").lower()
member = input("Rewards member? (yes/no): ").lower()

# Validate showtime
if showtime not in ["matinee", "evening"]:
    print("Invalid showtime.")
else:
    # -------------------------------
    # 1. Determine base price by age
    # -------------------------------
    if age < 12:
        base_price = 6.00
    elif age >= 65:
        base_price = 7.00
    elif 12 <= age <= 17:
        base_price = 9.00
    else:
        base_price = 13.00

    # -------------------------------
    # 2. Apply matinee discount
    # -------------------------------
    if showtime == "matinee":
        matinee_discount = 2.00
    else:
        matinee_discount = 0.00

    price_after_matinee = base_price - matinee_discount

    # -------------------------------
    # 3. Apply rewards discount (15%)
    # -------------------------------
    if member == "yes":
        rewards_discount = price_after_matinee * 0.15
    else:
        rewards_discount = 0.00

    final_price = price_after_matinee - rewards_discount

    # -------------------------------
    # 4. Print receipt
    # -------------------------------
    print("\n--- Movie Ticket ---")
    print(f"Age: {age}")
    print(f"Showtime: {showtime.capitalize()}")
    print(f"Rewards member: {member.capitalize()}")
    print(f"Base price: ${base_price:.2f}")
    print(f"Matinee discount: -${matinee_discount:.2f}")
    print(f"Rewards discount: -${rewards_discount:.2f}")
    print(f"Final price: ${final_price:.2f}")
    print("--------------------")
