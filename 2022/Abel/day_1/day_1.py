# get data and parse it into nested list
with open('data.txt') as f:
    data = []
    l = []
    for line in f:
        if line != '\n':
            l.append(int(line.strip()))
        else:
            data.append(l)
            l = []

# PART 1
# figure out the elf with the most calories
max_calories = 0
for elf in data:
    max_calories = max(max_calories, sum(elf))

print(max_calories)


# PART 2
# sort the data highest to lowest by sum of internal lists
data.sort(key=sum, reverse=True)

# flatten the top three entries of data into one list and print
top_three = [item for l in data[:3] for item in l]

print(sum(top_three))