from common.common import read_file


def create_heigthmap(lines):
    heightmap = {}
    for y, line in enumerate(lines):
        for x, height in enumerate(line):
            heightmap[(x, y)] = int(height)

    return heightmap


def get_size(heightmap):
    max_x, max_y = list(heightmap.keys()).pop()
    return max_x + 1, max_y + 1


def find_adjacent_locations(heightmap, position):
    width, height = get_size(heightmap)
    adjacent_locations = []
    x, y = position

    if x > 0:
        adjacent_locations.append((x - 1, y))
    if x < width - 1:
        adjacent_locations.append((x + 1, y))
    if y > 0:
        adjacent_locations.append((x, y - 1))
    if y < height - 1:
        adjacent_locations.append((x, y + 1))

    return adjacent_locations


def find_low_points(heightmap):
    low_points = []

    for position, height in heightmap.items():
        adjacent_locations = find_adjacent_locations(heightmap, position)
        lower_locations = [location for location in adjacent_locations if heightmap[location] <= height]
        if not lower_locations:
            low_points.append(position)

    return low_points


def calculate_risk_level(heightmap):
    low_points = find_low_points(heightmap)
    risk_level = [heightmap[point] for point in low_points]
    risk_level = sum(risk_level) + len(risk_level)
    return risk_level


def test():
    lines = read_file('day-09.test.txt')
    heightmap = create_heigthmap(lines)
    size = get_size(heightmap)
    low_points = find_low_points(heightmap)
    risk_level = calculate_risk_level(heightmap)

    assert (10, 5) == size, size
    assert 4 == len(low_points), low_points
    assert 15 == risk_level, risk_level


def main():
    lines = read_file('day-09.txt')
    heightmap = create_heigthmap(lines)

    p1 = calculate_risk_level(heightmap)
    p2 = None

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    test()
    main()
