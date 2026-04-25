# Program to print first n natural numbers using loop

n = int(input("Enter the value of n: "))

print("First", n, "natural numbers are:")

for i in range(1, n + 1):
    print(i, end=" ")