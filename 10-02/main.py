from math import sqrt
from my_math import my_sqrt

print('New version of square root')
for i in range(0, 21):
    print(f'{i:2}  {my_sqrt(i):12.10f}  {sqrt(i):12.10f}')