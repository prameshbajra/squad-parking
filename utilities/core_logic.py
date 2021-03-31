parking_slots = {}


def create_parking_slots(number_of_slots):
    number_of_slots = int(number_of_slots)
    if (number_of_slots is None or number_of_slots == 0):
        print(f"Cannot create parking lots. Please try again.")
        return False
    if (isinstance(number_of_slots, float)):
        number_of_slots = int(number_of_slots)
        print(
            f"Cannot create slots with decimal numbers. Rounding it off to : {number_of_slots}"
        )
    for i in range(number_of_slots):
        parking_slots[i + 1] = None
    print(f"Created Parking of {number_of_slots} slots.")
    return True


def park_vechile(vehicle_id, driver_age):
    if (vehicle_id is None or driver_age is None or driver_age == 0):
        print(
            f"Cannot add vehicle : {vehicle_id} with drivers age : {driver_age}. Make sure you have entered valid age and vehicle id."
        )
        return False
    is_entry_successful = False
    vehicle_ids = []
    for slot_number, details in parking_slots.items():
        if (details is None):
            if (vehicle_id in vehicle_ids):
                print(
                    f"The vehicle : {vehicle_id} is already present in the parking area. You might want to recheck."
                )
                return False
            else:
                parking_slots[slot_number] = {
                    "vehicle_id": vehicle_id,
                    "driver_age": driver_age
                }
                is_entry_successful = True
                print(
                    f"Vehicle number : {vehicle_id} has been granted {slot_number} slot."
                )
                break
        else:
            vehicle_ids.append(details["vehicle_id"])
    if (not is_entry_successful):
        print(
            f"Sorry, we cannot grant entrance to {vehicle_id}. The parking lot is full."
        )
        return False
    return True


def get_vehicle_ids_by_drivers_age(drivers_age):
    vehicle_ids = []
    drivers_age = int(drivers_age)
    for slot_number, details in parking_slots.items():
        if (details is not None and details["driver_age"] == drivers_age):
            vehicle_ids.append(details["vehicle_id"])
    if (len(vehicle_ids) > 0):
        print(vehicle_ids)
    else:
        print(f"No records found for driver age : {drivers_age}")
    return vehicle_ids


def get_slot_number_by_vehicle_id(vehicle_id):
    for slot_number, details in parking_slots.items():
        if (details is not None and details["vehicle_id"] == vehicle_id):
            print(f"Vehicle : {vehicle_id} is present in slot : {slot_number}")
            return slot_number
    print(f"Vehicle : {vehicle_id} not found in our parking facility.")
    return None


def get_slot_number_by_drivers_age(drivers_age):
    slot_numbers_for_age = []
    drivers_age = int(drivers_age)
    for slot_number, details in parking_slots.items():
        if (details is not None and details["driver_age"] == drivers_age):
            slot_numbers_for_age.append(slot_number)
    if (len(slot_numbers_for_age) > 0):
        print(slot_numbers_for_age)
    else:
        print(f"No records found for driver age : {drivers_age}")
    return slot_numbers_for_age


def clear_parking_space(slot_number):
    slot_number = int(slot_number)
    if (parking_slots[slot_number] is None):
        print(f"Parking slot number : {slot_number} is already vacant.")
    else:
        vehicle_id = parking_slots[slot_number]["vehicle_id"]
        parking_slots[slot_number] = None
        print(
            f"Vehicle_id : {vehicle_id} has left the parking area. Slot number : {slot_number} is vacant now."
        )
