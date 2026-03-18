# Initial data
titles = ["Python Crash Course", "Clean Code", "The Pragmatic Programmer", "Code Complete", "SICP"]
copies = [5, 3, 7, 2, 4]

# -----------------------------------------
# 1. Print original catalog as a table
# -----------------------------------------
print("=== LIBRARY CATALOG ===")
for i in range(len(titles)):
    print(f"{i+1}. {titles[i]} - {copies[i]} copies")
print("========================")

# -----------------------------------------
# 2. Find book with most and fewest copies
# (No max() or min())
# -----------------------------------------
# Start by assuming the first book is both max and min
max_index = 0
min_index = 0

for i in range(1, len(copies)):
    if copies[i] > copies[max_index]:
        max_index = i
    if copies[i] < copies[min_index]:
        min_index = i

print(f"Most copies: {titles[max_index]} ({copies[max_index]})")
print(f"Fewest copies: {titles[min_index]} ({copies[min_index]})")

# -----------------------------------------
# 3. Total books + average copies per title
# -----------------------------------------
total = 0
for c in copies:
    total += c

average = total / len(copies)

print(f"Total books: {total}")
print(f"Average per title: {average:.2f}")

# -----------------------------------------
# 4. Append "Design Patterns" with 6 copies
# -----------------------------------------
titles.append("Design Patterns")
copies.append(6)

# -----------------------------------------
# 5. Insert "Algorithms" with 8 copies at index 1
# -----------------------------------------
titles.insert(1, "Algorithms")
copies.insert(1, 8)

# -----------------------------------------
# 6. Remove "SICP" from both lists
# -----------------------------------------
if "SICP" in titles:
    idx = titles.index("SICP")
    titles.pop(idx)
    copies.pop(idx)

# -----------------------------------------
# 7. Pop the last book and print what was removed
# -----------------------------------------
removed_title = titles.pop()
removed_copies = copies.pop()

print(f"Removed last book: {removed_title} ({removed_copies} copies)")

# -----------------------------------------
# 8. Print final catalog and its length
# -----------------------------------------
print("\n=== FINAL CATALOG ===")
for i in range(len(titles)):
    print(f"{i+1}. {titles[i]} - {copies[i]} copies")
print("=======================")
print(f"Total titles: {len(titles)}")
