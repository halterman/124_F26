def my_sum(lst: list[int]) -> int:
    s = 0
    for elem in lst:
        s += elem
    return s

def my_max(lst: list[int]) -> int | None:
    if len(lst) > 0:
        m = lst[0]
        for i in range(1, len(lst)):
            if lst[i] > m:
                m = lst[i]
        return m
    else:
        return None


if __name__ == '__main__':
    print(my_sum([10, 20, 30, 40]))
    print(my_sum([]))
    print(my_max([10, 20, 30, 40]))
    print(my_max([40, 20, 30, 10]))
    print(my_max([30, 20, 40, 10]))
    print(my_max([]))
    print('Test finished')