# Program to demonstrate Functions in Python

# 1. Define and call a function
def welcome():
    print("Welcome to Python")

welcome()

# 2. Pass arguments to a function
def add(a, b):
    print("\nSum =", a + b)

add(10, 20)

# 3. Return multiple values from a function
def calculations(a, b):
    return a + b, a - b, a * b

sum_result, sub_result, mul_result = calculations(10, 5)

print("\nMultiple Return Values:")
print("Addition:", sum_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)

# 4. Factorial using function
def factorial(n):
    f = 1

    for i in range(1, n + 1):
        f *= i

    return f

num = 5

print("\nFactorial using function:", factorial(num))

# 5. Factorial using recursion
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * recursive_factorial(n - 1)

print("Factorial using recursion:", recursive_factorial(num))

# 6. Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

terms = 7

print("\nFibonacci Series:")

for i in range(terms):
    print(fibonacci(i), end=" ")

print()

# 7. Lambda function
square = lambda x: x * x

print("\nLambda Function:")
print("Square of 6 =", square(6))

# 8. Built-in functions
numbers = [10, 20, 30, 40, 50]

print("\nBuilt-in Functions:")
print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

# 9. Scope of variables

global_var = "I am Global"

def scope_demo():
    local_var = "I am Local"

    print("\nInside Function:")
    print(global_var)
    print(local_var)

scope_demo()

print("\nOutside Function:")
print(global_var)

# 10. Check prime number using function

def is_prime(n):

    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False

    return True

number = int(input("\nEnter a number to check prime: "))

if is_prime(number):
    print(number, "is a Prime Number")
else:
    print(number, "is not a Prime Number")