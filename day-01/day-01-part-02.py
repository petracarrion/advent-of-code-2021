from common.common import read_file


def main():
    lines = read_file('day-01.txt')
    numbers = [int(line) for line in lines]

    groups = []
    for idx in range(len(numbers) - 2):
        groups.append(numbers[idx] + numbers[idx + 1] + numbers[idx + 2])
    print(groups)

    counter = 0
    previous_number = groups.pop(0)
    for n in groups:
        if n > previous_number:
            counter += 1
        previous_number = n

    print(counter)


if __name__ == '__main__':
    main()
