from collections import Counter

from common.common import read_file


def get_unique_segment_length(segments):
    lengths = [len(segment.replace(' ', '')) for segment in segments.values()]
    counter = Counter(lengths)
    unique_segments_lengths = [key for key, count in counter.items() if count == 1]
    return unique_segments_lengths


def count_unique_in_output(lines):
    output = [line[10:] for line in lines]

    count = 0
    for line in output:
        for digit in line:
            if len(digit.replace(' ', '')) in unique_segment_length:
                count += 1

    return count


def map_unique_segments(line):
    segments = {}
    for segment in line:
        length = len(segment)
        if length in unique_segment_length:
            segments[length_mapping[length]] = ''.join(sorted(segment))
    return segments


def map_digits(unique_segment_mapping, orig_by_length, to_map_by_length):
    unique_to_map = unique_segment_mapping.copy()
    orig_by_length = orig_by_length.copy()
    to_map_by_length = to_map_by_length.copy()
    mapping = {}
    digits = 'abcdefg'
    for digit in digits:
        if digit in unique_to_map['abc    '] and digit not in unique_to_map[' bc    ']:
            mapping['a'] = digit
    for digit in mapping.values():
        for segment in unique_to_map:
            unique_to_map[segment] = unique_to_map[segment].replace(digit, '')
        for length in to_map_by_length:
            to_map_by_length[length] = [segment.replace(digit, '') for segment in to_map_by_length[length]]
    for digit in mapping.keys():
        for length in orig_by_length:
            orig_by_length[length] = [segment.replace(digit, '') for segment in orig_by_length[length]]

    length_5 = [item for sublist in to_map_by_length[5] for item in sublist]
    length_5_count = Counter(length_5)
    e_or_f = [digit for digit, count in length_5_count.items() if count == 1]
    d_or_e = set(unique_to_map['abcdefg']).difference(set(unique_to_map[' bc  fg']))
    f_or_g = set(unique_to_map[' bc  fg']).difference(set(unique_to_map[' bc    ']))

    e = d_or_e.intersection(e_or_f)
    assert len(e) == 1
    mapping['e'] = e.pop()

    f = set(e_or_f).difference({mapping['e']})
    assert len(f) == 1
    mapping['f'] = f.pop()

    g = f_or_g.difference({mapping['f']})
    assert len(g) == 1
    mapping['g'] = g.pop()

    d = d_or_e.difference({mapping['e']})
    assert len(d) == 1
    mapping['d'] = d.pop()

    for digit in mapping.values():
        for segment in unique_to_map:
            unique_to_map[segment] = unique_to_map[segment].replace(digit, '')
        for length in to_map_by_length:
            to_map_by_length[length] = [segment.replace(digit, '') for segment in to_map_by_length[length]]
    for digit in mapping.keys():
        for length in orig_by_length:
            orig_by_length[length] = [segment.replace(digit, '') for segment in orig_by_length[length]]

    length_6 = [item for sublist in to_map_by_length[6] for item in sublist]
    length_6_count = Counter(length_6)

    c = [digit for digit, count in length_6_count.items() if count == 3]
    assert len(c) == 1
    mapping['c'] = c.pop()

    b = [digit for digit, count in length_6_count.items() if count == 2]
    assert len(b) == 1
    mapping['b'] = b.pop()

    mapping = {v: k for k, v in mapping.items()}

    return mapping


def sort_segments_by_length(line):
    by_length = {}
    for segment in line:
        segment = ''.join(sorted(segment))
        length = len(segment.replace(' ', ''))
        if length not in by_length.keys():
            by_length[length] = []
        if segment not in by_length[length]:
            by_length[length].append(segment)

    return by_length


def decode_segment(segment, digit_mapping):
    decoded = ''
    for i in segment:
        decoded += digit_mapping[i]

    decoded = ''.join(sorted(decoded))
    decoded = segment_map_inverted[decoded]
    return decoded


def decode_line_output(line, digit_mapping):
    output = line[10:]
    line_output = ''
    for segment in output:
        line_output += decode_segment(segment, digit_mapping)

    return int(line_output)


def calculate_output(lines):
    output = 0
    orig_by_length = sort_segments_by_length(segment_map.values())
    for line in lines:
        unique_segment_mapping = map_unique_segments(line)
        to_map_by_length = sort_segments_by_length(line)
        digit_mapping = map_digits(unique_segment_mapping, orig_by_length, to_map_by_length)
        output += decode_line_output(line, digit_mapping)

    return output


def test():
    lines = read_file('day-08.test.txt')
    lines = [line.replace('|', '') for line in lines]
    lines = [line.split() for line in lines]

    assert count_unique_in_output(lines) == 26

    outputs = [
        8394,
        9781,
        1197,
        9361,
        4873,
        8418,
        4548,
        1625,
        8717,
        4315,
    ]

    orig_by_length = sort_segments_by_length(segment_map.values())
    for idx, line in enumerate(lines):
        unique_segment_mapping = map_unique_segments(line)
        to_map_by_length = sort_segments_by_length(line)
        digit_mapping = map_digits(unique_segment_mapping, orig_by_length, to_map_by_length)
        line_output = decode_line_output(line, digit_mapping)

        assert len(unique_segment_mapping.keys()) == 4
        assert len(digit_mapping.keys()) == 7
        assert line_output == outputs[idx]

    assert calculate_output(lines) == 61229


def main():
    lines = read_file('day-08.txt')
    lines = [line.replace('|', '') for line in lines]
    lines = [line.split() for line in lines]

    p1 = count_unique_in_output(lines)
    p2 = calculate_output(lines)

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    segment_map = {
        0: 'abcdef ',
        1: ' bc    ',  # unique
        2: 'ab de g',
        3: 'abcd  g',
        4: ' bc  fg',  # unique
        5: 'a cd fg',
        6: 'a cdefg',
        7: 'abc    ',  # unique
        8: 'abcdefg',  # unique
        9: 'abcd fg',
    }

    segment_map_inverted = {}
    for digit, segment in segment_map.items():
        segment = segment.replace(' ', '')
        digit = str(digit)
        segment_map_inverted[segment] = digit

    unique_segment_map = {
        1: ' bc    ',  # unique
        4: ' bc  fg',  # unique
        7: 'abc    ',  # unique
        8: 'abcdefg',  # unique
    }
    unique_segment_length = get_unique_segment_length(segment_map)
    unique_segments = [segment for segment in segment_map.values() if len(segment) in unique_segment_length]
    length_mapping = {}
    for segment in unique_segments:
        length_mapping[len(segment.replace(' ', ''))] = segment

    test()
    main()
