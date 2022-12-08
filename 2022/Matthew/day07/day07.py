class Day7:
    def __init__(self):
        with open('day07.txt', 'r') as f:
            self.raw_data = f.read()
        self.parse_data()
        self.file_system_size = 70000000
        self.storage_space = self.file_system_size - self.shell.wd.size

    def parse_data(self):
        s = Shell()
        for raw_command in self.raw_data.split('$ '):
            command_type = raw_command[:2]
            if command_type == 'cd':
                command = raw_command.strip().split()[-1]
                s.cd(command)
            elif command_type == 'ls':
                for item in raw_command.split('\n')[1:-1]:
                    elements = item.split()
                    if item[:3] == 'dir':
                        name = elements[-1]
                        s.mkdir(name)
                    else:
                        size_text, name = elements
                        s.touch(name, int(size_text))
        s.cd('/')
        self.shell = s
        return s

    def sum_dir_sizes(self, max_size):
        sizes = [d.size for d in self.shell.ls_dir_r() if d.size <= max_size]
        total = sum(sizes)
        print(f'Total of dir size respecting a {max_size} max: {total}')
        return total

    def smallest_dir(self, required_space=30000000):
        self.shell.cd('/')
        space_needed = required_space - self.storage_space
        sizes = [d.size for d in self.shell.ls_dir_r() if d.size >=
                 space_needed]
        best_candidate = min(sizes)
        print(
            f'The best candidate for delation, based on a {space_needed} space requirement, is {best_candidate}')
        return best_candidate


class Shell:
    def __init__(self):
        self.root = Directory('/')
        self.wd = self.root

    def cd(self, loc):
        if loc == '..':
            self.wd = self.wd.parent
        elif loc == '/':
            self.wd = self.root
        else:
            self.wd = self.wd.contents[loc]

    def mkdir(self, name):
        dir = Directory(name, parent=self.wd)
        self.wd.contents[name] = dir

    def touch(self, name, size):
        file = File(name, size, parent=self.wd)
        self.wd.contents[name] = file

    def ls(self):
        for _, v in self.wd.contents.items():
            print(v)

    def ls_dir_r(self):
        flat = []

        def do(wd):
            for i in wd.contents.values():
                if type(i) == Directory:
                    flat.append(i)
                    do(i)
        do(self.wd)
        return flat


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.contents = {}
        self.size = 0

    def __repr__(self):
        return f'{self.name} (dir, size={self.size})'


class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.parent = parent
        self.size = size
        p = parent
        while p:
            p.size += size
            p = p.parent

    def __repr__(self):
        return f'{self.name} (file, size={self.size})'


d = Day7()
d.sum_dir_sizes(max_size=100_000)
d.smallest_dir(required_space=30_000_000)
