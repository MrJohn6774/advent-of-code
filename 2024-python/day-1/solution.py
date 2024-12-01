from aocd import get_data, submit
from bisect import bisect_left, bisect_right

# with open('example.txt') as f:
#     inputs = f.read().splitlines()

inputs = get_data(day=1, year=2024).strip().splitlines()

list_a, list_b = [], []
for line in inputs:
    a, b = line.split()
    list_a.append(int(a))
    list_b.append(int(b))

list_a.sort()
list_b.sort()
ans = 0

for a, b in zip(list_a, list_b):
    ans += abs(a-b)

print(ans)
# submit(ans, part='a', day=1, year=2024)

ans = 0

for a in list_a:
    # ans += a * len([i for i in list_b if i == a])    # O(n^2)
    ans += a * (bisect_right(list_b, a) - bisect_left(list_b, a))    # O(nlogn)

print(ans)
# submit(ans, part='b', day=1, year=2024)
