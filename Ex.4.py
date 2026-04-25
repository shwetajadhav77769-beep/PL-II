# Program to perform different list operations

# 1. Creating a list
numbers = [18,99,49,32,77,22,99]

print("Original List:")
print(numbers)

# 2. Sum and Average
total = sum(numbers)
average = total / len(numbers)

print("\nSum of elements:", total)
print("Average of elements:", average)

# 3. Maximum and Minimum
print("\nMaximum element:", max(numbers))
print("Minimum element:", min(numbers))

# 4. Sorting the list
sorted_list = sorted(numbers)

print("\nSorted List:")
print(sorted_list)

# 5. Removing duplicates
unique_list = list(set(numbers))

print("\nList after removing duplicates:")
print(unique_list)

# 6. Searching an element
search = int(input("\nEnter element to search: "))

if search in numbers:
    print("Element found in the list")
else:
    print("Element not found in the list")

# 7. Merging two lists
list2 = [64,52,77]

merged_list = numbers + list2

print("\nSecond List:", list2)
print("Merged List:", merged_list)

# 8. Counting even and odd numbers
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\nEven numbers count:", even_count)
print("Odd numbers count:", odd_count)

# 9. Finding second largest element
unique_sorted = sorted(set(numbers))

print("\nSecond Largest Element:", unique_sorted[-2])

# 10. List Slicing
print("\nList Slicing Operations:")
print("First 3 elements:", numbers[:3])
print("Last 3 elements:", numbers[-3:])
print("Elements from index 2 to 5:", numbers[2:6])
print("Every second element:", numbers[::2])