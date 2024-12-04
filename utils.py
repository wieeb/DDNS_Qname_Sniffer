# utils.py
import sys
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
