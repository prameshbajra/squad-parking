parking_slots = {}


def create_parking_slots(number_of_slots):
    """This method creates the framework for the parking area. Based on the number_of_slots space is created for the same number.

    Args:
        number_of_slots (str): Initially str, later converted into int, will create 'n' number of spaces in the parking area.

    Returns:
        Boolean: Returns True if space is created, else False.
    """
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
    """Allocates a slot that is closest to the entrance, based on the number plate of the vehicle and drivers age.

    Args:
        vehicle_id (str): Registration plate / number plate of the vehicle that needs to be parked on to a slot in parking area.
        driver_age (str): Age of the driver who parks.   

    Returns:
        Boolean: Return True if the parking space is alloted, else False.
    """
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
                    f"Vehicle number : {vehicle_id} has been granted slot number {slot_number}."
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
    """Given the age of the driver, return all the number plates of the vehicle which has drivers of that age.

    Args:
        drivers_age (str -> int): Age of the driver

    Returns:
        list: Returns list of number plates having drivers with same age. If not driver with that age exists then empty list is returned.
    """
    vehicle_ids = []
    drivers_age = int(drivers_age)
    for slot_number, details in parking_slots.items():
        if (details is not None and int(details["driver_age"]) == drivers_age):
            vehicle_ids.append(details["vehicle_id"])
    if (len(vehicle_ids) > 0):
        print(vehicle_ids)
    else:
        print(f"No records found for driver age : {drivers_age}")
    return vehicle_ids


def get_slot_number_by_vehicle_id(vehicle_id):
    """Given the number plate of the vehicle find out which slot the vehicle is parked at.

    Args:
        vehicle_id (str): Number plate of the vehicle

    Returns:
        int: Returns the slot number on which the vehicle is parked at. If not present returns None.
    """
    for slot_number, details in parking_slots.items():
        if (details is not None and details["vehicle_id"] == vehicle_id):
            print(f"Vehicle : {vehicle_id} is present in slot : {slot_number}")
            return slot_number
    print(f"Vehicle : {vehicle_id} not found in our parking facility.")
    return None


def get_slot_number_by_drivers_age(drivers_age):
    """Given the drivers age, this method returns the slot numbers for which drivers of that age is present.

    Args:
        drivers_age (str -> int): Age of the driver that was used to enter when parking.

    Returns:
        list: A list of slot numbers for which drivers of that age is present.
    """
    slot_numbers_for_age = []
    drivers_age = int(drivers_age)
    for slot_number, details in parking_slots.items():
        if (details is not None and int(details["driver_age"]) == drivers_age):
            slot_numbers_for_age.append(slot_number)
    if (len(slot_numbers_for_age) > 0):
        print(slot_numbers_for_age)
    else:
        print(f"No records found for driver age : {drivers_age}")
    return slot_numbers_for_age


def clear_parking_space(slot_number):
    """Removes the given slot number, marking it as empty and gives the vehicle that just left.

    Args:
        slot_number (str -> int): Returns the slot number that was emptied.
    """
    slot_number = int(slot_number)
    if (parking_slots[slot_number] is None):
        print(f"Parking slot number : {slot_number} is already vacant.")
    else:
        vehicle_id = parking_slots[slot_number]["vehicle_id"]
        parking_slots[slot_number] = None
        print(
            f"Vehicle_id : {vehicle_id} has left the parking area. Slot number : {slot_number} is vacant now."
        )
    return slot_number


def get_parking_slot():
    return parking_slots