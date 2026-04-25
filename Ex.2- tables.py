# Program to print multiplication table of a given number

number = int(input("Enter a number: "))

print("\nMultiplication Table of", number)

for i in range(1, 11):
    print(number, "x", i, "=", number * i)