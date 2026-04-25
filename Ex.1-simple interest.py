# Program to calculate Simple Interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time (in years): "))
simple_interest = (principal * rate * time) / 100

print("\nSimple Interest =", simple_interest)