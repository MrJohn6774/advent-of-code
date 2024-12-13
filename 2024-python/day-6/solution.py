from collections import deque
from itertools import cycle
import time
from aocd import get_data, submit
import numpy as np

use_example = False
submit_ans = False and not use_example

if use_example:
    with open('example.txt') as f:
        grid = np.array([list(line) for line in f.read().splitlines()])
else:
    grid = np.array([list(line) for line in get_data(year=2024, day=6).splitlines()])

s_pos = [(x, y) for y, line in enumerate(grid) for x, ch in enumerate(line) if ch == '^'][0]
pos = s_pos
directions = cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])
dx, dy = next(directions)
x, y = pos
visited = deque([pos])

while 0 <= x < len(grid[0]) and 0 <= y < len(grid):
    while grid[y][x] == '#':
        dx, dy = next(directions)
        x, y = pos[0] + dx, pos[1] + dy
        if not (0 <= x < len(grid[0]) and 0 <= y < len(grid)):
            break
    pos = (x, y)

    if pos not in visited:
        visited.append(pos)

    x, y = pos[0] + dx, pos[1] + dy

ans_a = len(visited)
print('Part 1: ', ans_a)


start_time = time.time()
ans_b = 0
visited.popleft()
grid_test = grid.copy()

while visited:
    pos = s_pos
    x, y = pos
    directions = cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])
    dx, dy = next(directions)
    visited_dir = set()

    # insert obstacle in path
    test_x, test_y = visited.pop()
    grid_test[test_y][test_x] = '#'

    # run simulation
    while 0 <= x < len(grid_test[0]) and 0 <= y < len(grid_test):
        while grid_test[y][x] == '#':
            dx, dy = next(directions)
            x, y = pos[0] + dx, pos[1] + dy
            if not (0 <= x < len(grid_test[0]) and 0 <= y < len(grid_test)):
                break
        pos = (x, y)

        # loop detection
        if (pos, (dx, dy)) not in visited_dir:
            visited_dir.add((pos, (dx, dy)))
        else:
            ans_b += 1
            break

        x, y = pos[0] + dx, pos[1] + dy
    
    # remove obstacle
    grid_test[test_y][test_x] = '.'

end_time = time.time()
print('Part 2: ', ans_b)
print('Part 2 execution time: ', end_time - start_time, 's')

if submit_ans:
    submit(ans_a, part='a', year=2024, day=6)
    submit(ans_b, part='b', year=2024, day=6)
