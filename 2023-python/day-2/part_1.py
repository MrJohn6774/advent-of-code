with open("input.txt") as f:
    inputs = f.readlines()

MAX = [12, 13, 14]
results = 0

def is_within_bounds(sets) -> bool:
    for each_set in sets:
        for each_color in each_set:
            each_color = each_color.split(" ")
            if ((each_color[1] == "red" and int(each_color[0]) > MAX[0])
                or
                (each_color[1] == "green" and int(each_color[0]) > MAX[1])
                or
                (each_color[1] == "blue" and int(each_color[0]) > MAX[2])):
                return False
    return True


for inp in inputs:
    inp = inp.split(": ")
    inp[1] = [each_set.split(", ") for each_set in inp[1].strip().split("; ")]

    if is_within_bounds(inp[1]):
        results += int(inp[0].split(" ")[1])


print(results)
