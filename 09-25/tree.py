height = int(input('Please enter tree height: '))

# #1
# for i in range(height):
#     print('*')

# #2
# row = 0
# for i in range(height):
#     # Print the correct number of spaces first
#     print('*' * (row + 1))
#     row += 1

#3
row = 0
for i in range(height):
    print(' ' * (height - 1), '*' + '*' * (2*row))
    row += 1
    height -= 1
