from common.common import read_file


def create_heigthmap(lines):
    heightmap = {}
    for y, line in enumerate(lines):
        for x, height in enumerate(line):
            heightmap[(x, y)] = int(height)

    return heightmap


def get_locations(heightmap):
    return list(heightmap.keys())


def find_adjacent_locations(locations, point):
    x, y = point
    adjacent_locations = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]

    adjacent_locations = [location for location in adjacent_locations if location in locations]

    return adjacent_locations


def find_low_points(heightmap):
    low_points = []
    locations = get_locations(heightmap)

    for position, height in heightmap.items():
        adjacent_locations = find_adjacent_locations(locations, position)
        lower_locations = [location for location in adjacent_locations if heightmap[location] <= height]
        if not lower_locations:
            low_points.append(position)

    return low_points


def calculate_risk_level(heightmap):
    low_points = find_low_points(heightmap)
    risk_level = [heightmap[point] for point in low_points]
    risk_level = sum(risk_level) + len(risk_level)
    return risk_level


def find_basins(heightmap):
    to_sort = list(heightmap.keys())
    to_sort = [point for point in to_sort if heightmap[point] != 9]
    basins = []
    while to_sort:
        point = to_sort.pop()
        basin = [point]
        adjacents = find_adjacent_locations(to_sort, point)
        while adjacents:
            basin += adjacents
            basin = list(set(basin))
            to_sort = [point for point in to_sort if point not in adjacents]
            adjacents = []
            for point in basin:
                adjacents += find_adjacent_locations(to_sort, point)
        basins.append(basin)

    return basins


def calculate_top3_basin_size(basins):
    basin_sizes = [len(basin) for basin in basins]
    basin_sizes = sorted(basin_sizes)
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


def test():
    lines = read_file('day-09.test.txt')
    heightmap = create_heigthmap(lines)
    locations = get_locations(heightmap)
    low_points = find_low_points(heightmap)
    risk_level = calculate_risk_level(heightmap)
    basins = find_basins(heightmap)
    top3_basin_size = calculate_top3_basin_size(basins)

    assert 50 == len(locations), locations
    assert 4 == len(low_points), low_points
    assert 15 == risk_level, risk_level
    assert 4 == len(basins), basins
    assert 1134 == top3_basin_size, top3_basin_size


def main():
    lines = read_file('day-09.txt')
    heightmap = create_heigthmap(lines)

    p1 = calculate_risk_level(heightmap)
    p2 = calculate_top3_basin_size(find_basins(heightmap))

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    test()
    main()
