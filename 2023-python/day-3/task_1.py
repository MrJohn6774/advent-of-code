import re

with open("input.txt") as f:
    inputs = f.read().splitlines()

height = len(inputs)
result = 0


def extract_digit(x: int, y: int) -> int:
    if y < 0 or y >= height:
        return 0

    found = 0

    for match in re.finditer(r"\d+", inputs[y]):
        if abs(match.start() - x) < 2 or abs(match.end() - 1 - x) < 2:
            found += int(inputs[y][match.start():match.end()])

    return found


for y, line in enumerate(inputs):
    for x, char in enumerate(line):
        if not (char.isdigit() or char == '.'):
            result += sum([extract_digit(x, y-1+j) for j in range(3)])

print(result)
