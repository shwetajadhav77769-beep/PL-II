# Program to demonstrate OOP concepts in Python

# 1. Create a class and object
class Student:
    def display(self):
        print("This is a Student class")
obj = Student()
obj.display()

# 2. Demonstrate constructor
class Person:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("\nConstructor Example:")
        print("Name:", self.name)
p1 = Person("Rahul")
p1.show()

# 3. Demonstrate instance and class variables
class Employee:
    company = "TCS"   # Class Variable
    def __init__(self, name):
        self.name = name   # Instance Variable
    def display(self):
        print("\nInstance and Class Variables:")
        print("Employee Name:", self.name)
        print("Company:", Employee.company)
e1 = Employee("Amit")
e2 = Employee("Sneha")

e1.display()
e2.display()

# 4. Single Inheritance
class Parent:
    def parent_method(self):
        print("\nSingle Inheritance:")
        print("This is Parent class")
class Child(Parent):
    def child_method(self):
        print("This is Child class")

c = Child()
c.parent_method()
c.child_method()

# 5. Multiple Inheritance
class Father:
    def father_method(self):
        print("\nFather class method")
class Mother:
    def mother_method(self):
        print("Mother class method")
class Son(Father, Mother):
    def son_method(self):
        print("Son class method")

s = Son()
print("\nMultiple Inheritance:")
s.father_method()
s.mother_method()
s.son_method()

# 6. Multilevel Inheritance
class Grandparent:
    def grandparent_method(self):
        print("\nGrandparent class")
class Parent2(Grandparent):
    def parent_method(self):
        print("Parent class")
class Child2(Parent2):
    def child_method(self):
        print("Child class")

m = Child2()
print("\nMultilevel Inheritance:")
m.grandparent_method()
m.parent_method()
m.child_method()

# 7. Method Overriding
class Animal:
    def sound(self):
        print("\nAnimal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
print("\nMethod Overriding:")
d.sound()

# 8. Calculate area of shapes using inheritance
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

rect = Rectangle(10, 5)
circle = Circle(7)

print("\nArea Calculation using Inheritance:")
print("Rectangle Area:", rect.area())
print("Circle Area:", circle.area())

# 9. Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private variable
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)

account.deposit(500)

print("\nEncapsulation:")
print("Balance:", account.get_balance())

# 10. Polymorphism
class Bird:
    def sound(self):
        print("Bird makes sound")
class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")
class Crow(Bird):
    def sound(self):
        print("Crow caws")

print("\nPolymorphism:")
birds = [Sparrow(), Crow()]

for b in birds:
    b.sound()