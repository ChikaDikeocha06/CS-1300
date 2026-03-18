# List Operations Toolkit

# Starting list
numbers = [15, 8, 23, 42, 4, 16, 31, 7, 19, 11]

# 1. Print original list
print("Original:", numbers)

# 2. Print first and last element
print("First:", numbers[0], "Last:", numbers[len(numbers) - 1])

# 3. Print middle 4 elements (index 3–6)
print("Middle 4:", numbers[3:7])

# 4. Append 99
numbers.append(99)
print("After append:", numbers)

# 5. Insert 0 at beginning
numbers.insert(0, 0)
print("After insert:", numbers)

# 6. Remove 42
numbers.remove(42)
print("After remove:", numbers)

# 7. Pop last element
removed = numbers.pop()
print("Popped:", removed)
print("After pop:", numbers)

# 8. Check if 23 is in list
print(23 in numbers)

# 9. Print index of 16
print("Index of 16:", numbers.index(16))

# 10. Print final list and length
print("Final:", numbers)
print("Length:", len(numbers))
