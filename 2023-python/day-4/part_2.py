with open("input.txt") as f:
    inputs = f.read().splitlines()

result = 0

for idx, card in enumerate(inputs):
    card = card.split(": ")
    card[1] = card[1].split(" | ")
    card[1][0] = [int(s) for s in card[1][0].split(" ") if s.isnumeric()]
    inputs[idx] = [int(s) for s in card[1][1].split(" ")
                   if s.isnumeric() and int(s) in card[1][0]]


def cal_card_score(idx: int) -> int:
    if isinstance(inputs[idx], int):
        return inputs[idx]
    if len(inputs[idx]) == 0:
        inputs[idx] = 1
        return 1

    inputs[idx] = 1 + sum([cal_card_score(idx+i)
                          for i in range(1, len(inputs[idx])+1)])
    return inputs[idx]


for idx in range(len(inputs)):
    result += cal_card_score(idx)

print(result)
