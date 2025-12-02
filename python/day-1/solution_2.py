with open("day-1\\input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

print(lines)

position = 50
count = 0 

for line in lines:
    direction = line[0]
    turns = int(line[1:])

    if direction == "L":
        if position==0:
            count-=1
        position -= turns
    else:
        position += turns
    
    print(f"Position {position}, turns {turns}, {direction}, count: {count}")
          
    if position >= 100:
        count+=position//100
        print(f"  {position//100}")
    elif position < 0:
        count+=-(position//100)
        print(f"  {-position//100}")
    elif position==0:
        count+=1
    

    position = position%100  

print(count)
