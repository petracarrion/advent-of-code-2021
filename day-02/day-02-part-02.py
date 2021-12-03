from common.common import read_file


def next_pos(position, move):
    horizontal_position, depth, aim = position

    direction, length = move.split()
    length = int(length)
    if direction == 'forward':
        horizontal_position += length
        depth += length * aim
    elif direction == 'up':
        aim -= length
    elif direction == 'down':
        aim += length

    return [horizontal_position, depth, aim]


def test_next_pos():
    assert next_pos([0, 0, 0], 'forward 1') == [1, 0, 0]
    assert next_pos([0, 0, 0], 'forward 5') == [5, 0, 0]

    assert next_pos([0, 0, 0], 'up 1') == [0, 0, -1]
    assert next_pos([0, 0, 0], 'up 5') == [0, 0, -5]

    assert next_pos([0, 0, 0], 'down 1') == [0, 0, 1]
    assert next_pos([0, 0, 0], 'down 5') == [0, 0, 5]

    assert next_pos([10, 10, -5], 'forward 5') == [15, -15, -5]
    assert next_pos([10, 10, -5], 'up 5') == [10, 10, -10]
    assert next_pos([10, 10, -5], 'down 5') == [10, 10, 0]

    assert next_pos([10, 10, 0], 'forward 5') == [15, 10, 0]
    assert next_pos([10, 10, 0], 'up 5') == [10, 10, -5]
    assert next_pos([10, 10, 0], 'down 5') == [10, 10, 5]

    assert next_pos([10, 10, 5], 'forward 5') == [15, 35, 5]
    assert next_pos([10, 10, 5], 'up 5') == [10, 10, 0]
    assert next_pos([10, 10, 5], 'down 5') == [10, 10, 10]


def test_example():
    """
    - forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
    - down 5 adds 5 to your aim, resulting in a value of 5.
    - forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by
    8*5=40.
    - up 3 decreases your aim by 3, resulting in a value of 2.
    - down 8 adds 8 to your aim, resulting in a value of 10.
    - forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by
    2*10=20 to a total of 60.

    After following these new instructions, you would have a horizontal position of 15 and a depth of 60. (Multiplying
    these produces 900.)
    """
    moves = [
        'forward 5',
        'down 5',
        'forward 8',
        'up 3',
        'down 8',
        'forward 2',
    ]
    position = [0, 0, 0]
    for move in moves:
        position = next_pos(position, move)
    print()
    print(f'{position=}')
    multiplication = position[0] * position[1]
    print(f'{multiplication=}')
    assert multiplication == 900


def main():
    lines = read_file('day-02.txt')

    position = [0, 0, 0]
    for move in lines:
        position = next_pos(position, move)

    print(f'{position=}')
    multiplication = position[0] * position[1]
    print(f'{multiplication=}')


if __name__ == '__main__':
    test_next_pos()
    test_example()
    main()
