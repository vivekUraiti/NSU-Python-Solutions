# """
# Lab 02 — Python Basics II

# Complete all tasks below.

# Topics:
# - built-in functions
# - assignment and augmented assignment
# - operator precedence
# - type conversion
# - strings
# - print() options
# - collections
# - mutable and immutable objects
# - formatted output
# - basic PEP 8
# - reading common errors

# Do not use:
# - if
# - for
# - while
# - user-defined functions
# """


# # ============================================================
# # Task 1 — Built-in Functions
# # ============================================================

# print("Task 1 — Built-in Functions")

# values = [12, 7, 19, 5, 14]

# # TODO:
# # Using built-in functions, calculate and print:
# #
# # number of values
# # smallest value
# # largest value
# # total
# # mean
# #
# # Do not calculate these manually.

# count = 0
# smallest = 0
# largest = 0
# total = 0
# mean = 0.0

# # TODO:
# # Print the results using f-strings.
# print(f"Number of values: {len(values)}")
# print(f"Smallest value: {min(values)}")
# print(f"Largest value: {max(values)}")
# print(f"Total: {sum(values)}")
# print(f"Mean: {sum(values) / len(values):.2f}")


# # ============================================================
# # Task 2 — Absolute Value and Rounding
# # ============================================================

# print("Task 2 — Absolute Value and Rounding")

# temperature_change = -7.438
# measurement = 19.87654

# # TODO:
# # Print the absolute value of temperature_change.
# #
# # Expected numerical value:
# # 7.438

# print(f"Absolute value of temperature_change: {abs(temperature_change)}")

# # TODO:
# # Round measurement to:
# #
# # 1 decimal place
# # 2 decimal places
# # 3 decimal places
# #
# # Use round().

# rounded_1 = round(measurement, 1)
# rounded_2 = round(measurement, 2)
# rounded_3 = round(measurement, 3)

# print(f"Rounded to 1 decimal place: {rounded_1}")
# print(f"Rounded to 2 decimal places: {rounded_2}")
# print(f"Rounded to 3 decimal places: {rounded_3}")




# # ============================================================
# # Task 3 — Assignment and Augmented Assignment
# # ============================================================

# print("Task 3 — Assignment and Augmented Assignment")

# balance = 1000.0

# # Perform the following operations using augmented assignment:
# #
# # 1. Add 250 to the balance.
# # 2. Subtract 120.
# # 3. Multiply the remaining balance by 1.05.
# #
# # TODO:
# # Replace the normal assignments below with +=, -=, and *=.

# balance += 250
# balance = balance + 250
# balance -= 120
# balance *= 1.05

# # TODO:
# # Print the final balance with two decimal places.


# print(f"Final balance: ${balance:.2f}")


# # ============================================================
# # Task 4 — Operator Precedence
# # ============================================================

# print("Task 4 — Operator Precedence")

# # Before running the program, predict each result.

# expression_1 = 2 + 3 * 4
# expression_2 = (2 + 3) * 4
# expression_3 = 20 / 5 + 3
# expression_4 = 20 / (5 + 3)
# expression_5 = 2 ** 3 ** 2

# # TODO:
# # Print each expression and its result.
# #
# # Example:
# # 2 + 3 * 4 = 14
# # (2 + 3) * 4 = 20
# # (20 / 5) + 3 = 7.0
# # (20 / (5 + 3)) = 2.5
# # 2 ** 3 ** 2 = 512


# print(f"2 + 3 * 4 = {expression_1}")
# print(f"(2 + 3) * 4 = {expression_2}")
# print(f"(20 / 5) + 3 = {expression_3}")
# print(f"(20 / (5 + 3)) = {expression_4}")
# print(f"2 ** 3 ** 2 = {expression_5}")


# # ============================================================
# # Task 5 — Time Conversion
# # ============================================================

# print("Task 5 — Time Conversion")

# # TODO:
# # Ask the user to enter a number of seconds.

# total_seconds = input("Enter a number of seconds: ")

# # TODO:
# # Convert the input to int.
# integer_seconds = int(total_seconds)

# # TODO:
# # Calculate:
# #
# # whole minutes
# # remaining seconds
# #
# # Example:
# # 135 seconds -> 2 minutes and 15 seconds
# #
# # Hint:

# minutes = integer_seconds // 60
# remaining_seconds = integer_seconds % 60

# # TODO:
# # Print:
# # 135 seconds = 2 minute(s) and 15 second(s)


# print(f"{integer_seconds} seconds = {minutes} minute(s) and {remaining_seconds} second(s)")


# # ============================================================
# # Task 6 — Conversion Is Not Always Reversible
# # ============================================================

# print("Task 6 — Type Conversion")

# value = 17.95

# # TODO:
# # Convert value to int and print it.
# #
# # Question:
# # Does int() round the value?

# integer_value = int(value)
# print(f"Integer value: {integer_value}")

# # TODO:
# # Convert integer_value back to float and print it.

# float_value = float(integer_value)
# print(f"Float value: {float_value}")

# # TODO:
# # Convert integer_value to str and print:
# #
# # Value as text: <value>
# print(f"Value as text: {str(integer_value)}")
# # Type: <type>
# print(f"Type: {type(str(integer_value))}")
# # Use type() for the second line.






# # ============================================================
# # Task 7 — Basic String Operations
# # ============================================================

# print("Task 7 — Basic String Operations")

# first_name = input("First name: ")
# last_name = input("Last name: ")

# # TODO:
# # Create full_name using string concatenation.

# full_name = first_name + last_name

# # TODO:
# # Print:
# #
# # Full name: <full_name>
# print(f"Full name: {full_name}")
# # Number of characters: <length>
# print(f"Number of characters: {len(full_name)}")
# # First character: <first character>
# print(f"First character: {full_name[0]}")
# # Last character: <last character>
# print(f"Last character: {full_name[-1]}")
# # First three characters: <slice>
# print(f"First three characters: {full_name[:3]}")

# # TODO:
# # Print full_name three times using string repetition.


# print(f"{full_name} " * 3)


# # ============================================================
# # Task 8 — Useful print() Options
# # ============================================================

# print("Task 8 — Useful print() Options")

# language = "Python"
# course = "AI and Big Data Analytics"
# university = "NSU"

# # TODO:
# # Print the three values on one line separated by:
# #
# print(language, course, university, sep=" | ")
# #
# # Expected:
# # Python | AI and Big Data Analytics | NSU
# #
# # Use sep=


# # TODO:
# # Use two print() calls and end= so that the result is:
# #
# # Python Programming
# #
# # Do not write "Python Programming" as one string.


# print("Python", end=" ")
# print("Programming")


# # ============================================================
# # Task 9 — Collections and Choosing Data Structures
# # ============================================================

# print("Task 9 — Collections")

# student_name = "Anna"
# student_age = 22
# student_skills = ["Python", "Mathematics", "Machine Learning"]
# student_university = "NSU"

# # TODO:
# # Create a dictionary named student with the keys:
# #
# # name
# # age
# # skills
# # university

# student = {"name": student_name, "age": student_age, "Skills": student_skills, "university": student_university}

# # TODO:
# # Print:
# #
# # student's name
# # student's university
# # first skill
# # number of skills
# #
# # Use dictionary access, indexing, and len().


# print(student["name"])
# print(student["university"])
# print(student["Skills"][0])
# print(len(student["Skills"]))


# # ============================================================
# # Task 10 — Mutable and Immutable Objects
# # ============================================================

# print("Task 10 — Mutable and Immutable Objects")

# # List example — mutable

# numbers = [10, 20, 30]
# same_numbers = numbers

# # TODO:
# # Change the first item in numbers to 99.
# numbers[0] = 99
# # Then print both:
# print(numbers)
# #
# print(same_numbers)
# #
# # Observe what happened.


# # String example — immutable

# text = "Python"
# same_text = text

# # TODO:
# # Create a new string by adding " Course" to text.
# #
# # Then print:
# #
# # text
# # same_text
# #
# # Compare this result with the list example.


# print(text.replace("Python", "Python Course"))


# # ============================================================
# # Task 11 — Small Statistics Report
# # ============================================================

# print("Task 11 — Small Statistics Report")

# scores = [78, 92, 85, 69, 88]

# # TODO:
# # Calculate:
# #
# # number of scores
# # minimum score
# # maximum score
# # total score
# # mean score
# #
# # Use built-in functions.

# score_count = len(scores)
# minimum_score = min(scores)
# maximum_score = max(scores)
# total_score = sum(scores)
# mean_score = total_score / score_count

# # TODO:
# # Print a clean report:
# #
# print(f"Number of scores: {score_count}")
# print(f"Minimum: {minimum_score}")
# print(f"Maximum: {maximum_score}")
# print(f"Mean: {mean_score}")
# #
# # Format the mean to exactly two decimal places.


# print(f"Mean: {mean_score:.2f}")


# # ============================================================
# # Task 12 — PEP 8 Cleanup
# # ============================================================

# print("Task 12 — PEP 8 Cleanup")

# # The following code works, but it is difficult to read.
# #
# # TODO:
# # Rewrite it using:
# #
# # meaningful variable names
# # snake_case
# # spaces around operators
# # intermediate variables
# # formatted output
# #
# # Keep the same calculation.

# Price=1250
# Quantity=3
# Discount=0.1

# Total_discount = Price * Quantity - Discount / 100 * Price * Quantity

# print(f"Total discount: ${Total_discount:.2f}")




# ============================================================
# Optional Challenge — Student Score Summary
# ============================================================

print("Optional Challenge — Student Score Summary")

# Create a small program using only concepts from Sections 1–2.
#
# Ask the user for:
#
# student name
student_name = input("Enter the student's name: ")
# three test scores
test_scores = input("Enter three test scores separated by spaces: ")

#
# Store the three scores in a list.
scores = [int(x) for x in test_scores.split()]


# Calculate:
#
# minimum score
minimum_score = min(scores)
# maximum score
maximum_score = max(scores)
# mean score
mean_score = sum(scores) / len(scores)
#
# Print a clean summary similar to:
print(f"Student: {student_name}")
print(f"Scores: {scores}")
print(f"Minimum: {minimum_score:.2f}")
print(f"Maximum: {maximum_score:.2f}")
print(f"Mean: {mean_score:.2f}")
# Student: Anna
# Scores: [78.0, 85.0, 91.0]
# Minimum: 78.00
# Maximum: 91.00
# Mean: 84.67
#
# Use:
# input()
# float()
# list
# min()
# max()
# sum()
# len()
# f-strings


# ============================================================
# Task 13 — Multiple Assignment
# ============================================================

print("Task 13 — Multiple Assignment")

# TODO:
# Assign these three values using ONE statement:
#
# x = 10
# y = 20
# z = 30

x = 10
y = 20
z = 30

# TODO:
# Print x, y, and z.
print(10, 20, 30)


# TODO:
# Swap a and b using one Python statement.

a = 5
b = 10

# Expected after swapping:
# a = 10
# b = 5

a, b = b, a




print(f"After swapping: a = {a}, b = {b}")



# ============================================================
# Task 14 — String Methods
# ============================================================

print("Task 14 — String Methods")

text = "  Python Programming Course  "

# TODO:
# Print the text:
# 1. without surrounding spaces
text = text.strip()

# 2. in lowercase
print(text.lower())
# 3. in uppercase
print(text.upper())
# 4. with "Course" replaced by "Lab"
print(text.replace("Course", "lab"))

# TODO:
# Check and print whether the cleaned text:
#
# starts with "Python"
print(text.startswith("Python"))
# ends with "Course"
print(text.endswith("Course"))
#
# Use:
# strip()
# lower()
# upper()
# replace()
# startswith()
# endswith()


# ============================================================
# Task 15 — Boolean Expressions
# ============================================================

print("Task 15 — Boolean Expressions")

age = 22
score = 85
is_master_student = True

# TODO:
# Print the result of:

# age >= 18
print(age >= 18)
# score >= 60
print(score >= 60)
# score >= 60 and 
print(score >= 60 and age >= 18)
# score < 60 or age < 
print(score < 60 or age < 18)
# not is_master_student
print(not is_master_student)

# TODO:
# Predict and then print:

# bool(0)
print(f"Boolean expression: {bool(0)}")

# bool(1)
print(bool(1))
# bool("")
print(bool(""))
# bool("Python")
print(bool("Python"))
# bool([])
print(bool([]))
# bool([1, 2])
print(bool([1, 2]))



# ============================================================
# Task 16 — Membership
# ============================================================

print("Task 16 — Membership")

numbers = [10, 20, 30]
text = "Python Programming"
student = {
    "name": "Anna",
    "age": 22,
}

# TODO:
# Print the result of:

# 20 in numbers
print(20 in numbers)
# 50 not in numbers
print(50 not in numbers)
# "Python" in text
print("Python" in text)
# "Java" not in text
print("Java" not in text)
# "age" in student
print("age" in student)
# "email" in student
print("email" in student)

