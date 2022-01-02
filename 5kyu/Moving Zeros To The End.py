"""
https://www.codewars.com/kata/52597aa56021e91c93000cb0

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""
from time import time


def move_zeros(array):
    result, zero_count = [], 0
    for number in array:
        if number == 0:
            zero_count += 1
        else:
            result.append(number)
    return result + ([0] * zero_count)


def move_zeros_one(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))


def move_zeros_two(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)


start = time()
for _ in range(1000000):
    move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
    move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])
print(time() - start)


start = time()
for _ in range(1000000):
    move_zeros_one([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
    move_zeros_one([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])
print(time() - start)


start = time()
for _ in range(1000000):
    move_zeros_two([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
    move_zeros_two([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])
print(time() - start)
