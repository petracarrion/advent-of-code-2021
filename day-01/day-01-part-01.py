def main():
    with open('day-01-part-01.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
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
