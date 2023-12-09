with open("input.txt") as f:
    inputs = f.read().splitlines()

# parse inputs
seeds = [int(s) for s in inputs[0].split(": ")[1].split()]
seeds = [range(seeds[i], seeds[i] + seeds[i+1])
         for i in range(0, len(seeds), 2)]
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


# return (converted_list, not_converted_list)
def convert(dest_start: int, src_start: int, size: int, convertee_range: range) -> (list, list):
    intersection_start = max(convertee_range.start, src_start)
    intersection_end = min(convertee_range.stop, src_start+size)
    if intersection_start < intersection_end:
        not_in_range = []
        converted = [range(intersection_start - src_start + dest_start,
                           intersection_end - src_start + dest_start)]
        if convertee_range.start < src_start:
            not_in_range.append(range(convertee_range.start, src_start))
        if convertee_range.stop > src_start+size:
            not_in_range.append(range(src_start+size, convertee_range.stop))
        return (converted, not_in_range)
    else:
        return ([], [])


for current_map in maps:
    # store and isolate converted range
    converted_range = []
    ignore_range = []
    for params in current_map:
        for seed_range in seeds:
            # ignore range that are already converted
            if seed_range not in ignore_range:
                (converted, not_converted) = convert(*params, seed_range)
                if converted:
                    ignore_range.append(seed_range)
                    # add non-converted range back into seeds
                    seeds += not_converted
                    # store converted range to a new list so that it won't be affected by next set of params
                    converted_range += converted

    # remove all converted range so that there are only non-converted range
    [seeds.remove(seed) for seed in ignore_range]
    # merge all converted and non-converted range
    seeds = converted_range + seeds

print(min([seed_range.start for seed_range in seeds]))
