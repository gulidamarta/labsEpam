def count_letters(input_string: str):
    result_dict = {ch: input_string.count(ch) for ch in input_string}
    return result_dict


def main():
    print(count_letters("stringsample"))
    print(count_letters("martamama"))


if __name__ == '__main__':
    main()
