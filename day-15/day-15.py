from common.common import read_file


def dijkstra(graph, start, goal):
    Q = set(graph)
    dist = {v: float("inf") for v in graph}
    dist[start] = 0
    prev = {}

    while Q:
        u = min(Q, key=dist.__getitem__)
        Q.remove(u)

        for i, d in enumerate(graph[u]):
            if d == None: continue
            v = get_new_pos(i, *u)

            alt = dist[u] + d
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    path = generate_path(start, goal, prev)
    return path, dist[goal]


def test(filename):
    lines = read_file(filename)


def main(filename):
    lines = read_file(filename)

    p1 = None
    p2 = None

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    test('input.test.txt')
    main('input.txt')
