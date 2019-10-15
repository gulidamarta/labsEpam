"""
Implement a function foo(List[int])->List[int] which, given a list of integers, return a new
list such that each element at index i of the new list is the product of all numbers in the
original array except the one at i. Example:

>>> foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24)
>>> foo([3, 2, 1])
[2, 3, 6]
"""
from typing import List


def foo(array: List[int]) -> List[int]:
    if len(array) == 1:
        return array
    # it is necessary to initialize temp arrays and result array
    # to have access to their elements and to set them
    left_array = [0] * len(array)
    right_array = [0] * len(array)
    product_array = [0] * len(array)
    left_array[0] = 1
    right_array[-1] = 1

    # construct the left array
    for i in range(1, len(array)):
        left_array[i] = array[i - 1] * left_array[i - 1]

    # construct the right array
    for i in range(len(array) - 2, -1, -1):
        right_array[i] = array[i + 1] * right_array[i + 1]

    # construct product array
    for i in range(len(array)):
        product_array[i] = left_array[i] * right_array[i]
    return product_array


def print_result(array: List[int]):
    print("Source array : {0}".format(array))
    print("Result array after multiplying: {0}".format(foo(array)))


def main():
    print_result([1, 2, 3, 4, 5])
    print_result([3, 2, 1])


if __name__ == '__main__':
    main()
