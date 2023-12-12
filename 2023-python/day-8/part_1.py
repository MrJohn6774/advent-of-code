import re

with open("input.txt") as f:
    lines = f.read().splitlines()

directions = [0 if char == 'L' else 1 for char in lines[0]]
nodes = {}
for lines in lines[2:]:
    lines = lines.split(" = ")
    nodes[lines[0]] = re.findall(r'[A-Z]+', lines[1])

reached = False
current_node = "AAA"
steps = 0

while not reached:
    for direction in directions:
        steps += 1
        if nodes[current_node][direction] == "ZZZ":
            reached = True
            break
        current_node = nodes[current_node][direction]

print(steps)
