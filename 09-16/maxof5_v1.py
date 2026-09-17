# Get the user's input
print('Please enter five integers')
num1 = int(input('#1 ==> '))
num2 = int(input('#2 ==> '))
num3 = int(input('#3 ==> '))
num4 = int(input('#4 ==> '))
num5 = int(input('#5 ==> '))

# Determine the largest number entered
if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
    largest = num1
elif num2 >= num1 and num2 >= num1 and num2 >= num4 and num2 >= num5:
    largest = num2
elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
    largest = num3
elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
    largest = num4
else:
    largest = num5

print(f'The largest is {largest}')


