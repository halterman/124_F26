# Get the user's input
print('Please enter five integers')
num1 = int(input('#1 ==> '))
num2 = int(input('#2 ==> '))
num3 = int(input('#3 ==> '))
num4 = int(input('#4 ==> '))
num5 = int(input('#5 ==> '))

# Determine the largest number entered
largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
if num4 > largest:
    largest = num4
if num5 > largest:
    largest = num5
    
print(f'The largest is {largest}')


