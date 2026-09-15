num = int(input("Please enter an integer in the range 1...5: "))

if 1 <= num <= 5:
    if num == 1:
        print("one")
    else:
        if num == 2:
            print("two")
        else:
            if num == 3:
                print("three")
            else:
                if num == 4:
                    print("four")
                else:
                    print("five")
else:
    print("The number you provided is out of range")