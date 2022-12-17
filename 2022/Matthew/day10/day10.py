# %%
class Day10:
    def __init__(self):
        with open('day10.txt', 'r') as f:
            self.data = [Command(l) for l in f]

    def run_display(self):
        X = 1
        display = ''
        cycle = pixel = 0
        strength = 0
        curr_interest = 20
        interest_step = 40
        for c in self.data:
            for _ in range(c.period):
                cycle += 1
                if X-1 <= pixel <= X+1:
                    display += 'O'
                else:
                    display += ' '
                pixel += 1
                if cycle % interest_step == 0:
                    display += '\n'
                    pixel = 0
                if cycle == curr_interest:
                    strength += X * curr_interest
                    curr_interest += interest_step
            X += c.increase
        print(f'This signal strength is {strength}\n')
        print(display)


class Command:
    def __init__(self, line):
        l = line.split()
        self.name = line
        if len(l) == 2:
            self.period = 2
            self.increase = int(l[1])
        else:
            self.period = 1
            self.increase = 0

    def __repr__(self):
        return self.name


d = Day10()
d.run_display()
