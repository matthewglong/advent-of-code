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

        self.proc_version = {
            9000: self.proc_step_9000, 9001: self.proc_step_9001}

        # Parse the unloading procedure
        raw_proc = d[partition+1:]
        self.proc = list(map(lambda x: re.findall(r'\d+', x), raw_proc))

    def proc_step_9000(self, command, stacks):
        for _ in range(int(command[0])):
            crate = stacks[command[1]].pop()
            stacks[command[2]].append(crate)

    def proc_step_9001(self, command, stacks):
        stacks[command[2]] += stacks[command[1]][-int(command[0]):]
        del stacks[command[1]][-int(command[0]):]

    def rearrange(self, stacks, proc):
        for command in self.proc:
            proc(command, stacks)

    def top_of_stacks(self, v):
        stacks = {k: [t for t in v]
                  for k, v in self.stacks.items()}  # Deep copy the data
        proc = self.proc_version[v]
        self.rearrange(stacks, proc)
        tops = ''.join([s[-1] for s in stacks.values() if len(s) > 0])
        print(f'Stack tops with the CrateMover {v} are {tops}')
        return tops


d = Day5()
d.top_of_stacks(9000)
d.top_of_stacks(9001)
