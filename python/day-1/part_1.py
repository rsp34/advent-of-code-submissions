with open("./python/day-1/input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

position = 50
count = 0 

for line in lines:
    direction = line[0]
    turns = int(line[1:])

    if direction == "L":
        position -= turns
    else:
        position += turns

    position = position%100

    if position == 0:
        count += 1


print(count)