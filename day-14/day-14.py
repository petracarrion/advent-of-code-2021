from collections import Counter

from common.common import read_file


def parse_polymer(polymer):
    pair_count = {}
    molecule_count = {polymer[0]: 1}

    last_molecule = polymer[0]
    for i in range(1, len(polymer)):
        molecule = polymer[i]
        pair = last_molecule + polymer[i]
        if pair not in pair_count:
            pair_count[pair] = 0
        pair_count[pair] += 1
        if molecule not in molecule_count:
            molecule_count[molecule] = 0
        molecule_count[molecule] += 1
        last_molecule = molecule

    return pair_count, molecule_count


def parse_lines(lines):
    template = lines[0]
    insertions = [line.split(' -> ') for line in lines[2:]]
    insertions = {insertion[0]: insertion[1] for insertion in insertions}

    return template, insertions


def grow(polymer, insertions, step_count):
    pair_count, molecule_count = parse_polymer(polymer)
    while step_count > 0:
        print('Step: ', step_count)
        last_pair_count = pair_count
        pair_count = {}
        for pair, count in last_pair_count.items():
            if pair not in pair_count.keys():
                pair_count[pair] = 0
            if pair in insertions.keys():
                insertion = insertions[pair]
                if insertion not in molecule_count:
                    molecule_count[insertion] = 0
                molecule_count[insertion] += count
                pair_left = pair[0] + insertion
                pair_right = insertion + pair[1]
                if pair_left not in pair_count.keys():
                    pair_count[pair_left] = 0
                pair_count[pair_left] += count
                if pair_right not in pair_count.keys():
                    pair_count[pair_right] = 0
                pair_count[pair_right] += count
        step_count -= 1
    return pair_count, molecule_count


def get_difference(polymer, insertions, step_count):
    pair_count, molecule_count = grow(polymer, insertions, step_count)

    molecule_count = Counter(molecule_count)
    sorted_molecule_count = molecule_count.most_common()
    most_common = sorted_molecule_count[0]
    less_common = sorted_molecule_count[-1]
    difference = most_common[1] - less_common[1]

    return difference


def test(filename):
    lines = read_file(filename)

    template, insertions = parse_lines(lines)

    difference = get_difference(template, insertions, 10)
    assert difference == 1588

    difference = get_difference(template, insertions, 40)
    assert difference == 2188189693529


def main(filename):
    lines = read_file(filename)
    template, insertions = parse_lines(lines)

    p1 = get_difference(template, insertions, 10)
    p2 = get_difference(template, insertions, 40)

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    test('input.test.txt')
    main('input.txt')
