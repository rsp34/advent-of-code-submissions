with open("./python/day-5/input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

fresh_id_ranges = []
split_idx = lines.index("")

fresh_id_range_lines = lines[:split_idx]
food_id_lines = lines[split_idx+1:]

for range_string in fresh_id_range_lines:
    start, end = [int(i) for i in range_string.split("-")]
    fresh_id_ranges.append(range(start,end+1))

food_ids = [int(i) for i in food_id_lines]

count = 0

for id in food_ids:
    for fresh_id_range in fresh_id_ranges:
        if id in fresh_id_range:
            count += 1
            break

print(count)