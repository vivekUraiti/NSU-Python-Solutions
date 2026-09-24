"""
NSU Python — Lab 06
Functions as Values: lambda, Sorting, Filtering, and map

Complete Tasks 1–12.
Tasks 13–14 are optional bonus tasks.

Use only concepts covered in Lecture 06 and earlier lectures.
"""

# ============================================================
# Task 1 — Functions as values
# ============================================================
# Create a function:
#
#   square(number)
#
# that returns number ** 2.
#
# Then:
# 1. assign the function object to a new variable called operation;
# 2. call square(5);
# 3. call operation(5);
# 4. print whether operation is square.
#
# Expected final comparison:
# True
#
# Important:
# operation = square
# stores the function object.
#
# operation = square()
# would call the function immediately.

# Write your code below:

def square(number):
    return number ** 2

operation = square

print(square(5))
print(operation(5))
print(operation == square)


# ============================================================
# Task 2 — Passing a function as an argument
# ============================================================
# Create:
#
#   double(number)
#   triple(number)
#
# Then create:
#
#   apply(operation, value)
#
# apply() should call operation(value) and return the result.
#
# Examples:
# apply(double, 5) -> 10
# apply(triple, 5) -> 15
#
# Pass the function names WITHOUT parentheses.

# Write your code below:

def double(number):
    return number * 2

def triple(number):
    return number * 3

def apply(operation, value):
    return operation(value)

print(apply(double, 5))
print(apply(triple, 5))



# ============================================================
# Task 3 — Higher-order function
# ============================================================
# Create:
#
#   transform(values, operation)
#
# It should:
# - create an empty result list;
# - loop through values;
# - apply operation() to each value;
# - append each result;
# - return the new list.
#
# Then create:
#
#   square(number)
#
# Test:
# transform([1, 2, 3, 4], square)
#
# Expected:
# [1, 4, 9, 16]

# Write your code below:


def transform(values, operation):
    result = []
    for value in values:
        result.append(operation(value))
    return result
    
def square(number):
    return number * number


print(transform([1, 2, 3, 4], square))


# ============================================================
# Task 4 — Lambda expressions
# ============================================================
# Create these lambda functions:
#
#   double
#   add
#   is_even
#
# Requirements:
# double(5)    -> 10
# add(3, 4)    -> 7
# is_even(8)   -> True
# is_even(7)   -> False
#
# Each lambda must contain only one expression.

# Write your code below:

double = lambda x: x * 2
add = lambda x, y: x + y
is_even = lambda x: x % 2 == 0

print(double(5))
print(add(3, 4))
print(is_even(8))
print(is_even(7))


# ============================================================
# Task 5 — sorted() versus list.sort()
# ============================================================
# Start with:
#
# numbers = [8, 3, 10, 1, 6]
#
# Part A:
# Use sorted() to create a NEW list called ordered.
#
# Print:
# - numbers
# - ordered
#
# Confirm that numbers did not change.
#
# Part B:
# Call numbers.sort().
# Print numbers again.
#
# Expected sorted order:
# [1, 3, 6, 8, 10]
#
# Also store the result of numbers.sort() in a variable:
#
#   result = numbers.sort()
#
# Print result.
#
# What does list.sort() return?

# Write your code below:

numbers = [8, 3, 10, 1, 6]

ordered = sorted(numbers)
print(ordered)
print(numbers)

# B

numbers.sort()
print(numbers)

result = numbers.sort()
print(result) # None






# ============================================================
# Task 6 — Descending order
# ============================================================
# Start with:
#
# scores = [82, 95, 73, 88, 61]
#
# Use sorted() with reverse=True.
#
# Store the result in:
#
#   high_to_low
#
# Expected:
# [95, 88, 82, 73, 61]
#
# The original scores list should remain unchanged.

# Write your code below:
scores = [82, 95, 73, 88, 61]

high_to_low = sorted(scores, reverse=True)
print(high_to_low)


# ============================================================
# Task 7 — Sorting with key
# ============================================================
# Start with:
#
words = ["pear", "watermelon", "fig", "banana", "kiwi"]
#
# Create:
#
#   shortest_first
#   longest_first
#
# shortest_first:
# sort by string length from shortest to longest.
#
# longest_first:
# sort by string length from longest to shortest.
#
# Use key=len for at least one of the two results.
#
# Do not manually calculate the lengths.

# Write your code below:

shortest_first = sorted(words, key=len)
print(shortest_first)

longest_first = sorted(words, key=len, reverse=True)
print(longest_first)






# ============================================================
# Task 8 — Case-insensitive sorting
# ============================================================
# Start with:
#

cities = [
    "berlin",
    "Algiers",
    "cairo",
    "Amsterdam",
    "zurich"
]

#
# Sort the list alphabetically without treating uppercase
# and lowercase letters as separate groups.
#
# Use:
#
#   key=str.lower
#
# Store the result in:
#
#   ordered_cities
#
# The original capitalization must stay unchanged.

# Write your code below:

ordered_cities = sorted(cities, key=str.lower)
print(ordered_cities)


# ============================================================
# Task 9 — Sorting tuples with lambda
# ============================================================
# Start with:
#
students = [
    ("Anna", 82),
    ("Boris", 95),
    ("Mira", 88),
    ("Daniel", 73)
]
#
# Sort students by score from highest to lowest.
#
# Use:
#
#   sorted()
#   key=lambda ...
#   reverse=True
#
# Expected first item:
# ("Boris", 95)

# Write your code below:

score_high_to_low = sorted(students, key=lambda x: x[1], reverse=True)
print(score_high_to_low)

# ============================================================
# Task 10 — Filtering values
# ============================================================
# Start with:
#
scores = [45, 70, 82, 39, 91, 60, 58]
#
# Use filter() and a lambda to keep only scores >= 60.
#
# Convert the filter result to a list.
#
# Expected:
# [70, 82, 91, 60]

# Write your code below:

passing_scores = list(filter(
    lambda x: x >= 60,
    scores
))

print(passing_scores)



# ============================================================
# Task 11 — Transforming values with map()
# ============================================================
#  Start with:
#
prices = [100, 250, 80, 40]
#
# Use map() and a lambda to increase every price by 10%.
#
# Convert the result to a list.
#
# Expected:
# [110.0, 275.0, 88.0, 44.0]
#
# Note:
# Floating-point output may sometimes contain small
# representation differences.

# Write your code below:

increases_price = map(lambda x: round(x * 1.10, 2), prices)
result = list(increases_price)
print(result)
#


# ============================================================
# Task 12 — Filter, sort, and map together
# ============================================================
# Start with:
#
students = [
    {"name": "Anna", "score": 82},
    {"name": "Boris", "score": 55},
    {"name": "Mira", "score": 91},
    {"name": "Daniel", "score": 67},
    {"name": "Sara", "score": 48}
]

# Step 1:
# Use filter() to keep students with score >= 60.
#
# Step 2:
# Use sorted() to order the passing students from
# highest score to lowest score.
#
# Step 3:
# Use map() to create a list containing only their names.
#
# Expected names:
# ["Mira", "Anna", "Daniel"]
#
# Use lambda expressions for the filter, sorting key,
# and map transformation.

# Write your code below:

passing_students = list(filter(
    lambda x: x["score"] >= 60, students
))
passing_students = sorted(
    passing_students,
    key=lambda x: x["score"],
    reverse=True
)
passing_scores = list(map(
    lambda x: x["name"], passing_students
))

print(passing_scores)


# ============================================================
# Task 13 — BONUS: Sort records by multiple ideas
# ============================================================
# Start with:
#
products = [
    {"name": "Keyboard", "price": 70},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 220},
    {"name": "USB Cable", "price": 10}
]
#
# Create:
#
#   by_price
#   by_name_length
#
# by_price:
# sort from cheapest to most expensive.
#
# by_name_length:
# sort by the length of the product name,
# from shortest to longest.
#
# Use lambda expressions as sorting keys.

# Write your code below:

by_price = sorted(products, key=lambda x: x["price"], reverse=True)
print(by_price)

by_name_length = sorted(products, key=lambda x: x['name'])
print(by_name_length)

# ============================================================
# Task 14 — BONUS: Student ranking pipeline
# ============================================================
# Start with:
#
students = [
    ("Anna", 82),
    ("Boris", 55),
    ("Mira", 91),
    ("Daniel", 67),
    ("Sara", 48),
    ("Omar", 76)
]
#
# Build this pipeline:
#
# 1. filter() -> keep scores >= 60
# 2. sorted() -> highest score first
# 3. map() -> convert each tuple to a string:
#
#       "Name: score"
#
# Expected:
# [
#     "Mira: 91",
#     "Anna: 82",
#     "Omar: 76",
#     "Daniel: 67"
# ]
#
# Store the final result in:
#
#   ranking
#
# Print ranking.

# Write your code below:

ranking = list(filter(
    lambda x: x[1] >= 60,
    students,
))

ranking = sorted(ranking, key=lambda x: x[1], reverse=True)

ranking = list(map(lambda x: f" {x[0]}: {x[1]}", ranking))
print(ranking)



# ============================================================
# Task 15 — Sort numbers by distance from zero
# ============================================================
# Start with:
#
numbers = [-10, 3, -2, 8, -7, 1]
#
# Sort the numbers by their absolute value.
#
# Use:
#   sorted()
#   key=abs
#
# Expected:
# [1, -2, 3, -7, 8, -10]
#
# Do not change the original list.

# Write your code below:

sorted_num = sorted(numbers, key=abs)
print(sorted_num)


# ============================================================
# Task 16 — Sort words alphabetically by last letter
# ============================================================
# Start with:
#
words = ["apple", "banana", "kiwi", "orange", "pear"]
#
# Sort the words according to their LAST character.
#
# Use:
#
#   sorted()
#   key=lambda ...
#
# Hint:
# word[-1]
#
# Store the result in:
#
#   ordered_words

# Write your code below:

ordered_words = sorted(words, key=lambda x: x[-1])
print(ordered_words)



# ============================================================
# Task 17 — Filter negative numbers
# ============================================================
# Start with:
#
numbers = [5, -3, 8, -1, 0, 12, -7, 4]
#
# Use filter() and a lambda to keep only negative numbers.
#
# Convert the result to a list.
#
# Expected:
# [-3, -1, -7]

# Write your code below:

result = list(filter(lambda x: x < 0, numbers))
print(result)


# ============================================================
# Task 18 — Filter words by length
# ============================================================
# Start with:
#
words = [
    "cat",
    "python",
    "AI",
    "computer",
    "data",
    "algorithm"
]
#
# Use filter() to keep only words with at least 5 characters.
#
# Use a lambda.
#
# Expected:
# ["python", "computer", "algorithm"]

# Write your code below:

result = list(filter(lambda x: len(x) >= 5, words))
print(result)



# ============================================================
# Task 19 — Convert temperatures with map()
# ============================================================
# Start with:
#
celsius = [0, 10, 20, 30, 40]
#
# Convert every temperature from Celsius to Fahrenheit.
#
# Formula:
#
# Fahrenheit = Celsius * 9 / 5 + 32
#
# Use:
#
#   map()
#   lambda
#
# Expected:
# [32.0, 50.0, 68.0, 86.0, 104.0]

# Write your code below:

fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius))
print(fahrenheit)


# ============================================================
# Task 20 — Extract dictionary values with map()
# ============================================================
# Start with:
#
students = [
    {"name": "Anna", "age": 22},
    {"name": "Boris", "age": 24},
    {"name": "Mira", "age": 21},
    {"name": "Daniel", "age": 25}
]
#
# Use map() and a lambda to create a list containing
# only the student names.
#
# Expected:
# ["Anna", "Boris", "Mira", "Daniel"]

# Write your code below:

student = list(map(lambda x: x["name"], students))
print(student)

# ============================================================
# Task 21 — Sort students alphabetically
# ============================================================
# Start with:
#
students = [
    ("Mira", 91),
    ("anna", 82),
    ("Daniel", 67),
    ("boris", 55)
]
#
# Sort the students alphabetically by name.
#
# Ignore uppercase/lowercase differences.
#
# Use:
#
#   sorted()
#   key=lambda ...
#
# Hint:
# student[0].lower()
#
# Expected order:
# anna
# boris
# Daniel
# Mira

# Write your code below:

student = sorted(students, key=lambda x: x[0].lower())
print(student)


# ============================================================
# Task 22 — Sort by multiple values
# ============================================================
# Start with:
#
students = [
    ("Anna", 80),
    ("Boris", 90),
    ("Mira", 80),
    ("Daniel", 90),
    ("Sara", 70)
]
#
# Sort students:
#
# 1. by score from highest to lowest;
# 2. if two students have the same score,
#    sort them alphabetically by name.
#
# Expected:
#
# [
#     ("Boris", 90),
#     ("Daniel", 90),
#     ("Anna", 80),
#     ("Mira", 80),
#     ("Sara", 70)
# ]
#
# Use sorted() and a lambda.
#
# Hint:
# A tuple can be used as a sorting key:
#
#   key=lambda student: (...)
#
# Think about how to make the score sort in descending
# order without using reverse=True for the name.

# Write your code below:

student = sorted(students, key=lambda x: (-x[1], x[0]))
print(student)


# ============================================================
# Task 23 — Filter and transform numbers
# ============================================================
# Start with:
#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# Step 1:
# Use filter() to keep only even numbers.
#
# Step 2:
# Use map() to square the remaining numbers.
#
# Expected:
# [4, 16, 36, 64, 100]
#
# Use lambda expressions.

# Write your code below:

number = list(filter(lambda x: x % 2 == 0, numbers))

square = list(map(lambda x: x ** 2, number))

print(square)



# ============================================================
# Task 24 — Product discount system
# ============================================================
# Start with:
#
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 80},
    {"name": "Monitor", "price": 300},
    {"name": "USB Cable", "price": 10}
]
#
# Step 1:
# Keep only products costing at least 50.
#
# Step 2:
# Apply a 20% discount to their prices.
#
# Step 3:
# Sort the discounted products from cheapest
# to most expensive.
#
# The result should contain dictionaries like:
#
# {
#     "name": "Keyboard",
#     "price": 64.0
# }
#
# Use:
#
#   filter()
#   map()
#   sorted()
#   lambda
#
# Do not modify the original products list.

# Write your code below:

product = list(filter(lambda x: x["price"] >= 50, products))

discount = list(map(lambda x: {"name": x["name"], "price": x["price"] * 0.80}, product))

sorted = sorted(discount, key=lambda x: x["price"])

print(sorted)


