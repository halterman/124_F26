# Get number from the user
value = int(input('Please enter an integer value in the range 0...31: '))
# Initial binary string is empty
binary_string = ''
# Integer must be less than 32
if 0 <= value < 32:
    binary_string += str(value//16)
    value %= 16
    binary_string += str(value//8)
    value %= 8
    binary_string += str(value//4)
    value %= 4
    binary_string += str(value//2)
    value %= 2
    binary_string += str(value)
# Report results
if binary_string != '':
    print(binary_string)
else:
    print('Unable to convert')
