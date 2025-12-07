from advent_of_code_2025.utils import read_lines

def run():
    print(part_1("src/advent_of_code_2025/day_5/input.txt"))
    print(part_2("src/advent_of_code_2025/day_5/input.txt"))

def part_1(input_file_path):
    fresh_ranges, available_ids = read_input(input_file_path)

    return sum(1 for id in available_ids if any(r[0] <= id <= r[1] for r in fresh_ranges))

def part_2(input_file_path):
    fresh_ranges, _ = read_input(input_file_path)

    fresh_ranges = sorted(fresh_ranges, key=lambda r: r[0])

    count_fresh = 0
    max_id = 0
    for range in fresh_ranges:
        capped_start = max(range[0], max_id + 1)
        if capped_start <= range[1]:
            count_fresh += (range[1] - capped_start + 1)
            max_id = range[1]
    
    return count_fresh

def read_input(input_file_path):
    lines = read_lines(input_file_path)
    split_index = lines.index("")
    fresh_ranges = [parse_range(x) for x in lines[:split_index]]
    available_ids = [int(x) for x in lines[split_index+1:]]
    return fresh_ranges, available_ids

def parse_range(range_str):
    parts = range_str.split("-")
    return (int(parts[0]), int(parts[1]))