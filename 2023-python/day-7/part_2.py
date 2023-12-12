with open("input.txt") as f:
    hands = [tuple(line.split()) for line in f.read().splitlines()]

card_value = ['J'] + [str(i) for i in range(2, 10)] + ['T', 'Q', 'K', 'A']


def cal_strength(hand: list[str]) -> int:
    # create frequency map
    freq = {}
    for card in hand:
        if card in freq:
            freq[card] += 1
        else:
            freq[card] = 1
    if 'J' in freq:
        joker_count = freq.pop('J')
        max_count = max(freq.values()) if len(freq) else 0
        # add 'J' count to the largest card count
        if max_count >= joker_count:
            freq[max(freq, key=freq.get)] += joker_count
        else:
            if len(freq):
                freq.pop(max(freq, key=freq.get))
            freq['J'] = joker_count + max_count

    return sum([3**(count) for count in freq.values() if count > 1])


def right_is_greater_than_left(left: str, right: str) -> bool:
    left_type = cal_strength(left)
    right_type = cal_strength(right)

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
