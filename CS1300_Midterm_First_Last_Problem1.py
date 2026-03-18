# Temperature Converter Program
# This program converts a temperature between Celsius and Fahrenheit

# Ask user for temperature (convert input to float for decimals)
temperature = float(input("Enter temperature: "))

# Ask user for scale and convert to uppercase for case-insensitive comparison
scale = input("Enter scale (C/F): ").upper()

# Check if the scale is Celsius
if scale == "C":
    # Convert Celsius to Fahrenheit using formula
    fahrenheit = temperature * 9/5 + 32
    
    # Print result formatted to 1 decimal place
    print(f"{temperature:.1f}°C = {fahrenheit:.1f}°F")

# Check if the scale is Fahrenheit
elif scale == "F":
    # Convert Fahrenheit to Celsius using formula
    celsius = (temperature - 32) * 5/9
    
    # Print result formatted to 1 decimal place
    print(f"{temperature:.1f}°F = {celsius:.1f}°C")

# If input is not C or F, print error message
else:
    print("Invalid scale.")
