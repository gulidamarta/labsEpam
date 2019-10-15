"""
Implement a function get_shortest_word(s: str)->str which returns the longest word in the
given string. The word can contain any symbols except whitespaces(' ', '\n', '\t' and so on).
If there are multiple longest words in the string with a same length return the word that
occurs first. Example:

>>> get_longest_word("Python is simple and effective!")
'effective!'
>>> get_longest_word("Any phytonista like a namespace a lot.")
'phytonista'
"""
from typing import List


def get_longest_word(s: str) -> str:
    sorted_string: List[str] = sorted(s.split(), key=len)
    max_string: str = sorted_string[0]
    max_len: int = len(sorted_string[0])

    for i in range(1, len(sorted_string)):
        if len(sorted_string[i]) > max_len:
            max_len = len(sorted_string[i])
            max_string = sorted_string[i]
    return max_string


def main():
    print(get_longest_word("Python is simple and effective!"))
    print(get_longest_word("Any phytonista like a namespace a lot."))


if __name__ == '__main__':
    main()
