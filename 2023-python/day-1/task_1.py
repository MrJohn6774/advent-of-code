with open("input.txt") as f:
    inputs = f.readlines()

for idx, input in enumerate(inputs):
    integers = [int(s) for s in list(input) if s.isdigit()]
    inputs[idx] = integers[0] * 10 + integers[-1]

# print(inputs)
print(sum(inputs))