import unittest
import utilities.core_logic as cl
from utilities.file_operations import process_parking, process_lines, parse_input_file


class TestFileOperations_process_parking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n==== Starting : process_parking ====")
        cl.parking_slots = {}

    def test_process_parking(self):
        # If parking is tried without creation of parking slots ...
        # Program exits with meaningful print statement ...
        with self.assertRaises(SystemExit) as cm:
            process_parking("park", "KK-09-IL-9173 driver_age 28")
        self.assertEqual(cm.exception.code, 0)

        self.assertTrue(process_parking("create_parking_lot", "3"))
        self.assertTrue(
            process_parking("vehicle_registration_number_for_driver_of_age",
                            "31"))
        self.assertTrue(process_parking("SOME_RANDOM_THING", "RANDOM_VALUE"))
        self.assertTrue(process_parking("park", "PB-01-HH-1234 driver_age 21"))
        self.assertTrue(process_parking("park", "OI-34-KL-4912 driver_age 32"))
        self.assertTrue(process_parking("slot_numbers_for_driver_of_age",
                                        "32"))

    @classmethod
    def tearDownClass(cls):
        print("==== End ==== \n")


class TestFileOperations_process_lines(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n==== Starting : process_lines ====")

    def test_process_lines(self):
        # No matter the number of lines the program should process all lines accordingly ...
        self.assertIsNone(
            process_lines([
                "create_parking_lot 3", "Park PB-01-TG-2341 driver_age 40",
                "Park HR-29-TG-3098 driver_age 39", "Leave 1",
                "Park PB-01-HH-1234 driver_age 21",
                "Vehicle_registration_number_for_driver_of_age 18",
                "Vehicle_registration_number_for_driver_of_age 21",
                "Slot_number_for_car_with_number PB-01-HH-1234",
                "Slot_numbers_for_driver_of_age 40"
            ]))
        self.assertIsNone(
            process_lines(
                ["THISISRANDOM", "COMMAND", "WHICH", "WILL NOT EXECUTE"]))

    @classmethod
    def tearDownClass(cls):
        print("==== End ==== \n")


class TestFileOperations_parse_input_file(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n==== Starting : parse_input_file ====")

    def test_parse_input_file(self):
        self.assertIsNone(parse_input_file(r"./input/input_spaces.txt"))
        self.assertIsNone(parse_input_file(r"./input/input_valid.txt"))
        self.assertIsNone(parse_input_file(r"./input/input_parking_full.txt"))

    @classmethod
    def tearDownClass(cls):
        print("==== End ==== \n")