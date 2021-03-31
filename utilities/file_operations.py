import os

def parse_input_file(file_path):
    if(os.path.exists(file_path) and os.path.isfile(file_path) and ".txt" in file_path):
        lines = open(file_path).read().splitlines()
        lines = [line for line in lines if len(line) > 0]
        print(lines)
    else:
        print(f"Make sure the file is valid. We only accept .txt files for now.")
        return False