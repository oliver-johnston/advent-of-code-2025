from advent_of_code_2025.day_1 import day_1

def test_part_1():
    result = day_1.part_1("tests/day_1/example_input.txt")
    assert result == 3

def test_part_2():
    result = day_1.part_2("tests/day_1/example_input.txt")
    assert result == 6