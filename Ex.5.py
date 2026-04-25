# Program to perform Tuple and Set operations

# ---------------- TUPLE OPERATIONS ----------------

# 1. Creating a tuple
numbers = (60, 20, 30, 40, 50, 20)

print("Tuple Elements:")
print(numbers)

# 2. Sum and Average of tuple elements
total = sum(numbers)
average = total / len(numbers)

print("\nSum of tuple elements:", total)
print("Average of tuple elements:", average)

# 3. Maximum and Minimum element
print("\nMaximum element:", max(numbers))
print("Minimum element:", min(numbers))

# 4. Tuple Packing and Unpacking
packed_tuple = ("Python", 101, "Programming")

print("\nPacked Tuple:", packed_tuple)

language, code, subject = packed_tuple

print("Unpacked Values:")
print("Language:", language)
print("Code:", code)
print("Subject:", subject)

# 5. Convert tuple into list
tuple_to_list = list(numbers)

print("\nTuple converted to List:")
print(tuple_to_list)

# 6. Check membership of an element in tuple
search = int(input("\nEnter element to search in tuple: "))

if search in numbers:
    print("Element found in tuple")
else:
    print("Element not found in tuple")

# 7. Count occurrences of an element in tuple
count_element = int(input("\nEnter element to count in tuple: "))

count = numbers.count(count_element)

print("Occurrences of", count_element, "=", count)

# ---------------- SET OPERATIONS ----------------

# Creating sets
set1 = {16,35,8,9,10,12}
set2 = {10,5,19,32,8}

print("\nSet 1:", set1)
print("Set 2:", set2)

# 8. Union of sets
print("\nUnion:", set1.union(set2))

# 9. Intersection of sets
print("Intersection:", set1.intersection(set2))

# 10. Difference of sets
print("Difference (set1 - set2):", set1.difference(set2))

# 11. Removing duplicates using set
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]

unique_elements = set(list_with_duplicates)

print("\nList with duplicates:", list_with_duplicates)
print("After removing duplicates:", unique_elements)