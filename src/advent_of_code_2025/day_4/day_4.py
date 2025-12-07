from advent_of_code_2025.utils import read_lines

def run():
    print(part_1("src/advent_of_code_2025/day_4/input.txt"))
    print(part_2("src/advent_of_code_2025/day_4/input.txt"))

def part_1(input_file_path):
    rows = read_input(input_file_path)
    return count_and_mark(rows)

def part_2(input_file_path):
    rows = read_input(input_file_path)
    sum_count = 0
    prev_count = 999
    while prev_count > 0:
        prev_count = count_and_mark(rows)
        sum_count += prev_count
        reset_marks(rows)
    return sum_count

def count_and_mark(rows):
    count = 0
    for i in range(len(rows)):
        for j in range(len(rows[i])):            
            if rows[i][j] == '@' and count_neigbours(rows, i, j) < 4:
                rows[i][j] = 'X'
                count += 1
    return count

def reset_marks(rows):
    for i in range(len(rows)):
        for j in range(len(rows[i])):            
            if rows[i][j] == 'X':
                rows[i][j] = '.'

def count_neigbours(rows, i, j):
    count = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni = i + di
            nj = j + dj
            if ni < 0 or ni >= len(rows) or nj < 0 or nj >= len(rows[ni]):
                continue
            test = rows[ni][nj]
            if test == '@' or test == 'X':
                count += 1
    return count

def read_input(input_file_path):
    lines = read_lines(input_file_path)
    return [list(line) for line in lines]