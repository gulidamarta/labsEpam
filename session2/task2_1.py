"""
Implement a function which receives a string and replaces all symbols "" with ' and vise versa.
"""


def replace_quotes(source_string: str):
    new_string: str = ''
    for i in range(0, len(source_string)):
        if source_string[i] == '"':
            new_string += "'"
            continue
        if source_string[i] == "'":
            new_string += '"'
            continue
        new_string += source_string[i]
    return str(new_string)


def main():
    result_string: str = replace_quotes("Laaab '' \"\" uuu ' \" ")
    print(result_string)
    result_string: str = replace_quotes("Laab \"'' ' u'uu' ' \" ")
    print(result_string)


if __name__ == '__main__':
    main()

