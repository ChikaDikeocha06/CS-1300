# Problem 2: Weather Advisory System
# This program gives a weather message
# based on temperature and rain.

# Ask user for temperature
temp = float(input("Enter temperature: "))

# Ask if it is raining
rain = input("Is it raining? (yes/no): ")

# Check temperature conditions
if temp > 100:
    # Above 100 always shows extreme heat
    print("EXTREME HEAT WARNING: Stay indoors!")

elif temp > 85:
    # Between 86 and 100
    if rain == "yes":
        print("Warm rain — watch for flash floods.")
    else:
        print("Hot and dry — stay hydrated.")

elif 60 <= temp <= 85:
    # Between 60 and 85
    if rain == "yes":
        print("Grab an umbrella!")
    else:
        print("Nice weather — enjoy your day!")

elif 32 <= temp <= 59:
    # Between 32 and 59
    print("It's cold — bundle up!")

else:
    # Below 32
    print("FREEZE WARNING: Roads may be icy!")
