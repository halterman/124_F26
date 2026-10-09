"""
This module contains some custom math functions that
gives us experience writing functions in Python.
"""

from typing import Callable

Function = Callable[[float], float]


def abs(x: float) -> float:
    """ Returns the absolute value of x. """
    return x if x >= 0 else -x


def sqrt(x: float, tolerance: float) -> float:
    """ Returns the square root of the parameter x.
        tolerance controls the precision of the calculation. """
    r = 1.0
    while abs(r*r - x) > tolerance:
        r = (r + x/r)/2
    return r


def derivative(f: Function, x: float, h: float) -> float:
    return (f(x + h) - f(x))/h