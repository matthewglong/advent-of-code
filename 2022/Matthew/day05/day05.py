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
        self.stacks = {s[-1]: list(''.join(s[:-1]).strip()[::-1])
                       for s in decrufted}

        # Parse the unloading procedure
        raw_proc = d[partition+1:]
        self.proc = list(map(lambda x: re.findall(r'\d+', x), raw_proc))

    def proc_step(self, command):
        for _ in range(int(command[0])):
            crate = self.stacks[command[1]].pop()
            self.stacks[command[2]].append(crate)

    def rearrange(self):
        for command in self.proc:
            self.proc_step(command)

    def top_of_stacks(self):
        self.rearrange()
        tops = ''.join([s[-1] for s in self.stacks.values()])
        print(f'Stack tops are {tops}')
        return tops


# %%
d = Day5()
d.top_of_stacks()
# %%
