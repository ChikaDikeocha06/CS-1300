# Ask the user for the amount of money to convert
amount = float(input("Enter amount: "))

# Ask for the source currency and convert it to uppercase for consistency
currency = input("Enter currency (USD/EUR/GBP): ").upper()

# Check if the currency is USD
if currency == "USD":
    # Convert USD to EUR and GBP using fixed exchange rates
    eur = amount * 0.92
    gbp = amount * 0.79

    # Print results formatted to 2 decimal places
    print(f"{amount:.2f} USD = {eur:.2f} EUR")
    print(f"{amount:.2f} USD = {gbp:.2f} GBP")

# Check if the currency is EUR
elif currency == "EUR":
    # Convert EUR to USD and GBP
    usd = amount * 1.09
    gbp = amount * 0.86

    # Print results
    print(f"{amount:.2f} EUR = {usd:.2f} USD")
    print(f"{amount:.2f} EUR = {gbp:.2f} GBP")

# Check if the currency is GBP
elif currency == "GBP":
    # Convert GBP to USD and EUR
    usd = amount * 1.27
    eur = amount * 1.16

    # Print results
    print(f"{amount:.2f} GBP = {usd:.2f} USD")
    print(f"{amount:.2f} GBP = {eur:.2f} EUR")

# If the user enters anything else, it's invalid
else:
    print("Invalid currency.")
