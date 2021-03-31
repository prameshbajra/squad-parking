import os

from utilities.core_logic import create_parking_slots, park_vechile, get_slot_number_by_drivers_age, get_slot_number_by_vehicle_id, get_vehicle_ids_by_drivers_age, clear_parking_space


def process_parking(command, value):
    if (command == "create_parking_lot"):
        create_parking_slots(value)
    elif (command == "park"):
        unpacked_values = value.split(" ")
        vehicle_id = unpacked_values[0]
        drivers_age = unpacked_values[2]
        park_vechile(vehicle_id, drivers_age)
    elif (command == "slot_numbers_for_driver_of_age"):
        get_slot_number_by_drivers_age(value)
    elif (command == "slot_number_for_car_with_number"):
        get_slot_number_by_vehicle_id(value)
    elif (command == "vehicle_registration_number_for_driver_of_age"):
        get_vehicle_ids_by_drivers_age(value)
    elif (command == "leave"):
        clear_parking_space(value)
    else:
        print("Command not valid. Skipping !")


def process_lines(lines):
    for index, line in enumerate(lines):
        command = (line.split(" ", 1)[0]).lower()
        value = (line.split(" ", 1)[1]).lower()
        if (command is None or value is None):
            print(
                f"Line : {line} is invalid. Please correct it and run again.")
        else:
            process_parking(command, value)


def parse_input_file(file_path):
    if (os.path.exists(file_path) and os.path.isfile(file_path)
            and ".txt" in file_path):
        lines = open(file_path).read().splitlines()
        lines = [line for line in lines if len(line) > 0]
        process_lines(lines)
    else:
        print(
            f"Make sure the file exists and is valid. We only accept .txt files for now."
        )
        return False