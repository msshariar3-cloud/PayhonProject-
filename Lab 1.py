Lab 01 — Python Basics
Complete all tasks below.

Topics:
- variables
- basic data types
- input and output
- type conversion
- arithmetic operators
- basic PEP 8
"""
# Program 1: Personal Information
# Topics: input/output, variables, basic data types, PEP 8

print("--- Program 1: Personal Information ---")

# Taking input from the user (input is always a string by default)
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

# Displaying the output
print("\n--- User Details ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
#============================

# Program 2: Basic Arithmetic Operations
# Topics: arithmetic operators, variables, input/output, PEP 8

print("\n--- Program 2: Basic Arithmetic Operations ---")

# Taking two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2  # Division always returns a float in Python 3

# Displaying the results
print(f"\nAddition ({num1} + {num2}) = {addition}")
print(f"Subtraction ({num1} - {num2}) = {subtraction}")
print(f"Multiplication ({num1} * {num2}) = {multiplication}")
print(f"Division ({num1} / {num2}) = {division}")

#==========================

# Program 3: Type Conversion
# Topics: type conversion, basic data types, variables, PEP 8

print("\n--- Program 3: Type Conversion ---")

# String to Integer conversion
str_num = "100"
int_num = int(str_num)
print(f"String '{str_num}' converted to Integer: {int_num} (Type: {type(int_num)})")

# Integer to Float conversion
float_num = float(int_num)
print(f"Integer {int_num} converted to Float: {float_num} (Type: {type(float_num)})")

# Float to String conversion
str_float = str(float_num)
print(f"Float {float_num} converted to String: '{str_float}' (Type: {type(str_float)})")

# Note: Trying to convert a non-numeric string (like "Hello") to int will cause an error.

#============================

# Program 4: Calculate Circle Area
# Topics: arithmetic operators, variables, input/output, type conversion, PEP 8

print("\n--- Program 4: Calculate Circle Area ---")

# Taking radius input and converting it to float
radius = float(input("Enter the radius of the circle: "))

# Defining the value of PI (constant)
PI = 3.14159

# Calculating the area (Area = PI * r^2)
area = PI * (radius ** 2)

# Displaying the output rounded to 2 decimal places
print(f"The area of the circle with radius {radius} is: {area:.2f}")

#================================

# Program 5: Simple Average Calculator
# Topics: variables, basic data types, arithmetic operators, input/output, PEP 8

print("\n--- Program 5: Simple Average Calculator ---")

# Taking three integer inputs from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Calculating the sum and average
total_sum = num1 + num2 + num3
average = total_sum / 3

# Displaying the results
print(f"\nThe sum of the three numbers is: {total_sum}")
print(f"The average of the three numbers is: {average:.2f}")

#========================

# Program 6: Temperature Converter
# Topics: type conversion, arithmetic operators, variables, input/output, PEP 8

print("\n--- Program 6: Temperature Converter ---")

# Taking temperature in Celsius as input
celsius = float(input("Enter temperature in Celsius: "))

# Formula: Fahrenheit = (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Displaying the result
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")


