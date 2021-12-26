from collections import Counter

from common.common import read_file


def get_grid(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, value in enumerate(list(line)):
            grid[(x, y)] = int(value)
    return grid


def get_graph(grid, width, height):
    graph = {}
    for y in range(height):
        for x in range(width):
            # N E S W
            connections = {}

            if y - 1 >= 0:
                new_pos = (x, y - 1)
                connections[new_pos] = grid[new_pos]

            if x + 1 < width:
                new_pos = (x + 1, y)
                connections[new_pos] = grid[new_pos]

            if y + 1 < height:
                new_pos = (x, y + 1)
                connections[new_pos] = grid[new_pos]

            if x - 1 >= 0:
                new_pos = (x - 1, y)
                connections[new_pos] = grid[new_pos]

            graph[(x, y)] = connections
    return graph


def get_new_pos(i, x, y):
    if i == 0:
        new_pos = (x, y-1)
    elif i == 1:
        new_pos = (x+1, y)
    elif i == 2:
        new_pos = (x, y+1)
    elif i == 3:
        new_pos = (x-1, y)
    return new_pos


def generate_path(start, goal, prev):
    path = []
    p = goal
    while p != start:
        path.append(p)
        p = prev[p]
    path.append(start)
    path.reverse()
    return path


def get_dijkstra(graph, start, goal):
    queue = set(graph)
    dist = {v: float("inf") for v in graph}
    dist[start] = 0
    prev = {}

    while queue:
        current_pos = min(queue, key=dist.__getitem__)
        queue.remove(current_pos)

        connections = graph[current_pos]
        if connections:
            for new_pos, distance in connections.items():
                alternative = dist[current_pos] + distance
                if alternative < dist[new_pos]:
                    dist[new_pos] = alternative
                    prev[new_pos] = current_pos

    path = generate_path(start, goal, prev)
    return path, dist[goal]


def get_lowest_total_rist(lines):
    grid = get_grid(lines)
    last_pos = list(grid.keys())[-1]
    width = last_pos[0] + 1
    height = last_pos[1] + 1
    graph = get_graph(grid, width, height)
    start = (0, 0)
    end = (width - 1, height - 1)
    path, distance = get_dijkstra(graph, start, end)

    return distance


def test(filename):
    lines = read_file(filename)
    grid = get_grid(lines)
    last_pos = list(grid.keys())[-1]
    width = last_pos[0] + 1
    height = last_pos[1] + 1
    graph = get_graph(grid, width, height)
    lowest_total_rist = get_lowest_total_rist(lines)

    assert height == 10
    assert width == 10
    assert len(graph) == 100
    assert lowest_total_rist == 40


def main(filename):
    lines = read_file(filename)

    p1 = get_lowest_total_rist(lines)
    p2 = None

    print(f'{p1=}')
    print(f'{p2=}')


if __name__ == '__main__':
    test('input.test.txt')
    main('input.txt')
