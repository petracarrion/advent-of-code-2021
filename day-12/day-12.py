from functools import lru_cache

from common.common import read_file
import sys

sys.setrecursionlimit(150000)


def get_graph(lines):
    graph = [tuple(line.split('-')) for line in lines if not line.startswith('end-') and not line.endswith('-start')]
    graph += [tuple(line.split('-')[::-1]) for line in lines if not line.startswith('start-') and not line.endswith('-end')]
    return tuple(set(graph))


def get_adjacents(graph, start):
    adjacents = [edge[1] for edge in graph if edge[0] == start]
    return adjacents


def remove_lower(graph, node):
    graph = tuple(edge for edge in graph if edge[1] != node or node.isupper())
    return graph


@lru_cache(maxsize=None)
def remove_lower_visited_twice(graph, path, node):
    lower_in_path = [node for node in path[1:] if node.islower()]
    if node.islower():
        lower_in_path.append(node)
    visited_lower_twice = len(lower_in_path) != len(set(lower_in_path))
    graph = tuple(edge for edge in graph if
                  node.isupper() or (edge[1] not in lower_in_path) or not visited_lower_twice)
    return graph


def test_remove_lower_visited_twice():
    g1 = (('d', 'b'), ('b', 'd'), ('b', 'A'), ('b', 'end'), ('c', 'A'), ('A', 'c'), ('A', 'b'), ('A', 'end'))
    p1 = ('start', 'A', 'c', 'A')
    n1 = 'c'
    r1 = remove_lower_visited_twice(g1, p1, n1)
    e1 = (('d', 'b'), ('b', 'd'), ('b', 'A'), ('b', 'end'), ('c', 'A'), ('A', 'b'), ('A', 'end'))
    assert r1 == e1

    g1 = (('b', 'A'), ('A', 'c'), ('d', 'b'), ('A', 'end'), ('A', 'b'), ('b', 'end'), ('b', 'd'), ('c', 'A'))
    p1 = ('start', 'b', 'A', 'c', 'A')
    n1 = 'c'
    r1 = remove_lower_visited_twice(g1, p1, n1)
    e1 = (('b', 'A'), ('A', 'end'), ('b', 'end'), ('b', 'd'), ('c', 'A'))
    assert r1 == e1


@lru_cache(maxsize=None)
def find_all_paths(graph, path=None, start='start', end='end', revisit_lower=False):
    if path is None:
        path = ()
    all_paths = ()
    if revisit_lower:
        graph = remove_lower_visited_twice(graph, path, start)
    else:
        graph = remove_lower(graph, start)
    adjacents = get_adjacents(graph, start)
    for node in adjacents:
        if node == end:
            new_path = ((path + (start, node),),)
            all_paths += new_path
        else:
            new_path = path + (start,)
            new_all_paths = find_all_paths(graph, new_path, node, end, revisit_lower=revisit_lower)
            all_paths += new_all_paths
    all_paths = tuple(x for x in all_paths if x)
    return all_paths


def test(filename, revisit_lower=False):
    lines = read_file(filename)

    graph = get_graph(lines)
    all_paths = find_all_paths(graph, revisit_lower=revisit_lower)
    all_paths = set(all_paths)
    all_paths = list(all_paths)
    all_paths = sorted(all_paths)

    if filename == 'day-12.test.txt':
        assert len(graph) == 10
        if revisit_lower:
            assert len(all_paths) == 36
        else:
            assert len(all_paths) == 10
    if filename == 'day-12.test2.txt':
        assert len(graph) == 15
        if revisit_lower:
            assert len(all_paths) == 103
        else:
            assert len(all_paths) == 19
    if filename == 'day-12.test3.txt':
        assert len(graph) == 31
        if revisit_lower:
            assert len(all_paths) == 3509
        else:
            assert len(all_paths) == 226


def main(filename):
    lines = read_file(filename)
    graph = get_graph(lines)

    p1 = len(find_all_paths(graph))
    p2 = len(find_all_paths(graph, revisit_lower=True))

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    test_remove_lower_visited_twice()
    test('day-12.test.txt')
    test('day-12.test2.txt')
    test('day-12.test3.txt')
    test('day-12.test.txt', True)
    test('day-12.test2.txt', True)
    test('day-12.test3.txt', True)
    main('day-12.txt')
