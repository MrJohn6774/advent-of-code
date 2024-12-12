from functools import cmp_to_key
from aocd import get_data, submit

use_example = False
submit_ans = False and not use_example

if use_example:
    with open('example.txt') as f:
        rules, orders = f.read().split('\n\n')
else:
    rules, orders = get_data(year=2024, day=5).split('\n\n')

rules = [(int(line.split('|')[0]), int(line.split('|')[1])) for line in rules.splitlines()]
orders = [list(map(int, line.split(','))) for line in orders.splitlines()]

ans_a = ans_b = 0

def compare(a: int, b: int):
    for rule in rules:
        if (a, b) == rule:
            return -1
        elif (b, a) == rule:
            return 1
    return 0

for order in orders:
    sorted_order = sorted(order, key=cmp_to_key(compare))
    if order == sorted_order:
        # print(order, order[len(order)//2])
        ans_a += order[len(order)//2]
    else:
        ans_b += sorted_order[len(order)//2]

print(ans_a)
print(ans_b)

if submit_ans:
    submit(ans_a, part='a', year=2024, day=5)
    submit(ans_b, part='b', year=2024, day=5)
