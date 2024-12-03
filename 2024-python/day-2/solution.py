from typing import List
from aocd import get_data, submit

example = False
submitAns = False

if example:
    with open('example.txt') as f:
        input_data = f.read().splitlines()
else:
    input_data = get_data(day=2, year=2024).splitlines()

report = list(map(str.split, input_data))
report = [list(map(int, line)) for line in report]

gradient = []

for idx, data in enumerate(report):
    gradient.append([])
    for i in range(len(data)-1):
        first, second = data[i:i+2]
        gradient[idx].append(second - first)

# print(gradient)

def check_valid(data: List[int]) -> bool:
    cond_a = max(data) < 0 or min(data) > 0    # all negative or positive
    cond_b = 0 < max(list(map(abs, data))) < 4
    return cond_a and cond_b

def check_valid_b(data: List[int]) -> bool:
    for i in range(len(data)+1):
        modified_grad = data.copy()
        if i == 0:
            modified_grad = modified_grad[1:]
        elif i == len(data):
            modified_grad = modified_grad[:-1]
        else:
            diff = modified_grad.pop(i)
            modified_grad[i-1] += diff
        # print(modified_grad)
        if check_valid(modified_grad):
            return True
    return False

valid_a = list(map(check_valid, gradient))
# print(valid_a)
ans_a = sum(valid_a)
print('Part 1 Ans: ', ans_a)

ans_b = ans_a + sum([check_valid_b(data) for result, data in zip(valid_a, gradient) if not result])
print('Part 2 Ans: ', ans_b)

if submitAns and not example:
    submit(ans_a, part='a', year=2024, day=2)
    submit(ans_b, part='b', year=2024, day=2)