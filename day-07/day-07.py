import sys
from collections import Counter

from common.common import read_file


def get_points(line):
    points = line.split(',')
    points = [int(point) for point in points]
    return points


def calculate_fuel(points, position, constant_rate):
    fuel = 0
    point_count = Counter(points)
    for point, count in point_count.items():
        distance = abs(position - point)
        if constant_rate:
            fuel += distance * count
        else:
            fuel += sum(range(1, distance + 1)) * count
    return fuel


def find_lowest_consumption(points, constant_rate=True):
    min_pos = min(points)
    max_pos = max(points)

    lowest_consumption = sys.maxsize
    for position in range(min_pos, max_pos + 1):
        consumption = calculate_fuel(points, position, constant_rate)
        if consumption < lowest_consumption:
            lowest_consumption = consumption

    return lowest_consumption


def main():
    lines = read_file('day-07.txt')
    points = get_points(lines[0])

    p1 = find_lowest_consumption(points)
    print(f'{p1=}')

    p2 = find_lowest_consumption(points, False)
    print(f'{p2=}')


if __name__ == '__main__':
    _lines = read_file('day-07.test.txt')
    _points = get_points(_lines[0])

    assert find_lowest_consumption(_points) == 37
    assert find_lowest_consumption(_points, False) == 168

    main()
