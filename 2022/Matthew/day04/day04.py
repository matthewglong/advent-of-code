import re


class Day4:
    def __init__(self):
        self.full_overlap = 0
        self.partial_overlap = 0
        with open('day04.txt', 'r') as f:
            self.pairs = list(map(self.convert, f.read().splitlines()))

    def parse_pair(self, line):
        return list(map(int, re.split('-|,', line)))

    def convert(self, line):
        pair = self.parse_pair(line)
        if ((pair[0] <= pair[2]) & (pair[1] >= pair[3])) | ((pair[0] >= pair[2]) & (pair[1] <= pair[3])):
            self.full_overlap += 1
        if (pair[0] <= pair[3]) & (pair[1] >= pair[2]):
            self.partial_overlap += 1
        return pair

    # The following two methods are silly
    def get_full_overlap(self):
        print(f"The number of full overlaps is {self.full_overlap}")
        return self.full_overlap

    def get_partial_overlap(self):
        print(f"The number of partial overlaps is {self.partial_overlap}")
        return self.partial_overlap


d = Day4()
d.get_full_overlap()
d.get_partial_overlap()
