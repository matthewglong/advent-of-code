class Day6:
    def __init__(self):
        with open('day06.txt', 'r') as f:
            self.datastream = f.read().strip()

    def find_marker(self, size=4):
        count = size
        marker = self.datastream[:size]
        remaining_data = self.datastream[size:]
        for char in remaining_data:
            if len(set(marker)) == size:
                print(f'{marker} @ {count} for a {size} char marker')
                return marker, count
            else:
                marker = marker[1:] + char
                count += 1
        print('No markers found')
        return None, -1


d = Day6()
d.find_marker(4)
d.find_marker(14)
