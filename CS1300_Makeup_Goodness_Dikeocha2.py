# Ask the user for an email address
email = input("Enter an email address: ")

# -------------------------------
# 1. Count @ symbols and spaces
# -------------------------------
at_count = 0
space_count = 0

for char in email:
    if char == "@":
        at_count += 1
    if char == " ":
        space_count += 1

# -------------------------------
# 2. Check each criterion
# -------------------------------

# Criterion 1: Exactly one @
single_at = (at_count == 1)

# Criterion 2: At least one character before @
if single_at:
    at_index = email.index("@")
    before_at = (at_index >= 1)
else:
    before_at = False

# Criterion 3: At least one dot after @
if single_at:
    after_at = email[at_index + 1:]
    dot_after = ("." in after_at)
else:
    dot_after = False

# Criterion 4: At least two characters after the LAST dot
if dot_after:
    last_dot_index = email.rindex(".")
    extension = email[last_dot_index + 1:]
    domain_extension = (len(extension) >= 2)
else:
    domain_extension = False

# Criterion 5: No spaces
no_spaces = (space_count == 0)

# -------------------------------
# Print PASS/FAIL for each rule
# -------------------------------
print("Single @:", "PASS" if single_at else "FAIL")
print("Text before @:", "PASS" if before_at else "FAIL")
print("Dot after @:", "PASS" if dot_after else "FAIL")
print("Domain extension:", "PASS" if domain_extension else "FAIL")
print("No spaces:", "PASS" if no_spaces else "FAIL")

# -------------------------------
# Count total criteria met
# -------------------------------
criteria_met = (
    single_at +
    before_at +
    dot_after +
    domain_extension +
    no_spaces
)

print(f"Criteria met: {criteria_met} / 5")

# -------------------------------
# Final result
# -------------------------------
if criteria_met == 5:
    print("Result: Valid email address")
elif criteria_met in (3, 4):
    print("Result: Possibly valid - review format")
else:
    print("Result: Invalid email address")
