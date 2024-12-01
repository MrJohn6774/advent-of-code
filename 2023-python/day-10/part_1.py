from aocd import get_data
from collections import deque
from typing import Tuple


# with open('example.txt') as f:
    # grid = f.read().splitlines()

grid = get_data(day=10, year=2023).strip().splitlines()

pos_s = next((y, row.index('S')) for y, row in enumerate(grid) if 'S' in row)
print('S: ', pos_s)

visited = [pos_s]
visit_next = deque([pos_s])

def get_connections(tile_coord: Tuple[int, int]):
    y, x = tile_coord
    tile = grid[y][x]
    # top
    if y > 0 and (y-1, x) not in visited and tile in "S|JL" and grid[y-1][x] in "|7F":
        visited.append((y-1, x))
        visit_next.append((y-1, x))
    # bottom
    if y < len(grid) - 1 and (y+1, x) not in visited and tile in "S|7F" and grid[y+1][x] in "|JL":
        visited.append((y+1, x))
        visit_next.append((y+1, x))
    # left
    if x > 0 and (y, x-1) not in visited and tile in "S-J7" and grid[y][x-1] in "-LF":
        visited.append((y, x-1))
        visit_next.append((y, x-1))
    # right
    if x < len(grid[0]) - 1 and (y, x+1) not in visited and tile in "S-LF" and grid[y][x+1] in "-J7":
        visited.append((y, x+1))
        visit_next.append((y, x+1))


while visit_next:
    get_connections(visit_next.pop())

print("Pipe length: ", len(visited))
print("Ans: ", len(visited) // 2)
