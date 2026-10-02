def my_sqrt(x: float) -> float:
    """ Returns the square root of the parameter x.
        This is an example of how we can write our
        own function and not depend on the standard
        library. """
    r = 1.0
    diff = 1.0
    while diff > 0.00000001 or diff < -0.00000001:
        r = (r + x/r)/2
        diff = r*r - x
    return r