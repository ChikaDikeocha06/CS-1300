print("\nProblem 1 - PopBuzz")
nums= range(1,41)
def popbuzz(nums):
    for num in nums:
        if num % 4 == 0 and num % 7 == 0:
            print("PopBuzz")
        elif num % 4 == 0:
            print("Pop")
        elif num % 7 == 0:
            print("Buzz")
        else:
            print(num)
popbuzz(nums)

print("\nProblem 2 - Right_Triangle Star Pattern")
def right_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)
right_triangle(7)

print("\nProblem 3 - Common Elements Perserving Order")
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
def common_in_order(a,b):
    common = []
    for element in a:
        if element in b and element not in common:
            common.append(element)
    return common
print(common_in_order([1, 2, 3, 4], [3, 4, 5, 6]))

print("\nProblem 4 - Triangular Number")
tri_nums= []
def triangular(n):
    #use accumulator pattern
    total = 0
    for i in range(1, n + 1):
        total += i  
        tri_nums.append(total)
    return total
triangular(5)
print(tri_nums)

print("\nProblem 5 - Mini Libary Tracker")
menu= ["View borrowed books", "Borrow a book", "Return a book", "Show action history", "Quit"]
books= [] 
for i, menu_names in enumerate(menu, start=1):
            print(f"{i}. {menu_names}")
while True:
    try:
        user_choice = int(input("Enter a number 1-5: "))
    except ValueError:
        print("Invalid choice")
        continue   
    if user_choice == 1:
        print("\nCurrently Borrowed Books: ")
        for i, book_names in enumerate(books, start=1):
            print(f"{i}. {book_names}")
        if books == []:
            print("\tYou have no borrowed books.")
    elif user_choice == 2:
        book_input= input("Enter the title of the book you want to borrow: ")
        if book_input == "":
                print("Title cannot be empty.")
        else:            
                books.append(book_input)
                print(f"Borrowed: {book_input}")

    elif user_choice == 3:
        if books == []:
            print("You have no books to return.")
        else:
            print("\nCurrently Borrowed Books: ")
            for i, book_names in enumerate(books, start=1):
                print(f"{i}. {book_names}")
            try:
                return_choice = int(input("Enter the number of the book you want to return: "))
                if 1 <= return_choice <= len(books):
                    returned_book = books.pop(return_choice - 1)
                    print(f"Returned: {returned_book}")
                else:
                    print("Invalid choice")
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif user_choice == 4:
        print("\nAction History: ")
        if books == []:
            print("\tNo actions yet.")
        else:
            for i, book_names in enumerate(books, start=1):
                print(f"{i}. Borrow: {book_names}")

    elif user_choice == 5:
        print(f"Goodbye! Your currently have {len(books)} book(s) borrowed.")
        break
        
    else:
        print("Invalid choice")
