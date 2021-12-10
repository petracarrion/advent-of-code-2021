from common.common import read_file

openings = ['(', '[', '{', '<']
closings = [')', ']', '}', '>']
expected_mapping = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
found_prize = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
complete_prize = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def find_error(line):
    heap = []
    for found in line:
        if found in openings:
            heap.append(found)
        else:
            expected = expected_mapping[heap.pop()]
            if expected != found:
                return expected, found

    return []


def calculate_error_prize(lines):
    prize = 0
    for line in lines:
        error = find_error(line)
        if error:
            prize += found_prize[error[1]]
    return prize


def remove_invalid(lines):
    valid_lines = [line for line in lines if not find_error(line)]
    return valid_lines


def complete(line):
    heap = []
    for found in line:
        if found in openings:
            heap.append(found)
        else:
            heap.pop()

    missing = ''
    heap = ''.join(reversed(heap))
    for found in heap:
        missing += expected_mapping[found]

    return missing


def calculate_completion_prize(missing):
    prize = 0

    for found in missing:
        prize *= 5
        prize += complete_prize[found]

    return prize


def get_middle_score(lines):
    valid_lines = remove_invalid(lines)
    completion_strings = [complete(line) for line in valid_lines]
    completion_prizes = [calculate_completion_prize(completion_string) for completion_string in completion_strings]
    completion_prizes = sorted(completion_prizes)
    middle = int(len(completion_prizes) / 2)
    middle_score = completion_prizes[middle]
    return middle_score


def test():
    lines = read_file('day-10.test.txt')

    assert find_error('{([(<{}[<>[]}>{[]{[(<()>') == (']', '}')
    assert find_error('[[<[([]))<([[{}[[()]]]') == (']', ')')
    assert find_error('[{[{({}]{}}([{[{{{}}([]') == (')', ']')
    assert find_error('[<(<(<(<{}))><([]([]()') == ('>', ')')
    assert find_error('<{([([[(<>()){}]>(<<{{') == (']', '>')

    assert calculate_error_prize(lines) == 26397
    assert len(remove_invalid(lines)) == 5

    assert complete('[({(<(())[]>[[{[]{<()<>>') == '}}]])})]'
    assert complete('[(()[<>])]({[<{<<[]>>(') == ')}>]})'
    assert complete('(((({<>}<{<{<>}{[]{[]{}') == '}}>}>))))'
    assert complete('{<[[]]>}<{[{[{[]{()[[[]') == ']]}}]}]}>'
    assert complete('<{([{{}}[<[[[<>{}]]]>[]]') == '])}>'

    assert calculate_completion_prize('}}]])})]') == 288957
    assert calculate_completion_prize(')}>]})') == 5566
    assert calculate_completion_prize('}}>}>))))') == 1480781
    assert calculate_completion_prize(']]}}]}]}>') == 995444
    assert calculate_completion_prize('])}>') == 294

    assert get_middle_score(lines) == 288957


def main():
    lines = read_file('day-10.txt')

    p1 = calculate_error_prize(lines)
    p2 = get_middle_score(lines)

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    test()
    main()
