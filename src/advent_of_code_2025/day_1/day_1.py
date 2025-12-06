from advent_of_code_2025.utils import read_lines

def run():
    print(part_1("src/advent_of_code_2025/day_1/input.txt"))
    print(part_2("src/advent_of_code_2025/day_1/input.txt"))

def part_1(input_file_path):
    lines = read_lines(input_file_path)
    
    count = 0
    pos = 50

    for line in lines:
        if line[0] == 'L':
            pos -= int(line[1:])
        else:
            pos += int(line[1:])

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
        i = int(line[1:])
        for _ in range(i):
            if line[0] == 'L':
                pos -= 1
            else:
                pos += 1

            pos = pos % 100
        
            if pos == 0:
                count += 1

    return count