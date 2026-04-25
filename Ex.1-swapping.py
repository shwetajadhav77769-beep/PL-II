# Swap using a temporary variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nBefore swapping:")
print("a =", a, "b =", b)

# Swapping
temp = a
a = b
b = temp

print("\nAfter swapping:")
print("a =", a, "b =", b)