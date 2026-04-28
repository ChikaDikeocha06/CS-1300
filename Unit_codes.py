# ============================================
# CS1300 - ALL UNIT EXERCISES (1, 2, 3)
# ============================================

def unit1():
    print("\n===== UNIT 1 =====")

    # Beginner
    print("\n-- Unit 1 Beginner --")
    rgb_color = (255, 128, 0)

    print(rgb_color[0])
    print(rgb_color[1])
    print(rgb_color[2])

    palette = []
    palette.append(rgb_color)

    print(palette)

    # Intermediate
    print("\n-- Unit 1 Intermediate --")
    student1 = ("Alice", 90, 20)
    student2 = ("Bob", 85, 21)
    student3 = ("Charlie", 88, 19)

    classroom = [student1, student2, student3]

    print(classroom[1][0])

    name, grade, age = classroom[0]
    print(f"{name} is {age} years old with grade {grade}")

    # Advanced
    print("\n-- Unit 1 Advanced --")
    student = ("Alice", [85, 90, 78], 0)

    student[1].append(92)

    avg = sum(student[1]) / len(student[1])

    updated_student = (student[0], student[1], avg)

    print("Original:", student)
    print("Updated:", updated_student)


def unit2():
    print("\n===== UNIT 2 =====")

    # Beginner
    print("\n-- Unit 2 Beginner --")
    grades = [85, 90, 78]
    date = (4, 27, 2026)

    def boost_grades(grades):
        for i in range(len(grades)):
            grades[i] += 5

    boost_grades(grades)
    print(grades)

    # Intermediate
    print("\n-- Unit 2 Intermediate --")
    def find_range(*args):
        return (min(args), max(args))

    print(find_range(3, 7, 1))
    print(find_range(10, 5, 8, 2, 20, 15, 6))

    test_scores = [78, 92, 85, 88, 91]
    print(find_range(*test_scores))

    # Advanced
    print("\n-- Unit 2 Advanced --")
    def calculate_statistics(*args):
        count = len(args)
        total = sum(args)
        avg = total / count if count > 0 else 0
        return (count, total, avg)

    def update_student_records(records, bonus):
        new_list = []
        for name, grade in records:
            new_list.append((name, grade + bonus))
        return new_list

    records = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]

    stats = calculate_statistics(85, 90, 78)
    updated = update_student_records(records, 5)

    print(stats)
    print(updated)


def unit3():
    print("\n===== UNIT 3 =====")

    # Beginner
    print("\n-- Unit 3 Beginner --")
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(grid)
    print(grid[1][1])

    for row in grid:
        print(row)

    # Intermediate
    print("\n-- Unit 3 Intermediate --")
    scores = [45, 78, 92, 61, 88, 73, 55, 90, 82]

    passing_grades = [x for x in scores if x >= 60]

    letter_grades = [
        'A' if x >= 90 else
        'B' if x >= 80 else
        'C' if x >= 70 else
        'D'
        for x in passing_grades
    ]

    print(passing_grades)
    print(letter_grades)

    # Advanced
    print("\n-- Unit 3 Advanced --")
    table = [[i * j for j in range(1, 5)] for i in range(1, 5)]

    for row in table:
        print(row)

    def sum_diagonal(matrix):
        total = 0
        for i in range(len(matrix)):
            total += matrix[i][i]
        return total

    print("Diagonal sum:", sum_diagonal(table))

    gen = (x for row in table for x in row if x % 2 == 0)

    count = 0
    for num in gen:
        print(num)
        count += 1
        if count == 5:
            break


# ============================================
# MAIN
# ============================================

def main():
    unit1()
    unit2()
    unit3()


if __name__ == "__main__":
    main()