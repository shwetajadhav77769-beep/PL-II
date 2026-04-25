# Program to count digits in a number

number = int(input("Enter a number: "))

# Convert number to positive
number = abs(number)

count = 0
if number == 0:
    count = 1
else:
    while number > 0:
        count += 1
        number //= 10

print("\nNumber of digits =", count)