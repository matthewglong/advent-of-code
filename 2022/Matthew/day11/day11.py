# %%
import re
import math


class Day11:
    def __init__(self):
        regex = re.compile(
            r'Monkey (\d*):\n  Starting items: ([0-9 ,]*)\n  Operation: new = old (\+|\*) (old|\d*)\n  Test: divisible by (\d*)\n    If true: throw to monkey (\d*)\n    If false: throw to monkey (\d*)', re.M)
        with open('day11.txt', 'r') as f:
            monkeys = {}
            i = 0
            mod = 1
            for raw_info in f.read().split('\n\n'):
                self.curr = raw_info
                i += 1
                info = regex.search(raw_info).groups()
                m = Monkey(info)
                monkeys[m.name] = m
                mod *= m.test_num
        self.monkeys = monkeys
        self.mod = mod

    def echo_monkeys(self, round):
        if round:
            print(f'\nROUND {round}')
        for _, v in self.monkeys.items():
            print(v, v.items)

    def parse_monkey(self, monkey, worry_reduction):
        for item in monkey.items:
            monkey.items_inspected += 1
            worry = monkey.inspect(item)
            if worry_reduction:
                reduced_worry = worry // worry_reduction
            else:
                reduced_worry = worry % self.mod
            if reduced_worry % monkey.test_num == 0:
                self.monkeys[monkey.true_monkey].items.append(reduced_worry)
            else:
                self.monkeys[monkey.false_monkey].items.append(reduced_worry)
            monkey.items = []

    def parse_monkeys(self, worry_reduction):
        for _, monkey in self.monkeys.items():
            self.parse_monkey(monkey, worry_reduction)

    def monkeying_around(self, rounds=20, top_n=2, worry_reduction=None, test_points=None):
        for i in range(rounds):
            if test_points:
                if i in test_points:
                    self.echo_monkeys(i)
            self.parse_monkeys(worry_reduction=worry_reduction)
            i += 1
        if test_points:
            if i in test_points:
                self.echo_monkeys(i)

        inspections = [m.items_inspected for _, m in self.monkeys.items()]
        out = 1
        for num in sorted(inspections)[-top_n:]:
            out *= num
        print(f"Monkeying around value: {out}")


class Monkey:
    def __init__(self, details):
        self.name, start, operation, opp_num, test_num, self.true_monkey, self.false_monkey = details
        self.items = list(map(int, start.split(', ')))
        self.opp_num = opp_num
        self.test_num = int(test_num)
        self.opp_label = operation
        self.items_inspected = 0

        if operation == '*':
            self.operation = lambda x, y: x*y
        elif operation == '+':
            self.operation = lambda x, y: x+y
        else:
            raise ValueError(f"Unknown operation '{operation}'")

        if opp_num == 'old':
            self.inspect = self.inspect_item_old
        else:
            self.opp_num = int(self.opp_num)
            self.inspect = self.inspect_item_self

    def __repr__(self):
        return f'Monkey {self.name} inspected {self.items_inspected} items'

    def inspect_item_old(self, item):
        return self.operation(item, item)

    def inspect_item_self(self, item):
        return self.operation(item, self.opp_num)


# %%
d = Day11()
d.monkeying_around(rounds=20, worry_reduction=3)

d = Day11()
d.monkeying_around(rounds=10_000, test_points=(1, 10_000))
