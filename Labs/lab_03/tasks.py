"""
NSU Python — Lab 03
Conditions and for Loops

Complete Tasks 1–12.
Tasks 13–14 are optional bonus tasks.

Use only concepts covered in Lecture 03.
"""


# ============================================================
# Task 1 — Positive, negative, or zero
# ============================================================
# Ask the user to enter an integer.
# Print exactly one of:
#   Positive
#   Negative
#   Zero
#
# Example:
# Input: -7
# Output: Negative

# Write your code below:

# number = int(input("Enter an integer: "))

# if number > 0: 
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")



# ============================================================
# Task 2 — Age category
# ============================================================
# Ask the user for their age.
#
# Print:
#   Child      -> age < 13
#   Teenager   -> 13–17
#   Adult      -> 18–64
#   Senior     -> 65 or older
#
# Test boundary values: 12, 13, 17, 18, 64, 65.

# Write your code below:

# age = int(input("Enter your age: "))

# if age < 13:
#     print("Child")
# elif 13 <= age and age <= 17:
#     print("Teenager")
# elif 18 <= age and age <= 64:
#     print("Adult")
# else:
#     print("Senior")


# ============================================================
# Task 3 — Grade classifier
# ============================================================
# Ask the user for a score.
#
# First check whether the score is between 0 and 100 inclusive.
#
# For a valid score:
#   A    -> 90–100
#   B    -> 75–89
#   C    -> 60–74
#   Fail -> below 60
#
# For an invalid score print:
#   Invalid score

# Write your code below:

# score = int(input("Enter your score: "))

# if score > 0 and score <= 100:
#     if score >= 90:
#         print("A")
#     elif score >= 75:
#         print("B")
#     elif score >= 60:
#         print("C")
#     else:
#         print("Fail")
# else:
#     print("Invalid score")


# ============================================================
# Task 4 — Access decision
# ============================================================
# Ask the user for:
#   age
#   whether they have a ticket: yes/no
#
# A person may enter only if:
#   age >= 18 AND they have a ticket.
#
# Print one of:
#   Access granted
#   Ticket required
#   Must be 18 or older

# Write your code below:

# age = int(input("Enter your age: "))

# if age >= 18:
#     ticket = input("Do you have a ticket? (yes/no): ")
#     if ticket.lower() == "yes":
#         print("Access granted")
#     else:
#         print("Ticket required")
# else:
#     print("Must be 18 or older")



# ============================================================
# Task 5 — Even numbers with range()
# ============================================================
# Print all even numbers from 2 through 30.
#
# Required:
# Use range(start, stop, step).

# Write your code below:

# for num in range(2, 30, 2):
#     print(num)



# ============================================================
# Task 6 — Sum of multiples of 3
# ============================================================
# Calculate and print the sum of all multiples of 3
# from 3 through 99.
#
# Required:
# Use a for loop and an accumulator.
#
# Expected result:
# 1683

# Write your code below:
# total = 0
# for num in range(3, 100, 3):
#     total += num
# print(total)
    


# ============================================================
# Task 7 — Count number categories
# ============================================================
numbers = [4, -2, 0, 7, -5, 9, 0, -1, 8]

# Count how many values are:
#   positive
#   negative
#   zero
#
# Print all three counts.
# Do not manually count the values.

# Write your code below:

# positive_count = 0
# negative_count = 0
# zero_count = 0

# for num in numbers:
#     if num > 0:
#         positive_count += 1
#     elif num < 0:
#         negative_count += 1
#     else:
#         zero_count += 1

# print(f"Positive count: {positive_count}")
# print(f"Negative count: {negative_count}")
# print(f"Zero count: {zero_count}")




# ============================================================
# Task 8 — Count vowels
# ============================================================
# Ask the user to enter a word or short text.
# Count how many vowels it contains.
#
# Treat uppercase and lowercase equally.
# Vowels: a e i o u
#
# Example:
# Input: Artificial Intelligence
# Output: 10
#
# Hint:
# Iterate directly over the string.

# Write your code below:

text = input("Enter a word or text: ")

vowels_count = 0
vowels = ["a", "e", "i", "o", "u"]
for word in text:
    if word.lower() in vowels:
        vowels_count += 1
        continue

print(f"Vowels count: {vowels_count}")




# ============================================================
# Task 9 — Student results
# ============================================================
scores = [85, 42, 67, 91, 58, 73, 100, 39]

# Count:
#   passed students: score >= 60
#   failed students: score < 60
#
# Also print the average score.
#
# Required:
# Use a loop to calculate the total.
#
# Expected:
# Passed: 5
# Failed: 3
# Average: 69.38

# Write your code below:

passed_students_count = 0
failed_students_count = 0
total_score = 0

for score in scores:
    if score >= 60:
        passed_students_count += 1
    else:
        failed_students_count += 1
    total_score += score

Average = total_score / len(scores)

print(f"Passed: {passed_students_count}")
print(f"Failed: {failed_students_count}")
print(f"Average: {Average:.2f}")



# ============================================================
# Task 10 — Search and stop
# ============================================================
names = ["Anna", "Boris", "Sasha", "Maria", "Oleg", "Dina"]

# Ask the user for a name.
# Search the list using a for loop.
#
# If found:
#   print "Found"
#   stop immediately with break
#
# If not found:
#   print "Not found"
#
# Do not use:
#   if target in names
#
# Hint:
# A Boolean variable such as found = False can help.

# Write your code below:

found = False

your_name = input("Enter a name for search: ")
for name in names:
    if name == your_name:
        found = True
        print("Found")

if not found:
    print("Not found")


# ============================================================
# Task 11 — Skip invalid scores
# ============================================================
raw_scores = [78, -5, 91, 120, 66, 0, 88, 101, 54]

# Valid scores are from 0 to 100 inclusive.
#
# Use continue to skip invalid scores.
# For valid scores:
#   print each valid score
#   calculate the average of valid scores
#
# At the end print:
#   Valid scores: ...
#   Average: ...
#
# Required:
# Use continue.

# Write your code below:

valid_scores = []
total_sum = 0

for score in raw_scores:
    if score > 0 or score <= 100:
        continue
    print(f"Processing valid score: {score}")
    valid_scores += score
    total_sum += score

if len(valid_scores) > 0:
    Average = total_sum / len(valid_scores)
else:
    Average = 0

print(f"Valid scores: {valid_scores}")
print(f"Average: {Average:.2f}")


# ============================================================
# Task 12 — Dictionary iteration
# ============================================================
student_scores = {
    "Anna": 92,
    "Boris": 58,
    "Sasha": 76,
    "Maria": 49,
    "Oleg": 84,
}

# Iterate using .items().
#
# Print:
#   Anna: Pass
#   Boris: Fail
#   ...
#
# Score >= 60 means Pass.
# Then print how many students passed.

# Write your code below:

# num_student_passed = 0

# for name, score in student_scores.items():
#     if score >= 60:
#         print(f"{name}: Pass")
#         num_student_passed += 1
#     else:
#         print(f"{name}: Fail")

# print(f"Number of student passed: {num_student_passed}")



# ============================================================
# BONUS Task 13 — FizzBuzz
# ============================================================
# Print numbers 1 through 30.
#
# If divisible by both 3 and 5 -> FizzBuzz
# If divisible only by 3       -> Fizz
# If divisible only by 5       -> Buzz
# Otherwise print the number.
#
# Hint:
# Check the most specific condition first.

# Write your code below:

for num in range(1, 31):

    if num % 15 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)



# ============================================================
# BONUS Task 14 — Limited login attempts
# ============================================================
correct_pin = "4821"

# Give the user at most 3 attempts to enter the PIN.
#
# Use:
#   for
#   range()
#   break
#
# Correct PIN:
#   Access granted
#
# Three wrong attempts:
#   Access denied
#
# Do NOT use a while loop.

# Write your code below:

pin = input("Enter your pin:")

appended_pin = []
for pin_1 in correct_pin:
    appended_pin.append(appended_pin)
    if pin == appended_pin:
        print("Access granted")
        break
    else:
        print("Access denied")
        break



