from advent_of_code_2025.utils import read_line

def run():
    print(part_1("src/advent_of_code_2025/day_2/input.txt"))
    print(part_2("src/advent_of_code_2025/day_2/input.txt"))

def part_1(input_file_path):
    return sum_invalids(input_file_path, is_repeating_part_1)

def part_2(input_file_path):
    return sum_invalids(input_file_path, is_repeating_part_2)

def sum_invalids(input_file_path, invalid_check_fn):
    line = read_line(input_file_path)

    ranges = line.split(',')

    invalids = []

    for r in ranges:
        start, end = map(int, r.split('-'))
        invalids.extend(get_invalids(start, end, invalid_check_fn))

    return sum(invalids)

def get_invalids(start, end, invalid_check_fn):
    invalids = []
    for i in range(start, end + 1):
        if invalid_check_fn(i):
            invalids.append(i)
    return invalids
        
def is_repeating_part_1(number):
    num_str = str(number)
    num_len = len(num_str)
    # must be even length to be repeating
    if num_len % 2 == 1:
        return False
    first_half = num_str[:num_len//2]
    second_half = num_str[num_len//2:]
    return first_half == second_half

def is_repeating_part_2(number):
    num_str = str(number)
    for size in range(1, len(num_str)//2 + 1):
        # only consider sizes that evenly divide the length of num_str
        if len(num_str) % size != 0:
            continue

        test = num_str[:size]
        # repeat test enough times to match length of num_str
        repeated = test * (len(num_str) // size)
        if repeated == num_str:
            return True
    return False