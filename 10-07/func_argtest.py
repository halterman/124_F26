from typing import Callable


def add(x: int, y: int) -> int:
    return x + y


def multiply(x: int, y: int) -> int:
    return x * y

def evaluate(f: Callable[[int, int], int], x: int, y: int):
    return f(x, y)


num1 = int(input('Please enter the first number: '))
num2 = int(input('Please enter the second number: '))

answer = add(num1, num2)
print(f'{num1} + {num2} = {answer}')
print(f'{num1} * {num2} = {multiply(num1, num2)}')

answer = evaluate(multiply, num1, num2)
print(f'The answer is {answer}')
