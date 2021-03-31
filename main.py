import traceback

from utilities.file_operations import parse_input_file

def start_parking_program():
    try:
        print("========== Welcome to Squad Parking. ========== \n")
        file_path = input("Enter the path for the file (should be .txt) you want to run : ")
        parse_input_file(file_path)
    except Exception:
        print("Oops! The program broke. Please try running it again.")

if __name__ == '__main__':
    start_parking_program()