from advent_of_code_2025.utils import read_lines

def run():
    print(part_1("src/advent_of_code_2025/day_1/input.txt"))
    print(part_2("src/advent_of_code_2025/day_1/input.txt"))

def part_1(input_file_path):
    lines = read_lines(input_file_path)
    
    count = 0
    pos = 50

    for line in lines:
        direction = -1 if line[0] == 'L' else 1
        amount = int(line[1:])
        pos += direction * amount
        pos = pos % 100
        if pos == 0:
            count += 1

    return count

def part_2(input_file_path):
    lines = read_lines(input_file_path)
    
    count = 0
    pos = 50

    # probably some maths way to do this, but brute forcing it one at a time works fine
    for line in lines:
        direction = -1 if line[0] == 'L' else 1
        amount = int(line[1:])
        for _ in range(amount):
            pos += direction
            pos = pos % 100        
            if pos == 0:
                count += 1

    return count