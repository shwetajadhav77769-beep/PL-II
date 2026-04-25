# Program to calculate area and perimeter of a rectangle

length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("\nArea of rectangle =", area)
print("Perimeter of rectangle =", perimeter)