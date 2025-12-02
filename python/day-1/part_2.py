with open("day-1\\input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

print(lines)

position = 50
count = 0 

for line in lines:
    direction = line[0]
    turns = int(line[1:])
    
    for x in range (turns):
        if direction == "L":
            position -= 1
        else:
            position += 1

        position %= 100
        
        if position == 0:
            count += 1
        


print(count)
