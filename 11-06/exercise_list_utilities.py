from listutilities import my_sum, my_max    # type: ignore

def test_my_sum() -> None:
    """
    >>> my_sum([10, 20, 30, 40, 50])
    150
    >>> my_sum([])
    0
    >>> my_sum([2, 2])
    4
    """
    pass

def test_my_max() -> None:
    """
    >>> my_max([10, 20, 30, 40, 50])
    50
    >>> my_max([20])
    20
    >>> my_max([2, 1, 3, 0])
    3
    """
    pass
