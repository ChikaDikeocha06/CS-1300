# CAMPUS CAFÉ ORDER SYSTEM

TAX_RATE = 0.07

while True:
    print("==============================")
    print("    CAMPUS CAFÉ ORDER SYSTEM")
    print("==============================")
    print("  1. Coffee       - $3.50")
    print("  2. Sandwich     - $6.00")
    print("  3. Salad        - $5.50")
    print("  4. Combo        - $8.00")
    print("  5. Exit")
    print("==============================")

    choice = input("Select an item (1-5): ")

    if choice == "5":
        print("Goodbye!")
        break

    total = 0

    # ---------------- COFFEE ----------------
    if choice == "1":
        base = 3.50
        size = input("Choose size (small/medium/large): ").lower()

        if size == "small":
            total = base
        elif size == "medium":
            total = base + 1.00
        elif size == "large":
            total = base + 2.00
        else:
            print("Invalid size, defaulting to Small.")
            total = base

    # ---------------- SANDWICH ----------------
    elif choice == "2":
        total = 6.00
        cheese = input("Add cheese? (yes/no): ").lower()

        if cheese == "yes":
            total += 0.75

    # ---------------- SALAD ----------------
    elif choice == "3":
        total = 5.50
        dressing = input("Choose dressing (ranch, italian, vinaigrette, none): ").lower()

        if dressing not in ["ranch", "italian", "vinaigrette", "none"]:
            print("Invalid dressing, defaulting to none.")

    # ---------------- COMBO ----------------
    elif choice == "4":
        total = 8.00

        # coffee size
        size = input("Coffee size (small/medium/large): ").lower()
        if size == "medium":
            total += 1.00
        elif size == "large":
            total += 2.00
        elif size != "small":
            print("Invalid coffee size, defaulting to small.")

        # cheese option
        cheese = input("Add cheese to sandwich? (yes/no): ").lower()
        if cheese == "yes":
            total += 0.75

    else:
        print("Invalid menu choice.")
        continue

    # ---------------- CUSTOMER INFO ----------------
    name = input("Enter student name: ").strip()
    if len(name) == 0:
        print("Name cannot be empty. Order cancelled.")
        continue

    # quantity validation
    try:
        quantity = int(input("How many items? "))
        if quantity <= 0:
            print("Quantity must be positive. Order cancelled.")
            continue
    except ValueError:
        print("Invalid quantity. Order cancelled.")
        continue

    subtotal = total * quantity
    tax = subtotal * TAX_RATE
    final_total = subtotal + tax

    # ---------------- RECEIPT ----------------
    print("\n==============================")
    print("        RECEIPT")
    print("==============================")
    print(f"Name: {name}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (7%): ${tax:.2f}")
    print(f"Total: ${final_total:.2f}")
    print("==============================\n")
