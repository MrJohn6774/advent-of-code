import re
from aocd import get_data, submit

example = False
toSubmit = False and not example

if example:
    with open('example.txt') as f:
        data = f.read()
else:
    data = get_data(year=2024, day=3)

matches = re.finditer(r"mul\((\d+),(\d+)\)", data)
ans_a = 0

do_donts = re.finditer(r"do(?:n't)?\(\)", data)
next_do_donts = next(do_donts)
enable = True
ans_b = 0

for match in matches:
    ans_a += int(match.group(1)) * int(match.group(2))

    # part 2
    if next_do_donts and next_do_donts.span()[0] < match.span()[1]:
        enable = next_do_donts.group() == "do()"
        next_do_donts = next(do_donts, None)
    
    if enable:
        ans_b += int(match.group(1)) * int(match.group(2))

print("Ans 1: ", ans_a)  
print("Ans 2: ", ans_b)

if toSubmit:
    submit(ans_a, part='a', year=2024, day=3)
    submit(ans_b, part='b', year=2024, day=3)
