"""
Implement a function get_digits(num: int)->Tuple[int] which returns a tuple of
a given integer's digits. Example:

>>> get_digits(87112357890)
(8, 7, 1, 1, 2, 3, 5, 7, 8, 9, 0)
"""
from typing import Tuple, List


def get_digits(num: int) -> Tuple[int]:
    str_digits: str = str(num)
    list_digits: str = str_digits.strip()
    int_list: List[int] = [int(i) for i in list_digits]
    return tuple(int_list)


def main():
    print(get_digits(87112357890))


if __name__ == '__main__':
    main()