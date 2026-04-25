# Program to reverse a number

number = int(input("Enter a number: "))

# Store original sign
sign = -1 if number < 0 else 1

# Convert to positive
number = abs(number)

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

# Restore sign
reverse *= sign

print("\nReversed number =", reverse)