import math

with open("input.txt") as f:
    inputs = f.readlines()

results = 0

def calculate_power(game) -> int:
    minimum = [0, 0, 0]
    for each_set in game:
        for each_color in each_set:
            each_color = each_color.split(" ")
            each_color[0] = int(each_color[0])
            if (each_color[1] == "red" and each_color[0] > minimum[0]):
                minimum[0] = each_color[0]
            if (each_color[1] == "green" and each_color[0] > minimum[1]):
                minimum[1] = each_color[0]
            if (each_color[1] == "blue" and each_color[0] > minimum[2]):
                minimum[2] = each_color[0]

    return math.prod(minimum)


for inp in inputs:
    inp = inp.split(": ")
    inp[1] = [each_set.split(", ") for each_set in inp[1].strip().split("; ")]

    results += calculate_power(inp[1])

print(results)
