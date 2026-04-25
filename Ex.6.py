# Program to perform Dictionary Operations

# 1. Create a dictionary of student details
students = {
    "Rahul": 85,
    "Sneha": 92,
    "Amit": 78
}

print("Student Dictionary:")
print(students)

# 2. Access keys, values, and items
print("\nDictionary Keys:")
print(students.keys())

print("\nDictionary Values:")
print(students.values())

print("\nDictionary Items:")
print(students.items())

# 3. Add and update dictionary elements

# Add new student
students["Priya"] = 88

# Update marks
students["Rahul"] = 90

print("\nDictionary after adding and updating elements:")
print(students)

# 4. Delete elements from dictionary

del students["Amit"]

print("\nDictionary after deleting an element:")
print(students)

# 5. Count frequency of words in a sentence using dictionary

sentence = input("\nEnter a sentence: ").lower()
words = sentence.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\nWord Frequency:")
print(frequency)

# 6. Merge two dictionaries

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = {**dict1, **dict2}

print("\nMerged Dictionary:")
print(merged_dict)

# 7. Convert hexadecimal to binary using dictionary

hex_dict = {
    '0': '0000', '1': '0001',
    '2': '0010', '3': '0011',
    '4': '0100', '5': '0101',
    '6': '0110', '7': '0111',
    '8': '1000', '9': '1001',
    'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101',
    'E': '1110', 'F': '1111'
}

hex_num = input("\nEnter a hexadecimal number: ").upper()

binary = ""

for digit in hex_num:
    binary += hex_dict[digit]

print("Binary equivalent:", binary)

# 8. Find student with highest marks

top_student = max(students, key=students.get)

print("\nStudent with highest marks:")
print(top_student, "=", students[top_student])

# 9. Sort dictionary by keys and values

# Sort by keys
sorted_keys = dict(sorted(students.items()))

print("\nDictionary sorted by keys:")
print(sorted_keys)

# Sort by values
sorted_values = dict(sorted(students.items(), key=lambda item: item[1]))

print("\nDictionary sorted by values:")
print(sorted_values)

# 10. Dictionary comprehension

squares = {x: x*x for x in range(1, 6)}

print("\nDictionary using comprehension (Squares):")
print(squares)