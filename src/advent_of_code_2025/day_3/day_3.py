from advent_of_code_2025.utils import read_lines

def run():
    print(part_1("src/advent_of_code_2025/day_3/input.txt"))
    print(part_2("src/advent_of_code_2025/day_3/input.txt"))

def part_1(input_file_path):
    return get_sum_of_digits(input_file_path, 2)

def part_2(input_file_path):
    return get_sum_of_digits(input_file_path, 12)

def get_sum_of_digits(input_file_path, number_of_digits):
    banks = read_lines(input_file_path)
    sum = 0
    for bank in banks:
        digits = [int(d) for d in bank]
        sum += get_max_number(digits, number_of_digits)

    return sum

def get_max_number(digits, number_of_digits):
    number = 0
    index_of_max = -1

    for i in range(number_of_digits):
        start = index_of_max + 1
        end = number_of_digits - i - 1
        
        eligbile_digits = digits[start:-end] if end > 0 else digits[start:]

        max_digit = max(eligbile_digits)
        index_of_max = digits.index(max_digit, start)

        number = (number * 10) + max_digit
    
    return number