"""
Implement a function split_by_indexes(s: str, indexes: List[int]) -> List[str] which splits
the s string by indexes specified in indexes. Wrong indexes must be ignored. Example:

>>> split_by_indexes("pythoniscool,isn'tit", [8, 6, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it"]
>>> split_by_indexes("no luck", [42])
["no luck"]
"""
from typing import List


def split_by_indexes(s: str, indexes: List[int]) -> List[str]:
    # it is useful for algorithm if the numbers will be in ascending order
    indexes.sort()
    print(indexes)
    result_list: List[str] = []
    start_index: int = 0
    i: int = 0
    if len(indexes) == 0:
        result_list.append(s)
    while i < len(indexes):
        # checking if it the last element in the indexes array and it
        # id in the right range. Append list, if everything is correct
        if (i == len(indexes) - 1) & (indexes[i] < len(s)):
            last_index = indexes[i]
            result_list.append(s[start_index:last_index])
            start_index = last_index
            last_index = len(s)
            result_list.append(s[start_index:last_index])
            break
        # If that element of the array is higher than length of the source string
        # output string from current start position to the end
        if indexes[i] >= len(s):
            result_list.append(s[start_index:len(s)])
            break
        if indexes[i] < len(s):
            last_index = indexes[i]
            result_list.append(s[start_index:last_index])
            start_index = last_index
        i += 1
    return result_list


def main():
    print(split_by_indexes("pythoniscool,isn'tit", [8, 6, 12, 13, 18]))
    print(split_by_indexes("no luck", [42]))


if __name__ == '__main__':
    main()
