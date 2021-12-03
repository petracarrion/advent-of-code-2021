from common.common import read_file


def get_gamma(lines):
    columns = {}
    for line in lines:
        digits = list(line)
        for idx, digit in enumerate(digits):
            if idx not in columns:
                columns[idx] = []
            columns[idx].append(digit)

    gamma = ['0'] * len(columns.keys())
    for idx, column in columns.items():
        zeros = 0
        ones = 0
        for digit in column:
            if digit == '0':
                zeros += 1
            if digit == '1':
                ones += 1
        gamma[idx] = '1' if ones > zeros else '0'
    gamma = ''.join(gamma)
    return gamma


def get_epsilon(gamma):
    epsilon = ''
    for digit in gamma:
        epsilon += '1' if digit == '0' else '0'

    return epsilon


def get_power_consumtion(lines):
    gamma = get_gamma(lines)
    epsilon = get_epsilon(gamma)

    return int(gamma, 2) * int(epsilon, 2)

def main():
    lines = read_file('day-03.txt')

    power_comsuption = get_power_consumtion(lines)

    print(f'{power_comsuption=}')


if __name__ == '__main__':
    test_data = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
    _lines = test_data.split()

    assert int(get_gamma(_lines), 2) == 22
    assert int(get_epsilon(get_gamma(_lines)), 2) == 9
    assert get_power_consumtion(_lines) == 198

    main()
