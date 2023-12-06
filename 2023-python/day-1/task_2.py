with open("input.txt") as f:
    inputs = f.readlines()

str_to_int_map = {
    "o" : [("one", "1e")],
    "t" : [("two", "2o"), ("three", "3e")],
    "f" : [("four", "4"), ("five", "5e")],
    "s" : [("six", "6"), ("seven", "7n")],
    "e" : [("eight", "8t")],
    "n" : [("nine", "9e")],
}


def translate_str_to_int(input: str) -> str:
    i = 0
    while i < len(input):
        try:
            leaves = str_to_int_map[input[i]]
            for leaf in leaves:
                if leaf[0] in input:
                    input = input.replace(*leaf)
        except KeyError:
            pass
        i += 1

    return input


for idx, input in enumerate(inputs):
    input = translate_str_to_int(input)
    # print(input)
    integers = [int(s) for s in list(input) if s.isdigit()]
    inputs[idx] = integers[0] * 10 + integers[-1]

print(sum(inputs))
