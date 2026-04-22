"""
==============================================
Session 2 Homework: Lists, Dictionaries, 
Functions & File Handling
Modern Data Engineering Course
Total Points: 100
==============================================

Instructions:
- Complete each task below
- Replace the ??? with your code
- Run the file to check your answers
- Submit your completed .py file
==============================================
"""

# ============================================
# TASK 1: Lists (15 points)
# ============================================

# 1a. Create a list of 5 Bangladeshi cities (5 pts)
cities = ???

# 1b. Add "Rajshahi" to the end of the list (3 pts)
???

# 1c. Remove the second city from the list (3 pts)
???

# 1d. Print the list sorted alphabetically (4 pts)
???


# ============================================
# TASK 2: List Comprehension (10 points)
# ============================================

prices_bdt = [1200, 450, 3200, 890, 5600, 150]

# 2a. Create a new list with only prices above 1000 (5 pts)
expensive = ???
print(f"Expensive items: {expensive}")

# 2b. Create a new list where each price has 15% VAT added (5 pts)
with_vat = ???
print(f"With VAT: {with_vat}")


# ============================================
# TASK 3: Tuples & Sets (10 points)
# ============================================

# 3a. Create a tuple of your (name, age, city) and unpack it (5 pts)
info = ???
name, age, city = info
print(f"{name}, {age}, from {city}")

# 3b. Remove duplicates from this list using a set (5 pts)
raw_ids = [101, 203, 101, 305, 203, 407, 305, 101]
unique_ids = ???
print(f"Unique IDs: {unique_ids}")


# ============================================
# TASK 4: Dictionaries (15 points)
# ============================================

# 4a. Create a dictionary for a student with
#     name, department, cgpa, and semester (5 pts)
student = ???

# 4b. Add a new key "university" with any value (3 pts)
???

# 4c. Print all keys and values using a loop (4 pts)
for ???:
    print(f"{key}: {value}")

# 4d. Use .get() to print "email" with a default "not provided" (3 pts)
email = ???
print(f"Email: {email}")


# ============================================
# TASK 5: Functions (20 points)
# ============================================

# 5a. Write a function that takes a list of numbers
#     and returns the average (8 pts)
def calculate_average(numbers):
    ???

print(calculate_average([80, 92, 75, 88, 95]))  # should print 86.0

# 5b. Write a function that takes a score and returns
#     a grade: A (90+), B (80+), C (70+), D (60+), F (below 60)
#     Give it a default parameter (7 pts)
def get_grade(score):
    ???

print(get_grade(92))   # A
print(get_grade(75))   # C
print(get_grade(45))   # F

# 5c. Write a function that takes a list of scores
#     and returns both the count and average (uses tuple) (5 pts)
def summarize(scores):
    ???

count, avg = summarize([85, 90, 78, 92])
print(f"Count: {count}, Average: {avg}")


# ============================================
# TASK 6: File Handling (30 points)
# ============================================

import csv, json

# Here is your data:
students = [
    {"name": "Rahim", "dept": "CSE", "cgpa": 3.65},
    {"name": "Fatima", "dept": "EEE", "cgpa": 3.82},
    {"name": "Karim", "dept": "CSE", "cgpa": 3.21},
    {"name": "Nadia", "dept": "BBA", "cgpa": 3.90},
    {"name": "Arif", "dept": "EEE", "cgpa": 2.95},
]

# 6a. Write this data to "students.csv" (8 pts)
???

# 6b. Read "students.csv" back and print each student (7 pts)
???

# 6c. Using your functions from Task 5, calculate
#     the average CGPA and save a summary to "summary.json"
#     The JSON should contain:
#     - total_students
#     - average_cgpa (rounded to 2 decimal places)
#     - highest_cgpa
#     - lowest_cgpa (15 pts)

???

# Verify by reading and printing the JSON
with open("summary.json") as f:
    result = json.load(f)
    print(result)


print("\nHomework complete! 🎉")
