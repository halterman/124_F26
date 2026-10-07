import math
import my_math

print('Newest version of square root')
for i in range(0, 21):
    print(f'{i:2}  {my_math.sqrt(i, 0.0000001):12.10f}  {math.sqrt(i):12.10f}')