# Invalid IDs
# - Double sequence e.g. nums[:mid] = nums[mid:]
# - Is it also 101010 -> every example is just twice

def check_id_for_repeated_sequences(id_string:str,substring_length:int):
    # 11111 - True
    # 121212 - True
    # 123456 - False
    # 121234 - False
    if len(id_string) % substring_length != 0:
        # We can't split the string uniformly
        return False
    
    sub = id_string[:substring_length]
    id_string = id_string[substring_length:]
    while id_string:
        next_sub = id_string[:substring_length]
        id_string = id_string[substring_length:]
        if sub != next_sub:
            return False

    return True

    number_of_subs = int(len(id_string)/substring_length)
    lastSection = id_string[:substring_length]
    for i in range(1,number_of_subs):
        nextSection = id_string[i*substring_length:(i+1)*substring_length]
        if nextSection != lastSection:
            return False
    return True

def isValidID(id:int):
    id_string = str(id)
    id_length = len(id_string)
    id_mid = int(id_length/2)+1

    return not any([check_id_for_repeated_sequences(id_string,l) for l in range(1,id_mid)])

    for substring_length in range(1,id_mid):
        if check_id_for_repeated_sequences(id_string, substring_length):
            return False
    return True
    
with open("./python/day-2/input.txt") as file:
    contents = file.readline()

ranges = contents.split(',')

total = 0

for r in ranges:
    start, end = r.split('-')
    for id in range(int(start),int(end)+1):
        if not isValidID(id):
            total+=id

print(total)