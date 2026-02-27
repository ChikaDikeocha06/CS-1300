# Problem 3: Student Grade Report
# This program calculates the average,
# assigns a letter grade, and determines status.

# Get student name
name = input("Enter student name: ")

# Get three exam scores
s1 = float(input("Enter Exam 1 score: "))
s2 = float(input("Enter Exam 2 score: "))
s3 = float(input("Enter Exam 3 score: "))

# Calculate average
avg = (s1 + s2 + s3) / 3

# Determine letter grade based on average
if avg >= 90:
    grade = "A"
elif avg >= 87:
    grade = "A-"
elif avg >= 83:
    grade = "B+"
elif avg >= 80:
    grade = "B"
elif avg >= 77:
    grade = "B-"
elif avg >= 73:
    grade = "C+"
elif avg >= 70:
    grade = "C"
elif avg >= 67:
    grade = "C-"
elif avg >= 63:
    grade = "D+"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"

# Determine academic standing
if avg >= 90:
    status = "Dean's List"
elif avg >= 70:
    status = "Good Standing"
elif avg >= 60:
    status = "Academic Probation"
else:
    status = "Academic Suspension Warning"

# Print results
print("Average:", round(avg, 2))
print("Grade:", grade)
print("Status:", status)
