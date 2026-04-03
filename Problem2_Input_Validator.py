errors = []
valid_majors = ["CS", "IT", "CE", "DS"]

while True:
    student_id = input("Enter student ID: ")
    name = input("Enter full name: ")
    age = input("Enter age: ")
    major = input("Enter major: ")

    errors = []  # reset each loop

    # Student ID: 8 digits only
    if not student_id.isdigit() or len(student_id) != 8:
        errors.append("Student ID must be exactly 8 digits.")

    # Name: not empty, at least 2 characters
    if len(name.strip()) < 2:
        errors.append("Name must not be empty and at least 2 characters.")

    # Age: number between 16 and 99
    if not age.isdigit() or not (16 <= int(age) <= 99):
        errors.append("Age must be a number between 16 and 99.")

    # Major: must be valid (case-insensitive)
    if major.upper() not in valid_majors:
        errors.append("Major must be one of: CS, IT, CE, DS.")

    # Output results
    if errors:
        print("\n".join(errors))
        print()
    else:
        print("Student profile created successfully!")
        break
