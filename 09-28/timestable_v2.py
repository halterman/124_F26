size = int(input("Enter maximum number: "))

for row in range(1, size + 1):
    for column in range(1, size + 1):
        print(f"{row * column:4}", end="")
    print()