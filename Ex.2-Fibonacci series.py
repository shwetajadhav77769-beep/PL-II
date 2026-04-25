# Program to display Fibonacci series

terms = int(input("Enter the number of terms: "))
a = 0
b = 1

print("\nFibonacci Series:")
for i in range(terms):
    print(a, end=" ")
    a, b = b, a + b