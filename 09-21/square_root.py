i = float(input('Please enter a number: '))
r = 1.0

# while r*r - i > 0.00000001 or r*r - i < -0.00000001:
#     r = (r + i/r)/2

diff = 1.0
while diff > 0.00000001 or diff < -0.00000001:
    r = (r + i/r)/2
    diff = r*r - i

print(f'The square root of {i} is {r}')
