NSU Python — Lab 04

Tasks=1=====================================
# Topic: Control Flow II - while Loops, Typing, Identity, and Functions

# 1. FUNCTIONS & TYPING (Type Hints)
# We define a function with type hints (float, int) -> float | None
def average(total: float, count: int) -> float | None:
    """
    Calculates the average.
    Returns None if the count is zero.
    """
    # 2. IDENTITY & CONTROL FLOW
    # '==' checks for value equality. Since small integers are cached in Python,
    # it's better to use '==' here. However, we will use 'is None' later for identity.
    if count == 0:
        return None
    return total / count


def main():
    total_sum = 0.0
    item_count = 0

    print("--- Average Calculator ---")
    print("Enter numbers to add to the total. Type 'exit' to finish.")

    # 3. WHILE LOOP (Control Flow)
    while True:
        user_input = input("Enter a number (or 'exit'): ")

        # 4. TYPING (Checking the data type)
        # The input() function always returns a String.
        print(f"Debug: The type of user_input is {type(user_input)}")

        if user_input.lower() == 'exit':
            break

        try:
            # Convert string input to a floating-point number
            number = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a numeric value or 'exit'.")
            continue

        total_sum += number
        item_count += 1

    # Calling the function defined above
    result = average(total_sum, item_count)

    # 5. IDENTITY
    # 'is None' checks for identity (if the object is exactly the None singleton)
    if result is None:
        print("No numbers were entered, so the average is undefined (None).")
    else:
        print(f"The average of the entered numbers is: {result}")


# Run the program
if __name__ == "__main__":
    main()
Tasks=2============================================

# Program to demonstrate For Loops with Lists and Ranges

# --- Part 1: Iterating over a List ---
print("--- Part 1: Iterating over a list ---")
tasks = ["Check emails", "Write report", "Attend meeting", "Review code"]

# Looping through each item in the 'tasks' list
for task in tasks:
    print("Task to do:", task)


# --- Part 2: Iterating using range() ---
print("\n--- Part 2: Iterating using range() ---")
total_rounds = 4

# Looping a specific number of times (0 to 3)
for i in range(total_rounds):
    # i + 1 is used because range starts counting from 0 by default
    print("Starting round number:", i + 1)

print("\nAll rounds completed successfully!")
Tasks=3===============================

# Initialize the counter variable
count = 1

# The while loop checks the condition before every iteration.
# As long as 'count' is less than or equal to 5, it keeps running.
while count <= 5:
    print(count)   # Print the current value of count
    count += 1     # Increment the counter (This moves it toward stopping!)

# This statement executes only after the condition becomes False.
print("Done")
OUTPUT:
text
1
2
3
4
5
Done
Program 2: Another example (Countdown)

# Initialize the countdown
count = 5

# Loop while count is greater than 0
while count > 0:
    print(count)
    count -= 1  # Decrement the variable so the loop eventually stops

print("Blast off!")
Output:

text
5
4
3
2
1
Blast off!
Tasks=4==========================
# Initialize the variable to an empty string
password = ""

# The loop will continue as long as the password is not "python"
while password != "python":
    # Read input inside the loop
    password = input("Enter the password: ")

    # Optional: Provide feedback for wrong attempts
    if password != "python":
        print("Incorrect password. Try again.")

# This line executes only when the loop condition becomes false
print("Access granted!")
Program 2: Number Guessing Game (Another example of the same topic)
# Set a secret number
secret_number = 7

# Initialize user guess to something that is not the secret number
guess = 0

print("Guess the secret number (between 1 and 10)!")

# Loop until the user guesses correctly
while guess != secret_number:
    # Take user input inside the loop
    guess = int(input("Enter your guess: "))

    # Check if the guess is wrong to give a hint
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")

print("Congratulations! You guessed the correct number.")
Tasks=5=============================
while True:
    print("\n--- Main Menu ---")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        print("Hello!")
    elif choice == '2':
        print("Goodbye!")
    elif choice == '3':
        print("Exiting program...")
        break  # Controlled exit
    else:
        print("Invalid choice. Please try again.")
Tasks=6=======================================
number = 0

while number < 5:
    number += 1

    if number == 3:
        continue
Expected
Output:
text
1
2
4
5

print(number)
Tasks=7===================================
print("--- Example 1: For Loop (Without Break) ---")
# The loop will finish naturally because all numbers are even
numbers_even = [2, 4, 6, 8]

for n in numbers_even:
    if n % 2 != 0: # Condition is never true
        print("Found an odd number:", n)
        break
else:
    # This runs because the loop completed without hitting 'break'
    print("All values are even.")

print("\n--- Example 2: For Loop (With Break) ---")
# The loop will hit a break because 5 is an odd number
numbers_odd = [2, 4, 5, 8]

for n in numbers_odd:
    if n % 2 != 0:
        print("Found an odd number:", n)
        break
else:
    # This does NOT run because the loop was terminated by 'break'
    print("All values are even.")

print("\n--- Example 3: While Loop (Search Problem) ---")
# A classic use case: searching for an item
target_password = "secret"
passwords_to_try = ["123", "admin", "guest"]
index = 0

while index < len(passwords_to_try):
    if passwords_to_try[index] == target_password:
        print(f"Password found: {passwords_to_try[index]}")
        break
    index += 1
else:
    # This runs because the while loop condition became False (list exhausted) without a break
    print("Password not found in the list.")
Expected Output:
text
--- Example 1: For Loop (Without Break) ---
All values are even.

--- Example 2: For Loop (With Break) ---
Found an odd number: 5

--- Example 3: While Loop (Search Problem) ---
Password not found in the list.
Tasks=8========================================
# Program to print a multiplication table from 1 to 3
# This demonstrates Nested Loops (a loop inside another loop)

print("Multiplication Table:")
print("-" * 25)

# Outer loop: iterates through rows (1, 2, 3)
for i in range(1, 4):

    # Inner loop: iterates through columns (1, 2, 3)
    for j in range(1, 4):
        # Calculate the product of the current row and column
        product = i * j

        # Print the product with a fixed width for neat alignment
        # end=" " prevents going to a new line immediately
        print(f"{product:4}", end="")

    # After the inner loop completes for the current row,
    # print() moves the cursor to the next line
    print()
Expected Output:
text
Multiplication Table:
-------------------------
   1   2   3
   2   4   6
   3   6   9
# Program to print coordinates for a 3x3 grid
# This demonstrates how the inner loop completes for each outer loop step.

for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print() # New line after the inner loop finishes
Output:

text
(1,1) (1,2) (1,3)
(2,1) (2,2) (2,3)
(3,1) (3,2) (3,3)
Tasks=9========================================
# Topic: Variables and Assignment in Python

print("--- 1. Dynamic Typing & Reassignment ---")
# 1. A Python variable name refers to an object.
x = 10
print(f"x = 10, type of x: {type(x)}")

# The name can later refer to another object of a different type.
x = "Python"
print(f"x = 'Python', type of x: {type(x)}")


print("\n--- 2. Assignment and Object References ---")
# 2. Assignment does not necessarily copy data.
# Here, 'numbers' is a list object.
numbers = [1, 2, 3]

# 'other' is assigned to 'numbers'. They both point to the EXACT SAME object in memory.
other = numbers

print(f"Original 'numbers': {numbers}")
print(f"Assigned 'other':   {other}")

# Let's verify they point to the same memory address using id()
print(f"Memory ID of 'numbers': {id(numbers)}")
print(f"Memory ID of 'other':   {id(other)}")

# 3. Modifying one variable affects the other because they share the same object.
other.append(4) # Adding 4 to the list using 'other' variable

print("\nAfter appending 4 to 'other':")
print(f"Numbers: {numbers}") # Notice that 'numbers' is also updated!
print(f"Other:   {other}")
Tasks=10==========================================
# --- Object and Reference Demonstration ---

print("--- Example 1: Reference (Aliasing) ---")
a = [1, 2, 3]
b = a  # 'b' now references the SAME list object as 'a'

print(f"Initial a: {a}")
print(f"Initial b: {b}")

# Modifying the list through 'b'
b.append(4)

print(f"After appending to b:")
print(f"a: {a}") # a is also changed!
print(f"b: {b}")

# Proof that they are the same object in memory
print(f"ID of a: {id(a)}")
print(f"ID of b: {id(b)}")
print("Both have the same ID, confirming they point to the same object.")


print("\n--- Example 2: How to make an independent copy ---")
c = [1, 2, 3]
d = c.copy()  # Creating a shallow copy of the list

print(f"Initial c: {c}")
print(f"Initial d: {d}")

# Modifying the copy
d.append(4)

print(f"After appending to d:")
print(f"c: {c}") # c remains unchanged
print(f"d: {d}")

print(f"ID of c: {id(c)}")
print(f"ID of d: {id(d)}")
print("Different IDs, confirming they are independent objects.")
Tasks=11===============================
# Topic: Object Identity, References, and the id() function

print("--- 1. Creating Variables and Checking IDs ---")

# 'a' is assigned a new list object [1, 2]
a = [1, 2]

# 'b' is assigned 'a'. This means 'b' points to the EXACT SAME list object as 'a' (Reference).
b = a

# 'c' is assigned a NEW list object [1, 2]. Even though it has the same values, it's a different object.
c = [1, 2]

# id() returns the identity (memory address) of the object
print(f"ID of a: {id(a)}")
print(f"ID of b: {id(b)}  <-- Same as 'a' (shared reference)")
print(f"ID of c: {id(c)}  <-- Different from 'a' (new object)")


print("\n--- 2. Comparing Values vs. Identities ---")

# '==' compares the VALUES (contents) of the objects
print(f"a == c: {a == c}")

# 'is' compares the IDENTITIES (memory addresses) of the objects
print(f"a is c: {a is c}")

# 'a' and 'b' point to the same object, so 'is' returns True
print(f"a is b: {a is b}")


print("\n--- 3. Demonstrating Mutable References (Optional but helpful) ---")

# Because 'a' and 'b' point to the same list, modifying 'b' will also change 'a'
b.append(3)
print(f"After b.append(3):")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}  <-- 'c' remains unchanged because it is a separate object.")
Expected Output:
--- 1. Creating Variables and Checking IDs ---
ID of a: 140245123456768
ID of b: 140245123456768  <-- Same as 'a' (shared reference)
ID of c: 140245123456832  <-- Different from 'a' (new object)

--- 2. Comparing Values vs. Identities ---
a == c: True
a is c: False
a is b: True

--- 3. Demonstrating Mutable References (Optional but helpful) ---
After b.append(3):
a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2]
Tasks=12===============================================

# Python Program: == versus is

def main():
    print("--- 1. Comparing Lists (Value vs Identity) ---")

    # Creating two different lists with the same values
    a = [1, 2]
    b = [1, 2]

    # Creating a reference to the first list
    c = a

    # '==' checks for VALUE equality
    print(f"a == b: {a == b}")
    # Output: True (Because both lists contain [1, 2])

    # 'is' checks for OBJECT IDENTITY (are they the exact same object in memory?)
    print(f"a is b: {a is b}")
    # Output: False (Because 'a' and 'b' are two completely different objects in memory)

    # 'c' was assigned to 'a', so they point to the exact same object
    print(f"a is c: {a is c}")
    # Output: True (Because 'c' is just another name for the same object 'a')

    print("\n--- 2. Best Practice: Checking for None ---")

    # The most common and safe use of 'is' is checking for None.
    value = None

    # Recommended way to check for None
    if value is None:
        print("Correct: The value is None. (Used 'is')")

    # Using '==' works here, but PEP 8 (Python style guide) recommends against it.
    if value == None:
        print("Not Recommended: The value is None. (Used '==')")


if __name__ == "__main__":
    main()
Tasks=13=================================================


# Program to demonstrate the use of 'is None' and 'is not None'

def verify_variable(var):
    """Function to check if a variable contains a value or not."""

    # 1. Checking if the variable is None
    # Slide tip: Use 'is None', not '== None'
    if var is None:
        print("Result: No value found. The variable is None.")

    # 2. Checking if the variable is NOT None
    # Slide tip: Use 'is not None' for the opposite check
    elif var is not None:
        print(f"Result: Value found. The variable is: {var}")


# --- Main Program Execution ---

# Scenario 1: Initialize a variable with None (meaning "no value")
user_data = None
print("--- Scenario 1: Initial State ---")
verify_variable(user_data)

print("\n--- Scenario 2: After Assigning a Value ---")

# Scenario 2: Assign a value to the variable
user_data = "Python Programming"
verify_variable(user_data)

# Scenario 3 (Optional): Testing with a falsey value to prove 'is not None' works
print("\n--- Scenario 3: Testing with Zero (0) ---")
# Note: 0 is falsey, but it is NOT None. Using 'is not None' correctly detects it.
number = 0
if number is not None:
    print(f"Result: The number is not None. It is {number}.")
Output of the program:
--- Scenario 1: Initial State ---
Result: No value found. The variable is None.

--- Scenario 2: After Assigning a Value ---
Result: Value found. The variable is: Python Programming

--- Scenario 3: Testing with Zero (0) ---
Result: The number is not None. It is 0.
Tasks=14==================================================
# 1. Create a mutable list
a = [10, 20]
print(f"Step 1: Original list 'a' = {a}")

# 2. Assign 'a' to 'b' (This does NOT copy the list)
b = a

# 3. Check if they are the exact same object in memory
print(f"Step 2: Is 'a' the same object as 'b'? {a is b}")

# 4. Modify the first element of 'b'
b[0] = 99

# 5. Print both lists to see the effect
print("\nStep 3: After modifying 'b[0] = 99'")
print(f"List 'a' = {a}") # 'a' is also changed!
print(f"List 'b' = {b}")

# 6. Create a proper independent copy using .copy()
c = a.copy()
print(f"\nStep 4: Created a copy 'c' = {c}")

# 7. Check if 'a' and 'c' are the same object
print(f"Is 'a' the same object as 'c'? {a is c}")

# 8. Modify the copy 'c'
c[0] = 50

# 9. Print both lists to see that 'a' remains unchanged
print("\nStep 5: After modifying 'c[0] = 50'")
print(f"List 'a' (Unchanged) = {a}")
print(f"List 'c' (Modified)  = {c}")
Expected Output:
Step 3: After modifying 'b[0] = 99'
List 'a' = [99, 20]
List 'b' = [99, 20]

Step 4: Created a copy 'c' = [99, 20]
Is 'a' the same object as 'c'? False

Step 5: After modifying 'c[0] = 50'
List 'a' (Unchanged) = [99, 20]
List 'c' (Modified)  = [50, 20]

Tasks=15===============================================


# Why Functions? - Demonstrating code reusability and avoiding repeated logic.

def calculate_discounted_price(price, discount_percentage):
    """
    This function calculates the final price after applying a discount.
    It represents the 'processing' part of the logic.
    """
    # Processing: Calculate the discount amount and subtract it from the original price
    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount

    # Output: Return the calculated final price
    return final_price


# --- Main Program Execution ---

print("--- Product 1 ---")
# Input
price1 = 100
discount1 = 10

# Processing & Output
# Instead of writing the math formula again, we just call the function.
final1 = calculate_discounted_price(price1, discount1)
print(f"Original Price: {price1}, Discount: {discount1}%, Final Price: {final1}")

print("\n--- Product 2 ---")
# Input
price2 = 250
discount2 = 15

# Processing & Output
# Reusing the same function with different inputs.
final2 = calculate_discounted_price(price2, discount2)
print(f"Original Price: {price2}, Discount: {discount2}%, Final Price: {final2}")

# Testing the function easily with a third scenario
print("\n--- Product 3 (Testing) ---")
final3 = calculate_discounted_price(500, 20)
print(f"Original Price: 500, Discount: 20%, Final Price: {final3}")

Tasks=16====================================

# 1. Defining a simple function (without parameters) as shown in the slide
def greet():
    # The function body must be indented
    print("Hello")
    print("Welcome to Python")

# 2. Defining a function with parameters (to show the use of parentheses)
def greet_user(name):
    print(f"Hello, {name}!")
    print("Welcome to Python")

# --- Main part of the program (Calling the functions) ---

print("--- Calling the basic function ---")
# Calling the function executes its body
greet()
greet()  # Calling it twice prints the message twice

print("\n--- Calling the function with a parameter ---")
# Passing arguments to the function
greet_user("Alice")
greet_user("Bob")

Tasks=17=======================================

# ==========================================
# Program: Demonstrating Function Parameters
# ==========================================

# 1. Function with a single parameter
# (Similar to the greet(name) example in your slide)
def greet_user(name):
    """Greets the user with the provided name."""
    print(f"Hello, {name}! Welcome to the program.")

# 2. Function with multiple parameters
# (Similar to the print_area(width, height) example in your slide)
def calculate_rectangle_area(length, width):
    """Calculates and prints the area of a rectangle."""
    area = length * width
    print(f"The area of the rectangle (Length: {length}, Width: {width}) is: {area}")

# 3. Function with multiple parameters and a DEFAULT parameter
def calculate_total_price(price, quantity, tax_rate=0.05):
    """Calculates total price. Tax rate is optional and defaults to 5%."""
    subtotal = price * quantity
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount
    print(f"Item Price: ${price:.2f} | Quantity: {quantity} | Tax Rate: {tax_rate * 100}%")
    print(f"Total Cost: ${total:.2f}\n")

# ==========================================
# Main Program Execution
# ==========================================
if __name__ == "__main__":
    print("--- Function Parameters Demo ---\n")

    # Calling function with a single argument
    greet_user("Alice")
    greet_user("Rahim")
    print("-" * 40)

    # Calling function with multiple arguments
    calculate_rectangle_area(5, 10)
    calculate_rectangle_area(7.5, 4)
    print("-" * 40)

    # Calling function using the DEFAULT parameter (tax_rate will be 0.05)
    print("Scenario A: Using default tax rate")
    calculate_total_price(100, 2)

    # Calling function OVERRIDING the default parameter (tax_rate will be 0.10)
    print("Scenario B: Overriding default tax rate")
    calculate_total_price(100, 2, 0.10)
Tasks=18=======================================================

# Program to demonstrate the concept of 'return' in Python functions

# 1. Basic Return: Sending a result back to the caller
def calculate_area(width, height):
    area = width * height
    return area  # Returns the calculated value back to the caller

# 2. Returned values can be stored in variables
stored_result = calculate_area(5, 3)
print(f"Stored result: {stored_result}")

# 3. Returned values can be reused or directly printed
print(f"Directly printed result: {calculate_area(10, 2)}")
# Reusing the returned value in another calculation
combined_area = calculate_area(4, 4) + calculate_area(2, 2)
print(f"Combined area using reused values: {combined_area}")


# 4. Printing is NOT the same as returning
def print_area_not_return(width, height):
    area = width * height
    print(f"Inside print_area_not_return: The area is {area}")
    # Note: No return statement here!

# This will print the message inside the function,
# but the variable will actually hold 'None' because there is no return statement.
returned_value = print_area_not_return(6, 6)
print(f"Value stored from the print function: {returned_value}")


# 5. A function can return early
def check_even_or_odd(number):
    if number % 2 != 0:
        return "Odd"  # Early return: the function ends here for odd numbers
    return "Even"     # This line only executes if the number is even

print(f"Checking 7: {check_even_or_odd(7)}")
print(f"Checking 4: {check_even_or_odd(4)}")

Tasks=19====================================

# Program to demonstrate functions without a return statement in Python

# 1. Function WITHOUT a return statement
def show_area(width, height):
    """
    This function calculates the area and prints it directly.
    It does NOT have a return statement.
    """
    area = width * height
    print(f"Inside the function: The area is {area}")
    # Notice there is no 'return area' here

# 2. Function WITH a return statement
def calculate_area(width, height):
    """
    This function calculates the area and returns the value.
    """
    area = width * height
    return area


print("--- Testing function WITHOUT return (show_area) ---")
# We assign the function call to a variable
value_1 = show_area(5, 3)

# The function executes and prints the area
print(f"The value of 'value_1' is: {value_1}")
print(f"The type of 'value_1' is: {type(value_1)}")
print("Explanation: Since there was no 'return' statement, Python automatically returned 'None'.\n")


print("--- Testing function WITH return (calculate_area) ---")
# We assign the function call to a variable
value_2 = calculate_area(5, 3)

# The function does NOT print anything by itself
print(f"The value of 'value_2' is: {value_2}")
print(f"The type of 'value_2' is: {type(value_2)}")
print("Explanation: The 'return' statement sent the value back to the caller, so we can store and use it.")

Output of the program:
--- Testing function WITHOUT return (show_area) ---
Inside the function: The area is 15
The value of 'value_1' is: None
The type of 'value_1' is: <class 'NoneType'>
Explanation: Since there was no 'return' statement, Python automatically returned 'None'.

--- Testing function WITH return (calculate_area) ---
The value of 'value_2' is: 15
The type of 'value_2' is: <class 'int'>
Explanation: The 'return' statement sent the value back to the caller, so we can store and use it.

Tasks=20===================================


def convert_seconds(total_seconds):
    """
    This function takes total seconds and returns
    hours, minutes, and remaining seconds as multiple values.
    """
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600

    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    # Returning multiple values (implicitly creates a tuple)
    return hours, minutes, seconds


# Taking a sample input (e.g., 3665 seconds)
time_in_seconds = 3665

# Unpacking the returned multiple values into separate variables
h, m, s = convert_seconds(time_in_seconds)

# Printing the results using f-strings
print(f"Total Seconds: {time_in_seconds}")
print(f"Hours: {h}")
print(f"Minutes: {m}")
print(f"Seconds: {s}")

Expected Output:

Total Seconds: 3665
Hours: 1
Minutes: 1
Seconds: 5

Tasks=21=================================


# Topic: Local Variables in Python
# A local variable is a variable declared inside a function.
# It can only be accessed within that specific function.

def calculate_bmi(weight_kg, height_m):
    """
    This function calculates the Body Mass Index (BMI).
    'weight_kg' and 'height_m' are parameters (which are also local).
    'bmi' is a LOCAL variable created inside this function.
    """
    # Creating a local variable named 'bmi'
    bmi = weight_kg / (height_m ** 2)

    # Returning the local variable's value to the caller
    return bmi


# --- Main Program Execution ---

# Here, 'result' is a GLOBAL variable because it's defined outside any function.
# We call the function and store its returned value in 'result'.
result = calculate_bmi(70, 1.75)

# Printing the global variable works perfectly
print(f"The calculated BMI is: {result:.2f}")

# --- Demonstrating the Local Scope Rule ---

# The following line will cause an error if you uncomment it!
# print(bmi)

# Explanation:
# If you try to run `print(bmi)` here, Python will throw a "NameError: name 'bmi' is not defined"
# This is because 'bmi' is a local variable. It was born inside the 'calculate_bmi' function,
# lived its life there, and was destroyed as soon as the function finished executing.
# The outside program (the global scope) has no access to it.

Tasks=22==============================================


# Function to calculate the average
def average(total, count):
    # Validation: Prevent division by zero
    if count == 0:
        return None
    return total / count


# Loop: Ask for input until valid (validation loop)
while True:
    # Note: A try/except block is better for handling non-integer inputs
    count = int(input("Count: "))

    # Condition: Check if the count is valid (non-negative)
    if count >= 0:
        break
    print("Count cannot be negative")

# Call the function with a fixed total (120) and the validated count
result = average(120, count)

# Condition: Handle the result returned from the function
if result is None:
    print("Cannot divide by zero")
else:
    print(f"Average = {result:.2f}")

Program 2:

def calculate_average(total_sum, number_count):
    """
    Function to calculate the average.
    Returns None if the count is zero to prevent a ZeroDivisionError.
    """
    if number_count == 0:
        return None
    return total_sum / number_count

def main():
    # 1. Validation Loop: Get a valid count of numbers from the user
    while True:
        try:
            count = int(input("How many numbers do you want to average? "))
            if count > 0:
                break
            elif count == 0:
                print("Count cannot be zero. Please enter a positive integer.")
            else:
                print("Count cannot be negative. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # 2. Loop: Collect the numbers from the user
    total = 0
    for i in range(count):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                total += num
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # 3. Function Call: Calculate the average
    result = calculate_average(total, count)

    # 4. Condition: Output the result
    if result is None:
        print("Cannot calculate average: division by zero.")
    else:
        print(f"The average of your numbers is: {result:.2f}")

# Run the program
if __name__ == "__main__":
    main()

