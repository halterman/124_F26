num = int(input("Please enter an integer in the range 1...10: "))

if num <= 10:
    if num > 0:
        print("Number is in range")
    else:
        print("Number is too small")
else:
    print("Number is too big")

