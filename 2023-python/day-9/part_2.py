with open('input.txt') as f:
    sequences = [list(map(int, line.split())) for line in f.read().splitlines()]

result = 0

for seq in sequences:
    seq_expanded = [seq]
    while any(el != 0 for el in seq_expanded[-1]):
        seq_expanded.append([current - prev for prev, current in zip(seq_expanded[-1], seq_expanded[-1][1:])])
    seq_expanded.reverse()

    first = 0
    for idx in range(1, len(seq_expanded)):
        first = seq_expanded[idx][0] - first

    result += first

print(result)
