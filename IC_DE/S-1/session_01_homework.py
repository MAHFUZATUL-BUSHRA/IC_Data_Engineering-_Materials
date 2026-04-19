"""
==============================================
Session 1 Homework: Python Basics
Modern Data Engineering Course
==============================================

Instructions:
- Complete each task below
- Replace the ??? with your code
- Run the file to check your answers
- Bonus tasks are optional but encouraged!

Topics covered:
  Variables, Data Types, Operators, Strings,
  Booleans, Type Conversion, Input/Output,
  Conditionals, Loops
==============================================
"""


# ============================================
# TASK 1: Variables & Data Types
# ============================================
# Create variables for a data pipeline run

pipeline_name = ???        # string: name it "user_sync_pipeline"
source_system = ???        # string: "crm_database"
total_records = ???        # integer: 25000
error_count = ???          # integer: 178
processing_time = ???      # float: 45.7 (seconds)
is_successful = ???        # boolean: True

# Print each variable and its type
# Example: print(f"{pipeline_name} -> {type(pipeline_name)}")

print(f"{pipeline_name} -> {type(pipeline_name)}")
# Do the same for the rest...



# ============================================
# TASK 2: Arithmetic Operations
# ============================================
# Using the variables from Task 1, calculate:

success_count = ???          # total_records minus error_count
success_rate = ???           # success_count divided by total_records, times 100
error_rate = ???             # error_count divided by total_records, times 100
records_per_second = ???     # total_records divided by processing_time

print(f"Success count: {success_count}")
print(f"Success rate: {success_rate:.2f}%")
print(f"Error rate: {error_rate:.2f}%")
print(f"Records/sec: {records_per_second:.1f}")



# ============================================
# TASK 3: String Operations
# ============================================
# Given this messy data from a CSV file:

raw_name = "   rahim UDDIN   "
raw_email = "RAHIM@GMAIL.COM"
raw_city = "dhaka"

# Clean them up:
clean_name = ???       # strip whitespace, then title case -> "Rahim Uddin"
clean_email = ???      # lowercase -> "rahim@gmail.com"
clean_city = ???       # capitalize -> "Dhaka"

print(f"Name: {clean_name}")
print(f"Email: {clean_email}")
print(f"City: {clean_city}")

# Build a formatted summary string using f-string
summary = ???   # "Rahim Uddin (rahim@gmail.com) from Dhaka"
print(summary)



# ============================================
# TASK 4: Type Conversion
# ============================================
# This data came from a CSV file — everything is a string!

str_price = "1250.75"
str_quantity = "8"
str_discount = "15"
str_in_stock = "True"

# Convert to proper types and calculate
price = ???          # convert to float
quantity = ???       # convert to int
discount = ???       # convert to int

subtotal = ???               # price * quantity
discount_amount = ???        # subtotal * discount / 100
final_total = ???            # subtotal - discount_amount

print(f"Subtotal: {subtotal:.2f} BDT")
print(f"Discount ({discount}%): -{discount_amount:.2f} BDT")
print(f"Final Total: {final_total:.2f} BDT")



# ============================================
# TASK 5: Comparisons & Booleans
# ============================================
# A data pipeline has these metrics:

rows_loaded = 9500
rows_expected = 10000
null_percentage = 3.2
max_allowed_nulls = 5.0
run_time_minutes = 12
max_run_time = 15

# Write boolean expressions:
data_complete = ???        # is rows_loaded >= rows_expected?
data_clean = ???           # is null_percentage <= max_allowed_nulls?
within_time = ???          # is run_time_minutes <= max_run_time?
all_checks_passed = ???    # are ALL three True? (use 'and')
any_issue = ???            # did ANY check fail? (hint: not all_checks_passed)

print(f"Data complete: {data_complete}")
print(f"Data clean: {data_clean}")
print(f"Within time: {within_time}")
print(f"All passed: {all_checks_passed}")
print(f"Any issue: {any_issue}")



# ============================================
# TASK 6: Conditionals (if/elif/else)
# ============================================
# Write a grading system for pipeline health

pipeline_score = 87   # try changing this to test all branches

# Rules:
#   90-100 -> "EXCELLENT" (green)
#   70-89  -> "GOOD" (yellow)
#   50-69  -> "WARNING" (orange)
#   below 50 -> "CRITICAL" (red)

if ???:
    grade = "EXCELLENT"
    color = "green"
elif ???:
    grade = "GOOD"
    color = "yellow"
elif ???:
    grade = "WARNING"
    color = "orange"
else:
    grade = "CRITICAL"
    color = "red"

print(f"Pipeline Score: {pipeline_score} -> {grade} ({color})")



# ============================================
# TASK 7: For Loops
# ============================================
# Given a list of database tables and their row counts:

tables = ["customers", "orders", "products", "reviews", "inventory"]
row_counts = [15000, 42000, 3500, 28000, 7200]

# Task 7a: Print each table name in UPPERCASE
for table in tables:
    print(???)

print("---")

# Task 7b: Print each table with its row count
# Hint: use range(len(tables)) or zip(tables, row_counts)
for i in range(len(tables)):
    print(f"Table: {???} -> {???} rows")

print("---")

# Task 7c: Find the total number of rows across all tables
total = 0
for count in row_counts:
    ???              # add count to total

print(f"Total rows across all tables: {total}")



# ============================================
# TASK 8: While Loop
# ============================================
# Simulate a data sync that processes 1000 records per batch

remaining = 7500
batch_size = 1000
batch_number = 0

while ???:           # keep going while remaining > 0
    batch_number += 1
    if remaining >= batch_size:
        processed = batch_size
    else:
        processed = remaining
    remaining = ???  # subtract processed from remaining
    print(f"Batch {batch_number}: processed {processed}, remaining: {remaining}")

print(f"Done! Processed in {batch_number} batches")



# ============================================
# TASK 9: Putting It All Together
# ============================================
# Build a complete pipeline status report

# --- Your pipeline data ---
pipeline = "ecommerce_daily_sync"
tables_processed = ["users", "orders", "products", "payments"]
total_rows = 95400
failed_rows = 1230
start_time_seconds = 0
end_time_seconds = 324

# --- Calculate metrics ---
success_rows = ???
success_rate = ???       # as percentage
duration_minutes = ???   # convert seconds to minutes
rows_per_second = ???

# --- Determine status ---
if success_rate >= 98:
    status = "HEALTHY"
elif success_rate >= 95:
    status = "WARNING"
else:
    status = "CRITICAL"

# --- Print the report ---
print("=" * 50)
print(f"  PIPELINE REPORT: {pipeline}")
print("=" * 50)
print(f"  Status: {status}")
print(f"  Duration: {???:.1f} minutes")
print(f"  Tables processed:")
for table in tables_processed:
    print(f"    - {table}")
print(f"  Total rows: {total_rows:,}")
print(f"  Successful: {success_rows:,} ({success_rate:.1f}%)")
print(f"  Failed: {failed_rows:,}")
print(f"  Throughput: {???:.0f} rows/sec")
print("=" * 50)


# ============================================
# BONUS: User Input Version
# ============================================
# Uncomment and complete this section to make
# an interactive version that asks for input!

# pipeline = input("Pipeline name: ")
# total = int(input("Total rows: "))
# failed = int(input("Failed rows: "))
# time_sec = float(input("Run time (seconds): "))
#
# ... calculate and print report ...


print("\nHomework complete! Great job! 🎉")
