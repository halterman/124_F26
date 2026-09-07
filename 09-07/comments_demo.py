# Author: Rick Halterman
# Revised September 7, 2026

# Get the input from the user
print("This program converts hours, minutes, and seconds to total seconds.")
hours = int(input("Please enter the hours: "))
minutes = int(input("Please enter the minutes: "))
seconds = int(input("Please enter the seconds: "))

# Compute the total number of seconds demonstrating simple arithmetic
total_seconds = hours * 3600 + minutes * 60 + seconds

# Report the result
print(f"The total number of seconds are {total_seconds}.")

x = int(input("Enter dividend: "))
y = int(input("Enter divisor: "))
if y != 0:
    print(f"{x}//{y} = {x // y}")
else:
    print("Cannot divide by zero")