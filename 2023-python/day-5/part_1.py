with open("input.txt") as f:
    inputs = f.read().splitlines()

# parse inputs
seeds = [int(s) for s in inputs[0].split(": ")[1].split()]
maps = []
current_map = []

for line in inputs[3:]:
    if ":" in line:
        maps.append(current_map)
        current_map = []
    elif line.strip():
        current_map.append(tuple(map(int, line.split())))
if current_map:
    maps.append(current_map)


def convert(dest_start: int, src_start: int, size: int, convertee: int) -> int:
    if convertee in range(src_start, src_start + size):
        # convert it to negative so that it won't be affected by next set of params in the same map
        return -(convertee - src_start + dest_start)
    else:
        return convertee


for current_map in maps:
    for params in current_map:
        seeds = [convert(*params, seed) for seed in seeds]
    seeds = [abs(seed) for seed in seeds]

print(min(seeds))
