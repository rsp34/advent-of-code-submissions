with open("./python/day-3/input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

def process_battery_bank(bank:str):

    sorted_bank = sorted(bank, reverse=True)
    max_joltage = sorted_bank[0]

    if max_joltage == bank[-1]:
        max_joltage = sorted_bank[1]

    position = bank.find(max_joltage)

    sorted_bank = sorted(bank[position+1:], reverse=True)
    joltage = sorted_bank[0]
    
    return int(max_joltage+joltage)

print(sum([process_battery_bank(bank) for bank in lines]))