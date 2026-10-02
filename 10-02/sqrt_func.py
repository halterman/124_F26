from math import sqrt

def my_sqrt(x: float) -> float:
    """ Returns the square root of the parameter x. """
    r = 1.0
    diff = 1.0
    while diff > 0.00000001 or diff < -0.00000001:
        r = (r + x/r)/2
        diff = r*r - x
    return r

print('New version of square root')
for i in range(0, 21):
    print(f'{i:2}  {my_sqrt(i):12.10f}  {sqrt(i):12.10f}')
