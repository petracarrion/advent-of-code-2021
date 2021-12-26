from common.common import read_file


def test(filename):
    lines = read_file(filename)


def main(filename):
    lines = read_file(filename)

    p1 = None
    print(f'{p1=}')

    p2 = None
    print(f'{p2=}')


if __name__ == '__main__':
    test('input.test.txt')
    main('input.txt')
