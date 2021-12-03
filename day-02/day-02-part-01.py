from common.common import read_file


def next_pos(position, move):
    x = position[0]
    y = position[1]

    direction, length = move.split()
    length = int(length)
    if direction == 'forward':
        x += length
    elif direction == 'up':
        y -= length
    elif direction == 'down':
        y += length

    return [x, y]


def test_next_pos():
    assert next_pos([0, 0], 'forward 1') == [1, 0]
    assert next_pos([0, 0], 'forward 5') == [5, 0]

    assert next_pos([0, 0], 'up 1') == [0, -1]
    assert next_pos([0, 0], 'up 5') == [0, -5]

    assert next_pos([0, 0], 'down 1') == [0, 1]
    assert next_pos([0, 0], 'down 5') == [0, 5]

    assert next_pos([10, 10], 'forward 5') == [15, 10]
    assert next_pos([10, 10], 'up 5') == [10, 5]
    assert next_pos([10, 10], 'down 5') == [10, 15]


def main():
    lines = read_file('day-02.txt')

    position = [0, 0]
    for move in lines:
        position = next_pos(position, move)

    print(f'{position=}')
    multiplication = position[0] * position[1]
    print(f'{multiplication=}')


if __name__ == '__main__':
    test_next_pos()
    main()
