"""
Lab 02 — Python Basics II

Complete all tasks below.

Topics:
- built-in functions
- assignment and augmented assignment
- operator precedence
- type conversion
- strings
- print() options
- collections
- mutable and immutable objects
- formatted output
- basic PEP 8
- reading common errors

Restrictions:
- No if
- No for
- No while
- No user-defined functions
"""
# --- 1. Built-in Functions & Type Conversion ---
num_str = "100"
num_int = int(num_str)          # Type conversion (str to int)
num_float = float(num_int)      # Type conversion (int to float)

print("--- Built-in Functions & Type Conversion ---")
print(f"Original string: '{num_str}'")
print(f"Converted to integer: {num_int}")
print(f"Converted to float: {num_float}")
print(f"Length of the string: {len(num_str)}")

# --- 2. Assignment & Augmented Assignment ---
# --- 3. Operator Precedence ---
counter = 10                    # Assignment
counter += 5                    # Augmented assignment (counter = counter + 5)
counter *= 2                    # Augmented assignment (counter = counter * 2)

# Precedence: Parentheses () > Exponent ** > Mult/Div * / > Add/Sub + -
result = 10 + 2 * 3 ** 2        # 3**2=9, 2*9=18, 10+18=28
result_precedence = (10 + 2) * 3 ** 2 # (12) * 9 = 108

print("\n--- Assignment, Augmented Assignment & Precedence ---")
print(f"Final counter value: {counter}")
print(f"Result (10 + 2 * 3 ** 2): {result}")
print(f"Result with parentheses: {result_precedence}")

# --- 4. Strings, Mutable & Immutable Objects ---
# Strings are immutable (cannot be changed in place)
greeting = "Hello"
# greeting[0] = 'J'  # <-- This would cause a TypeError (Common Error)
new_greeting = "J" + greeting[1:] # Creating a new string instead

print("\n--- Strings & Immutability ---")
print(f"Original string: {greeting}")
print(f"New string (immutable behavior): {new_greeting}")

# --- 5. Collections ---
# Lists are mutable (can be changed)
my_list = [1, 2, 3, 4, 5]
my_list.append(6)               # Modifying the list in place
my_list[0] = 99                 # Changing an element

# Dictionaries (key-value pairs)
my_dict = {"name": "Alice", "age": 25}
my_dict["age"] = 26             # Modifying a value

# Tuples are immutable
my_tuple = (10, 20, 30)

print("\n--- Collections (Lists, Dicts, Tuples) ---")
print(f"Mutable List: {my_list}")
print(f"Mutable Dictionary: {my_dict}")
print(f"Immutable Tuple: {my_tuple}")

# --- 6. Print() Options & Formatted Output ---
# Using sep (separator) and end (ending character)
print("\n--- Print Options & Formatted Output ---")
print("Apple", "Banana", "Cherry", sep=" | ")
print("This is on the ", end="")
print("same line.")

# Formatted output using f-strings and .format()
name = "Bob"
score = 95.5
print(f"Student: {name}, Score: {score:.2f}") # .2f formats to 2 decimal places
print("Student: {}, Score: {:.2f}".format(name, score))

# --- 7. Basic PEP 8 & Common Errors ---
# PEP 8: Variable names should be lowercase_with_underscores
# PEP 8: Spaces around operators (e.g., x = 1, not x=1)
# Common Error handling: Using try/except is not restricted, but we can
# demonstrate a common error by simply avoiding it.
# For example, trying to add a string and an integer directly would raise a TypeError.
# We safely avoid this by using proper type conversion (which we did at the top).