print("This program converts hours, minutes, and seconds to total seconds.")
hours = int(input("Please enter the hours: "))
minutes = int(input("Please enter the minutes: "))
seconds = int(input("Please enter the seconds: "))

total_seconds = hours * 3600 + minutes * 60 + seconds
print(f"The total number of seconds are {total_seconds}.")