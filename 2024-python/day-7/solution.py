from itertools import product
import time
from aocd import get_data, submit

use_example = False
submit_ans = False and not use_example

if use_example:
    with open('example.txt') as f:
        inputs = f.read().splitlines()
else:
    inputs = get_data(year=2024, day=7).splitlines()

data = []
for line in inputs:
    line = line.split(':')
    target, nums = line
    nums = list(map(int, nums.split()))
    data.append((int(target), nums))

ans_a = 0

for target, nums in data:
    for exp in range(2**(len(nums)-1)):
        result = int(nums[0])
        for i in range(1, len(nums)):
            if ((exp >> (i-1)) & 1):
                result *= nums[i]
            else:
                result += nums[i]
        if result == target:
            ans_a += target
            break

print('Part 1: ', ans_a)

start_time = time.time()
ans_b = 0

for target, nums in data:
    operations = list(product(range(3), repeat=len(nums) - 1))
    for ops in operations:
        result = nums[0]
        for i, op in enumerate(ops):
            match op:
                case 0:
                    result *= nums[i + 1]
                case 1:
                    result += nums[i + 1]
                case 2:
                    # result = int(f"{result}{nums[i + 1]}")
                    next_num = nums[i + 1]
                    factor = 1
                    while next_num >= factor:
                        factor *= 10
                    result = result * factor + next_num
        if result == target:
            ans_b += target
            break

end_time = time.time()
print('Part 2: ', ans_b)
print('Part 2 exec time: ', end_time-start_time, 's')

if submit_ans:
    submit(ans_a, part='a', year=2024, day=7)
    submit(ans_b, part='b', year=2024, day=7)