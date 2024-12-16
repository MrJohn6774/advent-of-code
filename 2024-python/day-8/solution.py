import re
from aocd import get_data, submit

use_example = False
submit_ans = False and not use_example

if use_example:
    with open('example.txt') as f:
        data = f.read()
else:
    data = get_data(year=2024, day=8)

width = data.find('\n')
height = data.count('\n') + 1

antinodes = set()
antinodes_2 = set()
antennas = {}
ans_b = 0

for attenna in re.finditer(r'[^.\n]', data):
    char = attenna.group()
    start, _ = attenna.span()
    x = start % (width + 1)    # +1 to account for \n char
    y = (start) // (width + 1)

    if char not in antennas:
        antennas[char] = [(x, y)]
        continue

    # calculate antinodes (part 1)
    for antt in antennas[char]:
        dx, dy = x - antt[0], y - antt[1]
        if 0 <= x + dx < width and 0 <= y + dy < height:
            antinodes.add((x + dx, y + dy))
        if 0 <= antt[0] - dx < width and 0 <= antt[1] - dy < height:
            antinodes.add((antt[0] - dx, antt[1] - dy))
    
    # calculate antinodes (part 2)
    for antt in antennas[char]:
        dx, dy = x - antt[0], y - antt[1]
        x_1, y_1 = x, y
        x_2, y_2 = antt
        while 0 <= x_1 + dx < width and 0 <= y_1 + dy < height:
            x_1, y_1 = x_1 + dx, y_1 + dy
            antinodes_2.add((x_1, y_1))
        while 0 <= x_2 - dx < width and 0 <= y_2 - dy < height:
            x_2, y_2 = x_2 - dx, y_2 - dy
            antinodes_2.add((x_2, y_2))

    antennas[char].append((x, y))

# print(antennas)
# print(antinodes)

ans_a = len(antinodes)
print('Part 1: ', ans_a)

flattened_antennas = [coord for coords in antennas.values() for coord in coords]
antinodes_2.update(flattened_antennas)

ans_b += len(antinodes_2)
print('Part 2: ', ans_b)

if submit_ans:
    submit(ans_a, part='a', year=2024, day=8)
    submit(ans_b, part='b', year=2024, day=8)
