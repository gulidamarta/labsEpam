import re


def test1_1(*strings):
    if len(strings) == 0:
        raise Exception("Amount of arguments should be higher than 0.")
    p = re.findall(r'[a+]', "Maarta")
    return p


def main():
    test_strings = ["hello", "world", "python",]
    print(test1_1(test_strings))


if __name__ == '__main__':
    main()