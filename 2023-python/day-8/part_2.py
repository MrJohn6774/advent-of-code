import re
import math

with open("input.txt") as f:
    lines = f.read().splitlines()

directions = [0 if char == 'L' else 1 for char in lines[0]]
nodes = {}
for lines in lines[2:]:
    lines = lines.split(" = ")
    nodes[lines[0]] = re.findall(r'[A-Z]+', lines[1])

starting_nodes = [node for node in nodes.keys() if node[2] == 'A']
steps = []

for starting_node in starting_nodes:
    reached = False
    current_node = starting_node
    step = 0
    while not reached:
        for direction in directions:
            step += 1
            if nodes[current_node][direction][2] == 'Z':
                reached = True
                break
            current_node = nodes[current_node][direction]
    steps.append(step)

print(steps)
print(math.lcm(*steps))
