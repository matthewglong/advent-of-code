data = '94651298688456123161881394547336912458971234908712398471928347923847298376'
data2 = '12345654321'
cleaned = list(map(int, list(data)))
counter = 0


class TreeCounter():
    def __init__(self):
        with open('data.txt', 'r') as f:
            self.data = list(map(lambda x: list(map(int, list(x))), f.read().splitlines()))

    def count_visible(self, trees, indices):
        finished = True
        to_remove = []
        for idx in range(1, len(trees) - 1):
            if trees[idx] <= trees[idx - 1] and trees[idx] <= trees[idx + 1]:
                to_remove.append(idx)
                finished = False
        for i in sorted(to_remove, reverse=True):
            del trees[i]
            indices.pop(i)
        if finished:
            return trees, indices
        return self.count_visible(trees, indices)

    def get_visible_trees(self):
        trees = []
        inverted_data = list(map(list, zip(*self.data)))
        print(inverted_data[0])
        for idx, row in enumerate(inverted_data):
            t, i = self.count_visible(row, list(range(len(row))))
            trees += list(map(lambda x: (idx, x), i))
        print(len(trees))
        for idx, row in enumerate(self.data):
            t, i = self.count_visible(row, list(range(len(row))))
            trees += list(map(lambda x: (x, idx), i))
        print(len(trees))
        print(len(list(set(trees))))
        return len(list(set(trees)))


tc = TreeCounter()
print(tc.data)
#tc.count_visible(cleaned, list(range(len(cleaned))))
tc.get_visible_trees()