import math
import my_math

print('Newest version of square root')
for i in range(0, 21):
    print(f'{i:2}  {my_math.sqrt(i, 0.0000001):12.10f}  {math.sqrt(i):12.10f}')


def func1(x: float) -> float:
    return 3*x + 1

def func2(x: float) -> float:
    return x**2

def func3(x: float) -> float:
    return math.cos(x)

print(round(my_math.derivative(func1, 10.0, 0.0000001), 5))
print(round(my_math.derivative(func2, 10.0, 0.0000001), 5))
print(round(my_math.derivative(func3, math.pi/2, 0.0000001), 5))