# Problem 1: Boolean Expression Evaluator
# This program asks for three integers and checks
# different Boolean expressions.

# Get user input
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

# Print the result of chained comparison
print("a < b < c            :", a < b < c)

# Print result using De Morgan's expression
print("not (a > b or b > c) :", not (a > b or b > c))

# Print equivalent comparison expression
print("a <= b and b <= c    :", a <= b and b <= c)

# Check if expression 2 and 3 match
if (not (a > b or b > c)) == (a <= b and b <= c):
    print("De Morgan's confirmed: Expressions 2 and 3 match!")
else:
    print("De Morgan's failed.")
