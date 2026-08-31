total_seconds = int(input("Please enter the number of seconds: "))

hours = total_seconds // 3600
total_seconds = total_seconds % 3600

minutes = total_seconds // 60
seconds = total_seconds % 60

print(f"{hours} hrs {minutes} min {seconds} sec")