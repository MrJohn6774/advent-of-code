with open("input.txt") as f:
    hands = [tuple(line.split()) for line in f.read().splitlines()]

card_value = [str(i) for i in range(2, 10)] + ['T', 'J', 'Q', 'K', 'A']


def cal_strength(hand: list[str]) -> int:
    total_value = 0
    combo_value = 0
    for idx in range(len(hand) - 1):
        if hand[idx] == hand[idx+1]:
            combo_value += 1
            total_value += combo_value
        else:
            combo_value = 0
    return total_value


def right_is_greater_than_left(left: str, right: str) -> bool:
    left_type = cal_strength(sorted(left))
    right_type = cal_strength(sorted(right))

    if right_type > left_type:
        return True
    # compare card face values if same types
    if right_type == left_type:
        for left_card, right_card in zip(left, right):
            if card_value.index(right_card) > card_value.index(left_card):
                return True
            elif card_value.index(right_card) < card_value.index(left_card):
                return False

    return False


def merge_sort(hands: list):
    if len(hands) <= 1:
        return hands

    mid = len(hands) // 2
    left_half = hands[:mid]
    right_half = hands[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if right_is_greater_than_left(left_half[i][0], right_half[j][0]):
            hands[k] = left_half[i]
            i += 1
        else:
            hands[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        hands[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        hands[k] = right_half[j]
        j += 1
        k += 1


merge_sort(hands)

result = 0
for idx, (_, bid) in enumerate(hands):
    result += (idx + 1) * int(bid)

# print(hands)
print(result)
