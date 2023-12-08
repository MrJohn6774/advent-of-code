import math

with open("input.txt") as f:
    inputs = f.read().splitlines()

result = 0

for card in inputs:
    card = card.split(": ")
    card[1] = card[1].split(" | ")
    card[1][0] = [int(s) for s in card[1][0].split(" ") if s.isnumeric()]
    card[1][1] = [int(s) for s in card[1][1].split(" ") if s.isnumeric() and int(s) in card[1][0]]

    if len(card[1][1]) > 0:
        result += math.pow(2, len(card[1][1]) - 1)

print(int(result))
