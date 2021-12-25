from common.common import read_file


def create_map(lines):
    cucumber_map = {}
    for y, line in enumerate(lines):
        for x, value in enumerate(list(line)):
            cucumber_map[(x, y)] = value

    return cucumber_map


def move_east(cucumber_map):
    next_cucumber_map = cucumber_map.copy()
    for pos, value in cucumber_map.items():
        if cucumber_map[pos] == '>':
            x, y = pos
            next_pos = (x + 1, y)
            if next_pos not in cucumber_map:
                next_pos = (0, y)
            if cucumber_map[next_pos] == '.':
                next_cucumber_map[pos] = '.'
                next_cucumber_map[next_pos] = '>'
    return next_cucumber_map


def move_south(cucumber_map):
    next_cucumber_map = cucumber_map.copy()
    for pos, value in cucumber_map.items():
        if cucumber_map[pos] == 'v':
            x, y = pos
            next_pos = (x, y + 1)
            if next_pos not in cucumber_map:
                next_pos = (x, 0)
            if cucumber_map[next_pos] == '.':
                next_cucumber_map[pos] = '.'
                next_cucumber_map[next_pos] = 'v'
    return next_cucumber_map


def get_next_step(cucumber_map):
    next_cucumber_map = cucumber_map.copy()
    next_cucumber_map = move_east(next_cucumber_map)
    next_cucumber_map = move_south(next_cucumber_map)
    return next_cucumber_map


def print_map(cucumber_map):
    for pos, value in cucumber_map.items():
        x, y = pos
        if x == 0:
            print()
        print(value, end="")


def get_stop_step(lines):
    cucumber_map = create_map(lines)
    last_cucumber_map = None
    step = 0
    while last_cucumber_map != cucumber_map:
        step += 1
        last_cucumber_map = cucumber_map
        cucumber_map = get_next_step(cucumber_map)

    return step


def test(filename):
    lines = read_file(filename)
    cucumber_map = create_map(lines)
    stop_step = get_stop_step(lines)

    assert len(cucumber_map.keys()) == 90
    assert stop_step == 58


def main(filename):
    lines = read_file(filename)

    p1 = get_stop_step(lines)
    p2 = None

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    test('input.test.txt')
    main('input.txt')
