import math

with open("input.txt") as f:
    races = list(zip(*[map(int, line.split(": ")[1].strip().split()) for line in f.readlines()]))

result = 1

for (T, D) in races:
    det_sqrt = math.sqrt(T**2 - 4 * D)
    lower_bound = math.ceil(0.5 * (T - det_sqrt))
    upper_bound = math.floor(0.5 * (T + det_sqrt))
    if det_sqrt - math.floor(det_sqrt) < 1e-5:
        lower_bound += 1
        upper_bound -= 1

    print(lower_bound, upper_bound)
    result *= upper_bound - lower_bound + 1

print(result)
