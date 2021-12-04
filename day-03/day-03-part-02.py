from common.common import read_file


def count_bits(numbers, idx):
    bits = [number[idx] for number in numbers]
    bit_count = [0, 0]
    for bit in bits:
        if bit == '0':
            bit_count[0] += 1
        if bit == '1':
            bit_count[1] += 1

    return bit_count


def get_most_common_bit(numbers, idx):
    bit_count = count_bits(numbers, idx)
    return '0' if bit_count[0] > bit_count[1] else '1'


def get_least_common_bit(numbers, idx):
    bit_count = count_bits(numbers, idx)
    return '1' if bit_count[0] > bit_count[1] else '0'


def apply_criteria(numbers, criteria):
    idx = 0
    while len(numbers) > 1:
        criteria_bit = criteria(numbers, idx)
        numbers = [number for number in numbers if number[idx] == criteria_bit]
        idx += 1

    return numbers[0]


def get_oxigen(numbers):
    return apply_criteria(numbers, get_most_common_bit)


def get_co2(numbers):
    return apply_criteria(numbers, get_least_common_bit)


def get_life_support_rating(numbers):
    oxigen = get_oxigen(numbers)
    co2 = get_co2(numbers)

    oxigen = int(oxigen, 2)
    co2 = int(co2, 2)

    return oxigen * co2


def main():
    lines = read_file('day-03.txt')

    life_support_rating = get_life_support_rating(lines)

    print(f'{life_support_rating=}')


if __name__ == '__main__':
    _lines = read_file('day-03-test.txt')

    assert get_oxigen(_lines) == '10111'
    assert get_co2(_lines) == '01010'
    assert get_life_support_rating(_lines) == 230

    main()
