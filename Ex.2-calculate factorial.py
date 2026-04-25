# Program to calculate factorial of a number using loop

number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("\nFactorial of", number, "is", factorial)