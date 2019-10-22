def generate_squares(number: int):
    numbers = {x: x ** 2 for x in range(1, number)}
    return numbers


def main():
    print(generate_squares(5))


if __name__ == '__main__':
    main()
