from aocd import get_data, submit

use_example = False
submit_ans = False and not use_example

if use_example:
    with open('example.txt') as f:
        data = f.read()
else:
    data = get_data(year=2024, day=9)

spaces = []
nums = []

for idx, value in enumerate(data):
    (spaces if idx % 2 else nums).append(int(value))

assert(len(spaces) + 1 == len(nums))

if use_example:
    print(spaces, len(spaces))
    print(nums, len(nums))

ans_a = 0
right_idx = len(nums) - 1
arr_pos = 0

for (left_idx, num_amount), sp_amount in zip(enumerate(nums), spaces):
    if num_amount == 0:
        break

    ans_a += sum([multiplier * left_idx for multiplier in range(arr_pos, arr_pos+num_amount)])
    arr_pos += num_amount

    # move rightmost elements to spaces
    while sp_amount > 0 and left_idx < right_idx:
        move_amount = min(sp_amount, nums[right_idx])
        sp_amount -= move_amount
        nums[right_idx] -= move_amount

        ans_a += sum([multiplier * right_idx for multiplier in range(arr_pos, arr_pos+move_amount)])
        arr_pos += move_amount

        # move right_idx when all rightmost elements are moved
        if nums[right_idx] < 1:
            right_idx -= 1


print('Part 1: ', ans_a)

ans_b = 0




if submit_ans:
    # submit(ans_a, part='a', year=2024, day=9)
    submit(ans_b, part='b', year=2024, day=9)
