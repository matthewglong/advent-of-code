with open("input.txt", "r") as f:
    d = {}
    for line in f.readlines():
        line = line.split("-")
        d[int(line[0])] = "open"
        d[int(line[1])] = "close"

sorted_keys = sorted(d.keys())
print(sorted_keys)

open_counter = 0
close_counter = 0
prev = sorted_keys[0]
total = 0
for i, key in enumerate(sorted_keys):
    if d[key] == "open":
        open_counter += 1
    if d[key] == "close":
        close_counter += 1
    
    if open_counter == close_counter:
        print("outside interval")
        print(f"beginning: {prev}")
        print(f"end: {key}")
        total += key - prev + 1
        if i+1 < len(sorted_keys):
            prev = sorted_keys[i+1]

print(total)