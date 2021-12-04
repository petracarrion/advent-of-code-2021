from common.common import read_file


def main():
    lines = read_file('day-05.txt')

    print(f'{lines=}')


if __name__ == '__main__':
    _lines = read_file('day-05-test.txt')

    print(f'{_lines=}')

    main()
