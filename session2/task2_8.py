"""
Implement a function get_pairs(lst: List[int)->List[Tuple] which returns a list of tuples
containing pairs of elements. Pairs should be performed as in the example. If there is
only one element in this list return None instead. Example:

>>> get_pairs([1, 2, 3, 8, 9])
[(1, 2), (2, 3), (3, 8), (8, 9)]
>>> get_pairs([2])
None
>>> get_pairs(['need', 'to', 'sleep', 'more'])
[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
"""
from typing import List, Union, Tuple


def get_pairs(lst: Union[List[int], List[str]]) -> Union[List[Tuple], None]:
    if len(lst) == 1:
        return None
    list_end = list()
    for i in range(len(lst) - 1):
        list_end.append((lst[i], lst[i + 1]))
    return list_end


def main():
    print(get_pairs([1, 2, 3, 8, 9]))
    print(get_pairs([2]))
    print(get_pairs(['need', 'to', 'sleep', 'more']))


if __name__ == '__main__':
    main()