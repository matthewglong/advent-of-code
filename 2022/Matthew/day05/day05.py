# %%
import re


class Day5:
    def __init__(self):
        with open('day05.txt', 'r') as f:
            d = f.read().splitlines()

        # Find separator between 2 data inputs
        partition = d.index('')

        # Parse the cargo stacks
        raw_stacks = d[:partition]
        transposed = list(zip(*raw_stacks))
        decrufted = transposed[1::4]
        self.stacks = {s[-1]: ''.join(s[:-1]).strip() for s in decrufted}

        # Parse the unloading procedure
        raw_proc = d[partition+1:]
        self.proc = list(map(lambda x: re.findall(r'\d+', x), raw_proc))
