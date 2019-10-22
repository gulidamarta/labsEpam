def combine_dicts(*args):
    if len(args) <= 1:
        raise Exception("You can combine only 2 and more dictionaries.")

    res_dict = dict()

    for i in range(len(args) - 1):
        res_dict.update({**args[i], **args[i + 1]})
    return res_dict


def main():
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'c': 300, 'd': 400}
    dict_3 = {'k': 150, 'm': 250}
    print(combine_dicts(dict_1, dict_2))
    print(combine_dicts(dict_1, dict_2, dict_3))


if __name__ == '__main__':
    main()
