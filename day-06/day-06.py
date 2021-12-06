from collections import Counter

from common.common import read_file


def get_population(line):
    population = line.split(',')
    population = [int(fish) for fish in population]
    population = Counter(population)
    population = dict(population)
    for i in range(9):
        if i not in population.keys():
            population[i] = 0

    return population


def next_day(population):
    next_population = {}

    zero_count = population[0]
    seven_count = population[7]
    for age, count in population.items():
        if age != 0:
            next_population[age - 1] = count
    next_population[6] = zero_count + seven_count
    next_population[8] = zero_count

    return next_population


def grow_population(population, days):
    for i in range(days):
        population = next_day(population)

    fish_count = sum(population.values())
    return fish_count


def main():
    lines = read_file('day-06.txt')
    population = get_population(lines[0])

    p1 = grow_population(population, 80)
    print(f'{p1=}')

    p2 = grow_population(population, 256)
    print(f'{p2=}')


if __name__ == '__main__':
    _lines = read_file('day-06.test.txt')

    _lines = [line.split(':')[1].strip() for line in _lines]
    for _i in range(1, len(_lines)):
        assert next_day(get_population(_lines[_i - 1])) == get_population(_lines[_i])

    _population = get_population(_lines[0])

    assert grow_population(_population, 18) == 26
    assert grow_population(_population, 80) == 5934
    assert grow_population(_population, 256) == 26984457539

    main()
