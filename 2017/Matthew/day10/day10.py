# %%
import numpy as np


class Day10:
    def __init__(self):
        with open('day10.txt', 'r') as f:
            r = f.read().strip()
            result = r.split(',')
        self.lengths = list(map(int, result))
        extra_ascii = [17, 31, 73, 47, 23]
        self.ascii_lengths = list(map(ord, r)) + extra_ascii
        self.num_marks = 256
        self.bracelet = list(range(self.num_marks))
        self.position = 0
        self.skip_size = 0

    def reset(self):
        self.bracelet = list(range(self.num_marks))
        self.position = 0
        self.skip_size = 0

    def swaparoo(self, start, length):
        stop = (start + length) % self.num_marks
        if start > stop:
            right = self.bracelet[start:]
            left = self.bracelet[:stop]
            right_size = len(right)
            left_size = len(left)
            slice = right + left
            slice.reverse()
            self.bracelet[:left_size] = slice[-left_size:]
            self.bracelet[-right_size:] = slice[:right_size]

        else:
            slice = self.bracelet[start:stop]
            slice.reverse()
            self.bracelet[start:stop] = slice

    def scramble(self, lengths):
        for length in lengths:
            self.swaparoo(self.position, length)
            self.position = (self.position + self.skip_size +
                             length) % self.num_marks
            self.skip_size += 1
        return

    def p1(self, n_prod=2):
        self.reset()
        self.scramble(self.lengths)
        answer = HelperFunc.prod(self.bracelet[:n_prod])
        print(f"Product of first two elements is: {answer}")
        return answer

    # SOMETHING IS WRONG WITH PART 2!!!
    def p2(self, loops=64):
        self.reset()
        for _ in range(loops):
            self.scramble(self.ascii_lengths)

        sparse_hash = [self.bracelet[i:i+16]
                       for i in range(0, self.num_marks, 16)]

        dense_hash = [HelperFunc.xor(chunk) for chunk in sparse_hash]

        hex = HelperFunc.mega_hex(dense_hash)
        print(f"The ASCII hex is: {hex}")
        return hex


class HelperFunc:
    def prod(l: list) -> int:
        p = 1
        for i in l:
            p *= i
        return p

    def xor(l: list) -> int:
        r = l[0]
        for i in l[1:]:
            r = r ^ i
        return r

    def mega_hex(l: list) -> str:
        hl = ["{:02x}".format(i) for i in l]
        f = ''.join(hl)
        return f


# %%
d = Day10()
d.p1()
test1 = d.bracelet

# %%
d.p2(1)
print(test1 == d.bracelet)
# %%
d.ascii_lengths
# %%
for i in range(0, 255):
    print("{:02x}".format(i))
# %%
len('0b3041e21b09681f9d8df545ad3402c5')
# %%
