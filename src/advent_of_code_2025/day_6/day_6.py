import re
from advent_of_code_2025.utils import read_lines, read_lines_no_strip

def run():
    print(part_1("src/advent_of_code_2025/day_6/input.txt"))
    print(part_2("src/advent_of_code_2025/day_6/input.txt"))

def part_1(input_file_path):
    input = read_input_part_1(input_file_path)
    return sum(calculate(x) for x in input)

def part_2(input_file_path):
    input = read_input_part_2(input_file_path)
    return sum(calculate(x) for x in input)

def read_input_part_1(input_file_path):
    lines = read_lines(input_file_path)
    split_lines = [re.split(r"\s+", line) for line in lines]
    transposed = list(map(list, zip(*split_lines)))
    return transposed

def read_input_part_2(input_file_path):
    lines = [list(x) for x in read_lines_no_strip(input_file_path)]
    transposed = list(map(list, zip(*lines)))

    problems = []
    current_problem = []
    current_number = 0
    current_operator = None
    
    for row in transposed:

        if all(x == ' ' for x in row):
            current_problem.append(current_operator)
            problems.append(current_problem)
            current_problem = []
            current_operator = None
            continue
        
        for value in row:
            if value in ['+', '*']:
                current_operator = value
            if value.isdigit():
                current_number = current_number * 10 + int(value)
        
        current_problem.append(current_number)
        current_number = 0
    
    current_problem.append(current_operator)
    problems.append(current_problem)

    return problems

def calculate(values):
    operator = values[-1]
    numbers = [int(x) for x in values[:-1]]
    result = numbers[0]

    for n in numbers[1:]:
        if operator == "+":
            result += n
        elif operator == "*":
            result *= n
    
    return result