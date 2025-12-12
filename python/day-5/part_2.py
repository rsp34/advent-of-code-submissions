def add_unique_ranges(existing_ranges:list[range],new_range:range):
    ranges_to_add = []
    for r in existing_ranges:
        if new_range.start < r.start and new_range.stop > r.start:
            ranges_to_add.append(range(new_range.start,r.start))
            new_range = range(r.stop,new_range.stop)
    
            
    if new_range.start < new_range.stop:
        ranges_to_add.append(new_range)

    existing_ranges += ranges_to_add
    existing_ranges.sort(key = lambda x: x.start)


with open("./python/day-5/example.txt") as file:
    lines = [line.strip() for line in file.readlines()]

fresh_id_ranges = []
split_idx = lines.index("")

fresh_id_range_lines = lines[:split_idx]
food_id_lines = lines[split_idx+1:]

for range_string in fresh_id_range_lines:
    start, end = [int(i) for i in range_string.split("-")]
    add_unique_ranges(fresh_id_ranges,range(start,end))

count = sum([len(r) for r in fresh_id_ranges])
print(count)


