from math import sqrt

for i in range(0, 21):
    r = 1.0

    diff = 1.0
    while diff > 0.00000001 or diff < -0.00000001:
        r = (r + i/r)/2
        diff = r*r - i

    print(f'{i:2}  {r:12.10f}  {sqrt(i):12.10f}')
