from common.common import read_file


def test():
    lines = read_file('day-09.test.txt')


def main():
    lines = read_file('day-09.txt')

    p1 = None
    p2 = None

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':

    test()
    main()
