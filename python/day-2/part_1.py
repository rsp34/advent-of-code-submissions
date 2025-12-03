# Invalid IDs
# - Double sequence e.g. nums[:mid] = nums[mid:]
# - Is it also 101010 -> every example is just twice

with open("./python/day-2/input.txt") as file:
    contents = file.readline()

ranges = contents.split(',')

total = 0

for r in ranges:
    start, end = r.split('-')
    for id in range(int(start),int(end)+1):
        id_string = str(id)
        id_length = len(id_string)
        if id_length%2 == 0:
            id_mid = int(id_length/2)
            if id_string[:id_mid] == id_string[id_mid:]:
                total+=id

print(total)