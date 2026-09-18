print('Please enter nonnegative integers (negative ends the list)')

num = 0
largest = -1

while num >= 0:
    num = int(input('Enter number (negative ends): '))
    if num > largest:
        largest = num

if largest >= 0:
    print(f'largest is {largest}')
else:
    print('No nonnegative numbers provided')