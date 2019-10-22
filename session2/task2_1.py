"""
Implement a function which receives a string and replaces all symbols "" with ' and vise versa.
"""


def replace_quotes(source_string: str) -> str:
    return source_string.translate(
        source_string.maketrans({"'": '"', '"': "'"})
    )


def main():
    result_string: str = replace_quotes("Laaab '' \"\" uuu ' \" ")
    print(result_string)
    result_string: str = replace_quotes("Laab \"'' ' u'uu' ' \" ")
    print(result_string)


if __name__ == '__main__':
    main()

