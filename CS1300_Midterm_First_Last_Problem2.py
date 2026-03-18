# Simple Sentence Analysis

# Get input
s = input("Enter a sentence: ")

# Counts using simple loops
upper = lower = digits = spaces = 0

for c in s:
    if c.isupper():
        upper += 1
    if c.islower():
        lower += 1
    if c.isdigit():
        digits += 1
    if c == " ":
        spaces += 1

# Output
print("Total characters:", len(s))
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
print("Digits:", digits)
print("Spaces:", spaces)
print("Reversed:", s[::-1])
