# %%
with open('data.txt') as f:
    data = []
    for line in f:
        line = line.rstrip()
        partition = int(len(line)/2)
        compartment_1 = set(list(line[:partition]))
        compartment_2 = set(list(line[partition:]))
        data.append([compartment_1, compartment_2])

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

total = 0
for bag in data:
    item = bag[0].intersection(bag[1]).pop()
    score = alphabet.index(item) + 1
    total += score
print(total)

total = 0
for index in range(0, len(data), 3):
    rucksack_1 = data[index][0].union(data[index][1])
    rucksack_2 = data[index + 1][0].union(data[index + 1][1])
    rucksack_3 = data[index + 2][0].union(data[index + 2][1])
    badge = rucksack_1.intersection(rucksack_2, rucksack_3).pop()
    score = alphabet.index(badge) + 1
    total += score
print(total)
