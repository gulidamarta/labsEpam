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


def get_longest_word(s: str) -> str:
    return max(s.split(' '), key=len)


def main():
    print(get_longest_word("Python is simple and effective!"))
    print(get_longest_word("Any phytonista like a namespace a lot."))


if __name__ == '__main__':
    main()
