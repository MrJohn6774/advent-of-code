import re
import math

with open("input.txt") as f:
    inputs = f.read().splitlines()

height = len(inputs)
result = 0


def extract_digit(x: int, y: int) -> list:
    if y < 0 or y >= height:
        return []

    found = []

    for match in re.finditer(r"\d+", inputs[y]):
        if abs(match.start() - x) < 2 or abs(match.end() - 1 - x) < 2:
            found.append(int(inputs[y][match.start():match.end()]))

    return found


for y, line in enumerate(inputs):
    for x, char in enumerate(line):
        if char == '*':
            extracted_digits = []
            for j in range(3):
                extracted_digits += extract_digit(x, y-1+j)
            if len(extracted_digits) == 2:
                result += math.prod(extracted_digits)

print(result)
