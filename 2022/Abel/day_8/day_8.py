import numpy as np


data = '94651298688456123161881394547336912458971234908712398471928347923847298376'
data2 = '12345654321'
cleaned = list(map(int, list(data)))
print(cleaned)
counter = 0

class TreeCounter():
    def __init__(self):
        with open('data.txt', 'r') as f:
            list(map(lambda x: list(map(int, list(x))), f.readlines()))

def count_visible(trees, counter):
    counter += 1
    finished = True
    to_remove = []
    for idx in range(1, len(trees) - 1):
        if trees[idx] <= trees[idx - 1] and trees[idx] <= trees[idx + 1]:
            to_remove.append(idx)
            finished = False
    for i in sorted(to_remove, reverse=True):
        del trees[i]
    if finished:
        return trees, counter
    return count_visible(trees, counter)

iterations = []

for _ in range(100):
    randomlist = list(np.random.choice(range(1, 10), 1000, replace=True))
    visible_trees, c = count_visible(randomlist, 0)
    iterations.append(c)

print(max(iterations))