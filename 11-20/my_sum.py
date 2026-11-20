def sum(*nums: int) -> int:
    s = 0
    for num in nums:
        s += num
    return s


print('1: ', sum())
print('2: ', sum(2))
print('3: ', sum(2, 5))
print('4: ', sum(7, 2, 5))
print('5: ', sum(7, 2, 5, 10))
print('6: ', sum(7, 2, 5, 10, 3, 4, 1, 6, 7, 8, 10, 5))
print('7: ', sum(*(7, 2, 5)))