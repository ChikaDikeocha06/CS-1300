#------------------------------------------------------
#Student Grade Tracker
#CS 1300 — Lecture 5 Mini-Project

#A modular, well-tested program that collects exam scores,
#calculates a letter grade and academic standing, and
#displays a formatted report.
#------------------------------------------------------

#STEP 1: Write main() first
test_scores = [50,75,90]
scores= [] #a variable to store the exam scores
avgs=[] # a variable to store the average of the exam scores
#Step 3: Create Stubs and Implement One at a Time
"""
    Prompt for and return student name
"""
def get_student_name(): #A stub function to get the student's name
    name= input("Student: ") #A variable to prompt the user to enter the student's name
    return name #A return statement to store the student's name and return it to the main function
"""
Collect n exam scores with validation
"""
def get_exam_scores(i): #A stub function to get the exam scores with a parameter i to track the exam number
    exam_score = int(input(f"   Exam {i+1}: ")) #A variable to promt user to enter each exam score with the exam number displayed
    return exam_score #A return statement to store exam each score and return it to the main function
"""
    Helper: validate a single score
"""
def is_valid_score(score): #A stub function to validate a single score with a parameter score to check if it is valid
    if not 0<= score <=100: #if not condition to check if schore is between 0 and 100 , if invalid it'll store and return false
        return False # return statement if invalid score is entered
    exam_score= int(score) #A variable to convert the score to int
    return exam_score#
    
"""
    Helper: retry loop for score entry
"""
def get_validated_scores(score=0, error_msg="Invalid Score Value"):
        for i in range(3):
            score = get_exam_scores(i)
            if is_valid_score(score): 
                scores.append(score)
            else:
                print(error_msg)
        return scores
"""
    Compute mean of a scores list
"""
def calculate_average(scores):
    avg = round(sum(scores) / len(scores), 2)
    avgs.append(avg)
    return avg

"""
    Map average to letter grade
"""
def determine_letter_grade(avg): 
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    
"""
    Map average to academic standing
"""
def determine_standing(avg):
    if avg >= 90:
        return "Dean's List"
    elif avg >= 70:
        return "Good Standing"
    elif avg >= 60:
        return "Academic Probation"
    else:
        return "Academic Warning"

"""
    Helper: print a decorative line
"""
def print_divider():
        return("=" *32)
    
"""
    Print the formatted grade report
"""
def display_report(avg, grade, standing):
    print(print_divider())
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
    print(f"Standing: {standing}")
    print(print_divider()) 
"""
    Run all unit tests
"""
"""
    Orchestrate the full program
"""
def main():
    test_grade_tracker()
    print(print_divider())
    print("STUDENT GRADE REPORT")
    print(print_divider())
    get_student_name()
    get_validated_scores()
    avg = calculate_average(scores)
    grade = determine_letter_grade(avg)
    standing = determine_standing(avg)
    display_report(avg, grade, standing)

def test_grade_tracker():
                run = input("Run tests first? (y/n): ").lower()
                if run != "y":
                    return   
                """
                Test the test_calculate_grade function
                """
                print("TESTING GRADE CALCULATOR.......")
                print("Exam scores= 50, 75, 90")

                # Test 1: (Test calculate_average function)
                print("Testing calculate_average function...")
                if calculate_average(test_scores) == 71.67:
                    print("✓ Passed")  
                else:
                    print("✗ Failed")
                    

                # Test 2: (Test determine_letter_grade function)
                print("Testing determine_letter_grade function...")
                if determine_letter_grade(71.67) == "C":
                    print("✓ Passed")
                else:
                    print("✗ Failed")    

                # Test 3: (Test determine_standing function)
                print("Testing determine_standing function...")
                if determine_standing(71.67) == "Good Standing":
                    print("✓ Passed")
                    print("Displaying test score report...")
                    print("=" *32)
                    print(f"Average: 71.67")
                    print(f"Grade: C")
                    print(f"Standing: Good Standing")
                    print("=" *32)
                else:
                    print("✗ Failed")


                       
main()