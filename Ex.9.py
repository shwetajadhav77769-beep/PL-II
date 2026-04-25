# Program to demonstrate File Handling and Exception Handling

# 1. Create and write data into a file
file = open("sample.txt", "w")
file.write("Python is easy to learn.\n")
file.write("File handling is important.\n")
file.close()
print("Data written into file successfully.")

# 2. Read data from a file
file = open("sample.txt", "r")
content = file.read()
print("\nFile Content:")
print(content)
file.close()

# 3. Append data into a file
file = open("sample.txt", "a")
file.write("This line is added using append mode.\n")
file.close()
print("Data appended successfully.")

# 4. Count lines, words, and characters in a file
file = open("sample.txt", "r")
content = file.read()

lines = content.splitlines()
words = content.split()
characters = len(content)

print("\nFile Statistics:")
print("Number of lines:", len(lines))
print("Number of words:", len(words))
print("Number of characters:", characters)
file.close()

# 5. Copy contents from one file to another
source = open("sample.txt", "r")
destination = open("copy.txt", "w")

destination.write(source.read())

source.close()
destination.close()
print("\nFile copied successfully.")

# 6. Handle division by zero exception
try:
    num1 = int(input("\nEnter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# 7. Handle invalid input exception
try:
    number = int(input("\nEnter an integer: "))
    print("You entered:", number)

except ValueError:
    print("Error: Invalid input. Please enter only numbers.")

# 8. Use try-except-finally block
try:
    file = open("sample.txt", "r")
    print("\nReading file using try-except-finally:")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Finally block executed.")

# 9. User-defined exception
class NegativeNumberError(Exception):
    pass
try:
    num = int(input("\nEnter a positive number: "))
    if num < 0:
        raise NegativeNumberError
    print("You entered:", num)

except NegativeNumberError:
    print("Error: Negative numbers are not allowed.")

# 10. File exception handling
try:
    file = open("unknown.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("\nError: File does not exist.")

except Exception as e:
    print("An error occurred:", e)

finally:
    print("File handling operation completed.")