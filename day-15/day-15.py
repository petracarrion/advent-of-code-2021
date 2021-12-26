from common.common import read_file


def get_size(grid):
    last_pos = list(grid.keys())[-1]
    width = last_pos[0] + 1
    height = last_pos[1] + 1
    return width, height


def enlarge_grid(grid, factor):
    new_map = {}
    width, height = get_size(grid)
    for tile_x in range(factor):
        for tile_y in range(factor):
            for x in range(width):
                for y in range(height):
                    new_pos = (tile_x * width + x, tile_y * height + y)
                    extra_distance = tile_x + tile_y
                    new_distance = grid[(x, y)] + extra_distance
                    while new_distance > 9:
                        new_distance -= 9
                    new_map[new_pos] = new_distance

    return new_map


def get_grid(lines, factor=1):
    grid = {}
    for y, line in enumerate(lines):
        for x, value in enumerate(list(line)):
            grid[(x, y)] = int(value)
    grid = enlarge_grid(grid, factor)
    return grid


def get_graph(grid):
    width, height = get_size(grid)
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


def get_lowest_total_rist(lines, factor=1):
    grid = get_grid(lines, factor)
    width, height = get_size(grid)
    graph = get_graph(grid)
    start = (0, 0)
    end = (width - 1, height - 1)
    path, distance = get_dijkstra(graph, start, end)

    return distance


def test(filename):
    lines = read_file(filename)
    grid = get_grid(lines)
    enlarged_grid = get_grid(lines, 5)
    last_pos = list(grid.keys())[-1]
    width = last_pos[0] + 1
    height = last_pos[1] + 1
    graph = get_graph(grid)
    enlarged_graph = get_graph(enlarged_grid)

    assert height == 10
    assert width == 10
    assert len(graph) == 100
    assert len(enlarged_graph) == 2500
    assert get_lowest_total_rist(lines) == 40
    assert get_lowest_total_rist(lines, 5) == 315


def main(filename):
    lines = read_file(filename)

    p1 = get_lowest_total_rist(lines)
    print(f'{p1=}')

    p2 = get_lowest_total_rist(lines, 5)
    print(f'{p2=}')


if __name__ == '__main__':
    test('input.test.txt')
    main('input.txt')
