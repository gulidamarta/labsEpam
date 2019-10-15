"""
Implement a function which works the same as str.split method (without str.split itself, of course)
"""
from typing import List


def split_string(string: str, separator: str) -> List[str]:
    result_list: List[str] = []
    i: int = 0
    temp_str: str = ''
    while i < len(string):
        if string[i] == separator:
            result_list.append(temp_str)
            temp_str = ''
        else:
            temp_str += string[i]
        if i == len(string) - 1:
            result_list.append(temp_str)
        i += 1
    return result_list


def main():
    result: List[str] = split_string("doing a lab work", " ")
    print(result)
    result = split_string("apple#banana#cherry#orange##", "#")
    print(result)
    result = split_string("apple####banana#cherry#orange", "#")
    print(result)


if __name__ == '__main__':
    main()