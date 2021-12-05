import re

from common.common import read_file


def get_start_ends(lines):
    start_ends = []
    for line in lines:
        start_end = re.findall(r'[0-9]+', line)
        start_end = [int(number) for number in start_end]
        start_ends.append(start_end)
    return start_ends


def get_diagonal(x1, x2, y1, y2):
    diagonal = []
    dx = x2 - x1
    dy = y2 - y1
    abs_dx = abs(dx)
    abs_dy = abs(dy)
    inc_x = dx / abs_dx
    inc_y = dy / abs_dy
    for i in range(1, abs_dx):
        diagonal.append([int(x1 + (i * inc_x)), int(y1 + (i * inc_y))])
    return diagonal


def get_all_points(start_ends, p2):
    all_points = []
    for start_end in start_ends:
        x1, y1, x2, y2 = start_end
        if x1 == x2 or y1 == y2:
            all_points.append([x1, y1])
            all_points.append([x2, y2])
            if x1 < x2:
                for x in range(x1 + 1, x2):
                    all_points.append([x, y1])
            if x2 < x1:
                for x in range(x2 + 1, x1):
                    all_points.append([x, y1])
            if y1 < y2:
                for y in range(y1 + 1, y2):
                    all_points.append([x1, y])
            if y2 < y1:
                for y in range(y2 + 1, y1):
                    all_points.append([x1, y])
        elif p2:
            all_points.append([x1, y1])
            all_points.append([x2, y2])
            all_points += get_diagonal(x1, x2, y1, y2)
    return all_points


def draw_lines(points):
    max_x = 0
    max_y = 0
    for point in points:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]
    matrix = []
    for y in range(max_y + 1):
        matrix.append([0] * (max_x + 1))

    for point in points:
        x, y = point
        matrix[y][x] += 1

    return matrix


def count_overlapping_points(matrix):
    count = 0
    for row in matrix:
        for pos in row:
            if pos > 1:
                count += 1
    return count


def get_overlapping_points(points, p2=False):
    start_ends = get_start_ends(points)
    points = get_all_points(start_ends, p2)
    matrix = draw_lines(points)
    overlapping_points = count_overlapping_points(matrix)
    return overlapping_points


def main():
    lines = read_file('day-05.txt')

    p1 = get_overlapping_points(lines)
    print(f'{p1=}')

    p2 = get_overlapping_points(lines, True)
    print(f'{p2=}')


if __name__ == '__main__':
    _lines = read_file('day-05.test.txt')

    assert get_diagonal(0, 8, 8, 0) == [[1, 7], [2, 6], [3, 5], [4, 4], [5, 3], [6, 2], [7, 1]]
    assert get_overlapping_points(_lines) == 5
    assert get_overlapping_points(_lines, True) == 12

    main()
