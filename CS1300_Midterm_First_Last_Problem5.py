# Student Roster Manager

# Starting data
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [88, 72, 95, 64, 81]

# Task 1: Print roster
print("=== CLASS ROSTER ===")
for i in range(len(names)):
    print(f"{i+1}. {names[i]} - {scores[i]}")
print("====================")

# Task 2: Find highest and lowest (no max/min)
highest_index = 0
lowest_index = 0

for i in range(len(scores)):
    if scores[i] > scores[highest_index]:
        highest_index = i
    if scores[i] < scores[lowest_index]:
        lowest_index = i

print("Highest:", names[highest_index], "-", scores[highest_index])
print("Lowest:", names[lowest_index], "-", scores[lowest_index])

# Task 3: Calculate average
total = 0
for s in scores:
    total += s

average = total / len(scores)
print(f"Average: {average:.2f}")

# Task 4: Grade report
print("--- Grade Report ---")
for i in range(len(scores)):
    score = scores[i]
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"{names[i]}: {score} -> {grade}")

# Task 5: Add Frank and remove Diana
names.append("Frank")
scores.append(77)

# Find index of Diana and remove from both lists
index = names.index("Diana")
names.pop(index)
scores.pop(index)

# Print updated length
print("Updated roster length:", len(names))
