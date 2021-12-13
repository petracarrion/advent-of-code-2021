from common.common import read_file


def parse_lines(lines):
    paper = {}
    folds = []
    max_x = 0
    max_y = 0
    for line in lines:
        comma_split = line.split(',')
        equal_split = line.split('=')
        if len(comma_split) == 2:
            x, y = comma_split
            x, y = int(x), int(y)
            pos = (x, y)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            paper[pos] = True
        if len(equal_split) == 2:
            axis, pos = equal_split
            axis = axis[-1]
            pos = int(pos)
            folds.append((axis, pos))
    size_x, size_y = (max_x + 1, max_y + 1)
    paper_size = size_x, size_y
    full_paper = {}
    for x in range(size_x):
        for y in range(size_y):
            pos = (x, y)
            full_paper[pos] = pos in paper.keys()
    return full_paper, paper_size, folds


def half(n):
    return int((n - 1) / 2)


def get_folded_pos(axis, folded_pos, x, y):
    folded_x, folded_y = x, y
    if axis == 'x':
        dist = folded_pos - x
        folded_x = x + (2 * dist)
    if axis == 'y':
        dist = folded_pos - y
        folded_y = y + (2 * dist)
    return folded_x, folded_y


def fold_paper(paper, paper_size, fold):
    axis, folded_pos = fold
    folded_x, folded_y = paper_size
    if axis == 'x':
        folded_x = folded_pos
    if axis == 'y':
        folded_y = folded_pos

    folded_paper = {}
    for x in range(folded_x):
        for y in range(folded_y):
            pos = (x, y)
            folded_paper[pos] = paper[pos] or paper.get(get_folded_pos(axis, folded_pos, x, y), False)
    folded_size = (folded_x, folded_y)
    return folded_paper, folded_size


def count_dots(paper):
    dot_count = [1 for value in paper.values() if value]
    dot_count = sum(dot_count)
    return dot_count


def print_paper(paper, paper_size):
    width, height = paper_size
    for y in range(height):
        line = ''
        for x in range(width):
            line += '*' if paper[(x, y)] else ' '
        print(line)


def test(filename):
    lines = read_file(filename)
    paper, paper_size, folds = parse_lines(lines)
    first_fold, fold_size = fold_paper(paper, paper_size, folds[0])
    dot_count = count_dots(first_fold)
    second_fold, fold_size = fold_paper(first_fold, fold_size, folds[1])
    print_paper(second_fold, fold_size)

    assert len(paper.keys()) == 165
    assert paper_size == (11, 15)
    assert len(folds) == 2
    assert folds
    assert dot_count == 17


def main(filename):
    lines = read_file(filename)
    orig_paper, orig_paper_size, folds = parse_lines(lines)
    first_fold, fold_size = fold_paper(orig_paper, orig_paper_size, folds[0])
    dot_count = count_dots(first_fold)

    paper = orig_paper
    paper_size = orig_paper_size
    for fold in folds:
        paper, paper_size = fold_paper(paper, paper_size, fold)

    p1 = dot_count
    p2 = 'See bellow:'

    print(f'{p1=}')
    print(f'{p2=}')
    print_paper(paper, paper_size)


if __name__ == '__main__':
    test('input.test.txt')
    main('input.txt')
