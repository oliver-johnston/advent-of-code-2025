def read_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def read_lines_no_strip(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line for line in lines]

def read_line(file_path):
    with open(file_path, 'r') as file:
        line = file.readline()
    return line.strip()