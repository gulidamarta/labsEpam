"""
Write a function that check whether a string is a palindrome or not. Usage of any reversing
functions is prohibited.
"""


def is_palindrome(source_string: str):
    source_string = source_string.replace(' ', '')
    source_string = source_string.replace('\'', '')
    source_string = source_string.replace('–', '')
    source_string = source_string.replace(',', '')
    source_string = source_string.lower()

    i: int = 0
    j: int = len(source_string) - 1
    while (i <= (len(source_string) // 2)) & (j >= (len(source_string) // 2)):
        if source_string[i] != source_string[j]:
            return False
        i += 1
        j -= 1
    return True


def main():
    strings_list = ("Able was I ere I saw Elba", "A man, a plan, a canal – Panama",
                    "Madam, I'm Adam", "Never odd or even", "Marta is doing lab",
                    "test function")
    for i in range(0, len(strings_list)):
        if is_palindrome(strings_list[i]):
            print(strings_list[i] + " : true")
        else:
            print(strings_list[i] + " : false")


if __name__ == '__main__':
    main()
