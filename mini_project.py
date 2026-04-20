#------------------------------------------------------
#Student Grade Tracker
#CS 1300 — Lecture 5 Mini-Project

#A modular, well-tested program that collects exam scores,
#calculates a letter grade and academic standing, and
#displays a formatted report.
#------------------------------------------------------

#STEP 1: Write main() first
"""
    Orchestrate the full program
"""
def main():
    get_student_name()
    is_valid_score()
    get_exam_scores()
    get_validated_scores()
    calculate_average()
    determine_letter_grade()
    determine_standing()
    print_divider()
    display_report()
    test_grade_tracker()

#Step 3: Create Stubs and Implement One at a Time
"""
    Prompt for and return student name
"""
def get_student_name():
    return input("Enter name: ")
"""
    Helper: validate a single score
"""
def is_valid_score(scores):
     return scores is not None and len(scores) > 0
"""
    Collect n exam scores with validation
"""
scores = []
def get_exam_scores():
    for i in range(3):
        s = int(input(f"Exam {i+1} score: "))
        score= get_validated_scores(s)
    
"""
    Helper: retry loop for score entry
"""
def get_validated_scores():
    if scores < 0 or scores > 100:
            print("Invalid!")
            return 
"""
    Compute mean of a scores list
"""
def calculate_average():
    avg = sum(scores) / len(scores)
    return
"""
    Map average to letter grade
"""
def determine_letter_grade(): 
    if calculate_average() >= 90: grade = "A"
    elif calculate_average() >= 80: grade = "B"
    elif calculate_average() >= 70: grade = "C"
    elif calculate_average() >= 60: grade = "D"
    else: grade = "F"
    return grade
"""
    Map average to academic standing
"""
def determine_standing():
    if calculate_average() >= 90: standing = "Dean's List"
    elif calculate_average() >= 70: standing = "Good Standing"
    elif calculate_average() >= 60: standing = "Academic Probation"
    else: standing = "Academic Warning"
"""
    Helper: print a decorative line
"""
def print_divider():
    div= "=" * 32
    print(div)
    return
"""
    Print the formatted grade report
"""
def display_report():
    print(print_divider())
    print("STUDENT GRADE REPORT")
    print(print_divider())   
    print(f"Student: {name}")
    print(f"Scores: {scores}")
    print(print_divider())
    print(f"Average: {calculate_average():.2f}")
    print(f"Grade: {determine_letter_grade()}")
    print(f"Standing: {determine_standing()}")
    print(print_divider())
"""
    Run all unit tests
"""
def test_grade_tracker():
    pass

main()
