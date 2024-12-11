from aocd import get_data, submit

use_example = False
submit_ans = False and not use_example

if use_example:
    with open('example.txt') as f:
        data = f.read().splitlines()
else:
    data = get_data(year=2024, day=4).splitlines()

ans_a = 0
ans_b = 0


def search_xmas(x_X: int, y_X: int) -> int:
    result = 0
    for direction in [(-1, 1), (1, 1), (-1, -1), (1, -1), (-1, 0), (1, 0), (0, -1), (0, 1)]:
        matches = 0
        dx, dy = direction
        n_x, n_y = x_X, y_X

        for needle in 'MAS':
            n_x += dx
            n_y += dy
            if n_x < 0 or n_y < 0 or n_x >= len(data[0]) or n_y >= len(data):
                break
            if needle != data[n_y][n_x]:
                break
            matches += 1

        result += matches // 3

    return result


def search_diagonal(x_A: int, y_A: int) -> int:
    result = 0
    for direction in [(-1, -1), (-1, 1)]:
        dx, dy = direction
        if x_A < 1 or y_A < 1 or x_A >= len(data[0])-1 or y_A >= len(data)-1:
            break
        if data[y_A + dy][x_A + dx] == 'M' and data[y_A - dy][x_A - dx] == 'S':
            result += 1
        elif data[y_A + dy][x_A + dx] == 'S' and data[y_A - dy][x_A - dx] == 'M':
            result += 1
    return result // 2

for y, line in enumerate(data):
    for x, ch in enumerate(line):
        if ch == 'X':
            ans_a += search_xmas(x, y)
        if ch == 'A':
            ans_b += search_diagonal(x, y)

print('Part 1: ', ans_a)
print('Part 2: ', ans_b)

if submit_ans:
    submit(ans_a, part='a', year=2024, day=4)
    submit(ans_b, part='b', year=2024, day=4)
