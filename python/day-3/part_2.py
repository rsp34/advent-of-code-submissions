with open("./python/day-3/input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

def process_battery_bank(bank:str, battery_count:int):

    if battery_count == 1:
        sorted_bank = sorted(bank,reverse=True)
    else:
        sorted_bank = sorted(bank[:-battery_count+1], reverse=True)
    max_joltage = sorted_bank[0]

    position = bank.find(max_joltage)

    total_joltage = ""
    if battery_count > 1:
        total_joltage = process_battery_bank(bank[position+1:],battery_count-1)
    
    return bank[position] + total_joltage

print(sum([int(process_battery_bank(bank,12)) for bank in lines]))