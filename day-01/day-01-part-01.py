from common.common import read_file


def main():
    lines = read_file('day-01.txt')
    numbers = [int(line) for line in lines]

    counter = 0
    previous_number = numbers.pop(0)
    for n in numbers:
        if n > previous_number:
            counter += 1
        previous_number = n
    print(counter)


if __name__ == '__main__':
    main()
