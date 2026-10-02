size = int(input("Enter maximum number: "))

print("      ", end="")
# Print the column labels
for column in range(1, size + 1):
    print(f"{column:4}", end="")
print()

# Print the line
print("     +", end="")
for column in range(1, size + 1):
    print(f"----", end="")
print()

for row in range(1, size + 1):
    # Print the label for the row
    print(f"{row:4} |", end="")
    # Print the row
    for column in range(1, size + 1):
        print(f"{row * column:4}", end="")
    print()  # Go down to the next row