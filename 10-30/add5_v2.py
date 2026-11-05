sum = 0.0
NUMBER_OF_ENTRIES = 5
print(f'Please enter {NUMBER_OF_ENTRIES} numbers:')
for i in range(1, NUMBER_OF_ENTRIES + 1):
    num = float(input(f'Enter number {i}: '))
    sum += num 
print('Average:', sum/NUMBER_OF_ENTRIES)