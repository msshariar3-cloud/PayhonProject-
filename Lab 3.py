"""
NSU Python — Lab 03
Conditions and for Loops

Complete Tasks 1–12.
Tasks 13–14 are optional bonus tasks.

Use only concepts covered in Lecture 03.
"""
from doctest import OutputChecker

Task=1============================================
# 1. Taking input from the user (Condition part)
num = int(input("Enter a number: "))

# 2. Checking the condition (If-Else)
if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")

print("-" * 20)

# 3. Using a for loop to print numbers
print("Printing numbers from 1 to 5 using a for loop:")
for i in range(1, 6):
    print(i)
#==========================
Task=2==============================================

# 1. Define our variables (like age and score in the slide)
user_age = 16
has_permission = False
ticket_price = 15

print("--- Movie Ticket Eligibility Checker ---")

# 2. Simple Boolean Expressions (using comparison operators)
print(f"Is the user 18 or older? {user_age >= 18}")
print(f"Does the user have a ticket? {ticket_price > 0}")

# 3. Using the 'and' operator (like the slide's 'age >= 18 and score >= 60')
# They must be 18 or older AND have permission to watch the movie.
can_watch_movie = user_age >= 18 and has_permission == True
print(f"Can the user watch the movie? {can_watch_movie}")

# 4. Storing a Boolean in a variable (like the 'passed' variable in the slide)
# Let's check if they are a child (under 13)
is_child = user_age < 13
print(f"Is the user a child? {is_child}")

# 5. Using the 'not' operator to reverse a boolean
is_adult = not is_child
print(f"Is the user an adult? {is_adult}")

Task=3=============================

# --- Program based on Comparison Operators ---

# 1. Initializing variables with numbers
x = 15
y = 8

print(f"Given values: x = {x}, y = {y}\n")

# 2. Using Comparison Operators
# Equality check
print(f"x == y (Is x equal to y?): {x == y}")  # Output: False

# Not equal check
print(f"x != y (Is x not equal to y?): {x != y}")  # Output: True

# Greater than check
print(f"x > y  (Is x greater than y?): {x > y}")   # Output: True

# Less than check
print(f"x < y  (Is x less than y?): {x < y}")   # Output: False

# Greater than or equal to check
print(f"x >= y (Is x greater than or equal to y?): {x >= y}") # Output: True

# Less than or equal to check
print(f"x <= y (Is x less than or equal to y?): {x <= y}") # Output: False


# 3. Comparisons also work with Strings (as shown in the image)
print("\n--- String Comparison ---")
name1 = "Anna"
name2 = "anna"

print(f"name1 == 'Anna': {name1 == 'Anna'}") # Output: True (Exact match)
print(f"name1 == name2 : {name1 == name2}")  # Output: False (Case-sensitive, 'A' and 'a' are different)


# 4. Important Note (as per the slide)
# Using '=' is for assignment, while '==' is for comparison.
# Example of Assignment:
a = 10  # 'a' is assigned the value 10
# Example of Comparison:
print(f"\nIs a equal to 10? {a == 10}") # Output: True

Task=4====================================================

# Student data
student_age = 19
student_score = 75
has_paid_fees = False

# 1. Using 'and': Both conditions must be True
# The student must be at least 18 years old AND score 60 or above.
is_eligible_for_exam = (student_age >= 18) and (student_score >= 60)

# 2. Using 'or': At least one condition must be True
# The student needs help if their score is below 50 OR they are under 18.
needs_help = (student_score < 50) or (student_age < 18)

# 3. Using 'not': Reverses the Boolean value
# The student is not allowed to sit for the exam if they haven't paid the fees.
is_not_allowed = not has_paid_fees

# Printing the results
print("--- Exam Eligibility Report ---")
print(f"Student Age: {student_age}, Score: {student_score}")
print(f"Has Paid Fees: {has_paid_fees}")
print("-" * 30)
print(f"Is eligible for exam?  : {is_eligible_for_exam}")
print(f"Does student need help?: {needs_help}")
print(f"Is student NOT allowed?: {is_not_allowed}")

Output:

--- Exam Eligibility Report ---
Student Age: 19, Score: 75
Has Paid Fees: False
------------------------------
Is eligible for exam?  : True
Does student need help?: False
Is student NOT allowed?: True

Task=5============================

temperature= 38
if temperature >37.5:
    print("High temperature")
    print("Check again later")

    print("Program fnished")

    Output:
     High temperature
     Check again later
     program finished

 Task=6======================

score = 75

if score >= 60:
    print("Passed")
    print("Good work")

print("This line always runs")

# Bad idea:
# if score >= 60:
# print("Passed")

# Example 1: Correct Indentation (4 spaces)
score = 75
if score >= 60:
    print("Passed")
    print("Good work")
print("This line always runs")

# Example 2: Incorrect Indentation (Will cause an IndentationError)
# Uncomment the lines below to see the error
# if score >= 60:
# print("Passed") # Missing indentation

# Example 3: Changing program meaning with indentation
score = 45
if score >= 60:
    print("Passed")
else:
    print("Failed")
    print("Please try again.") # Indented inside else, so it only prints if failed

    # Example 4: Nested indentation (8 spaces)
    is_student = True
    score = 85
    if is_student:
        if score >= 60:
            print("Student passed.")
    # ==========================================
    # Python Program: Indentation Is Syntax
    # ==========================================

print("--- 1. Correct Indentation Example ---")
# Rule: Use 4 spaces for each indentation level.
score = 75

if score >= 60:
    print("Passed")
    print("Good work")
# Note: The line below has NO indentation, so it runs regardless of the if condition.
print("This line always runs")

print("\n--- 2. Bad Idea: Incorrect Indentation (IndentationError) ---")
# Rule: A wrong indentation can change program meaning or cause a crash.
# If you uncomment the lines below, Python will throw an IndentationError
# because the print statement under the 'if' block must be indented.

# if score >= 60:
# print("Passed")  <-- This will cause an error: IndentationError: expected an indented block


print("\n--- 3. Changing Program Meaning with Indentation ---")
# Rule: Indentation defines the block. Look at how it changes the logic.

score = 55
print(f"Current score: {score}")

if score >= 60:
    print("Result: Passed")
else:
    print("Result: Failed")
    # This line is indented inside the 'else' block.
    # It ONLY runs if the score is less than 60.
    print("Please try again next time.")

    # This line has no indentation. It is outside the if/else block.
# It ALWAYS runs.
print("Grade evaluation complete.")

print("\n--- 4. Nested Indentation Example ---")
# Rule: Use 4 spaces for each level. Here we use 4 spaces, then another 4 spaces (8 total).
is_student = True
final_score = 90

if is_student:  # First level
    if final_score >= 60:  # Second level
        print("Student has passed the course.")
    else:
        print("Student has failed the course.")





Task= 7==========================================

age = int(input("Age: "))
if age >= 18:
    print("Adult")
else:
    print("Not adult")
print("Check completed")

# Get user input and convert it to an integer
age = int(input("Age: "))

# Check if the age is 18 or older
if age >= 18:
    print("Adult")
else:
    print("Not adult")

# This line runs regardless of the condition
print("Check completed")
# Program to check if a person is an adult or not

# Taking input from the user
age = int(input("Age: "))

# The if-else block
if age >= 18:
    print("Adult")
else:
    print("Not adult")

# This line is outside the if-else block, so it will always run
print("Check completed")

Example Output 1 (If age is 20):

text
Age: 20
Adult
Check completed
Example Output 2 (If age is 15):

text
Age: 15
Not adult
Check completed

Tasks=8========================================

Drafting the Code
score = int(input("Score: "))

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "Fail"

print(f"Grade: {grade}")

Drafting an Additional Example

age = int(input("Enter your age: "))

if age < 5:
    price = 0
elif age <= 12:
    price = 5
elif age <= 65:
    price = 10
else:
    price = 7 # Senior discount

print(f"Ticket price: ${price}")

Example 1: Grade Calculator

# Get the score from the user and convert it to an integer
score = int(input("Score: "))

# Check conditions from top to bottom
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    # This handles the remaining cases (anything below 60)
    grade = "Fail"

# Print the final result using an f-string
print(f"Grade: {grade}")

Example 2: Movie Ticket Pricing

age = int(input("Enter your age: "))

# Determine the ticket price based on age brackets
if age < 5:
    price = 0  # Infants get in free
elif age <= 12:
    price = 5  # Child price
elif age <= 65:
    price = 12 # Adult price
else:
    price = 8  # Senior citizen discount

print(f"Your ticket price is: ${price}")

Tasks=9=============================================

# ==========================================
# Topic: Order Matters in elif Chains
# ==========================================

# Scenario 1: Wrong Order (Broad condition first)
print("--- Wrong Order ---")
score = 95

if score >= 60:  # Broad condition (True for 95)
    print("Passed")  # This runs first, and Python stops checking!
elif score >= 90:  # Specific condition (Never reached)
    print("Excellent")

# Output: Passed
# Reason: 95 >= 60 is True, so the program stops and hides the "Excellent" result.


# ==========================================

# Scenario 2: Better Order (Specific condition first)
print("\n--- Better Order ---")
score = 95

if score >= 90:  # Specific condition checked first
    print("Excellent")  # This runs and Python stops checking!
elif score >= 60:  # Broad condition (Only reached if score < 90)
    print("Passed")

# Output: Excellent
# Reason: By placing the more specific condition first, we correctly identify
# the high score before the general "Passed" condition can catch it.

Tasks =10==============================================

# Nested Conditions Example: Online Exam Eligibility

# Variables (You can change these values to test the program)
fees_paid = True
attendance_percentage = 80

# Outer Condition: Check if the student has paid the fees
if fees_paid:
    print("Fees status: Verified.")

    # Inner/Nested Condition: Check the attendance
    if attendance_percentage >= 75:
        print("Attendance is sufficient.")
        print("Result: You are eligible to take the exam.")
    else:
        print("Attendance is below 75%.")
        print("Result: You are NOT eligible due to low attendance.")

else:
    # This block executes if the outer 'if' condition is False
    print("Fees status: Pending.")
    print("Result: You must pay the fees first to check eligibility.")
Sample output
Fees status: Verified.
Attendance is sufficient.
Result: You are eligible to take the exam.

Tasks=11=================================

# ==========================================
# Program: Truthiness in Conditions
# Description: Demonstrating how Python evaluates non-Boolean values
# ==========================================

print("--- 1. Testing Strings (Empty vs Non-empty) ---")

# Empty string (Falsy)
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("Name is empty (Falsy)")

# Non-empty string (Truthy)
name = "Alice"
if name:
    print(f"Hello, {name}")
else:
    print("Name is empty (Falsy)")


print("\n--- 2. Testing Numbers (Zero vs Non-zero) ---")

# Zero (Falsy)
count = 0
if count:
    print(f"Count is {count} (Truthy)")
else:
    print("Count is 0 (Falsy)")

# Non-zero number (Truthy)
count = 5
if count:
    print(f"Count is {count} (Truthy)")
else:
    print("Count is 0 (Falsy)")


print("\n--- 3. Testing Lists (Empty vs Non-empty) ---")

# Empty list (Falsy)
numbers = []
if numbers:
    print(f"Sum of numbers: {sum(numbers)}")
else:
    print("No numbers yet (Falsy - Empty list)")

# Non-empty list (Truthy)
numbers = [10, 20, 30]
if numbers:
    print(f"Sum of numbers: {sum(numbers)}")
else:
    print("No numbers yet (Falsy - Empty list)")


print("\n--- 4. Interactive Example (from the slide) ---")

# Taking user input to demonstrate truthiness dynamically
user_name = input("Enter your name: ")

if user_name:
    print(f"Hello, {user_name}")
else:
    print("Name is empty")


