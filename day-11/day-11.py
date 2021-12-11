from common.common import read_file


class AllFlashedException(Exception):
    def __init__(self, step):
        self.step = step


def create_map(lines):
    heightmap = {}
    for y, line in enumerate(lines):
        for x, height in enumerate(line):
            heightmap[(x, y)] = int(height)

    return heightmap


def increase(energy_map, positions, inc=1):
    return {pos: energy + inc if pos in positions else energy for (pos, energy) in energy_map.items()}


def get_adjacents(positions, pos):
    x, y = pos
    adjacents = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x - 1, y - 1),
    ]
    adjacents = [pos for pos in adjacents if pos in positions]
    return adjacents


def find_to_flash(energy_map, flashed):
    to_flash = [pos for pos in energy_map.keys() if pos not in flashed and energy_map[pos] > 9]
    return to_flash


def flash(energy_map, step):
    energy_map = energy_map.copy()
    all_positions = list(energy_map.keys())
    flashed = []
    to_flash = find_to_flash(energy_map, flashed)
    while to_flash:
        for pos in to_flash:
            adjacent = get_adjacents(all_positions, pos)
            energy_map = increase(energy_map, adjacent)
            flashed.append(pos)
        to_flash = find_to_flash(energy_map, flashed)
    for pos in flashed:
        energy_map[pos] = 0
    if len(flashed) == len(all_positions):
        raise AllFlashedException(step)
    return energy_map, len(flashed)


def count_flashes(energy_map, steps):
    all_positions = list(energy_map.keys())
    total_count = 0
    for i in range(steps):
        energy_map = increase(energy_map, all_positions)
        energy_map, step_count = flash(energy_map, i + 1)
        total_count += step_count
    return total_count


def find_simultaneously_flash(energy_map):
    try:
        count_flashes(energy_map, 1000000)
    except AllFlashedException as exc:
        return exc.step


def test():
    lines = read_file('day-11.test.txt')
    energy_map = create_map(lines)
    all_positions = list(energy_map.keys())

    increased = increase(energy_map, all_positions)
    flashed, flash_count = flash(increased, 1)
    assert flash_count == 0

    assert count_flashes(energy_map, 2) == 35
    assert count_flashes(energy_map, 10) == 204
    assert count_flashes(energy_map, 100) == 1656

    assert find_simultaneously_flash(energy_map) == 195


def main():
    lines = read_file('day-11.txt')
    energy_map = create_map(lines)

    p1 = count_flashes(energy_map, 100)
    p2 = find_simultaneously_flash(energy_map)

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    test()
    main()
