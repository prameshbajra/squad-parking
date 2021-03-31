import unittest

from utilities.core_logic import create_parking_slots, park_vechile, get_vehicle_ids_by_drivers_age, get_slot_number_by_vehicle_id, get_slot_number_by_drivers_age, clear_parking_space, get_parking_slot


class TestCoreLogic_create_parking_slots(unittest.TestCase):
    def test_create_parking_slots(self):
        self.assertTrue(create_parking_slots(7))
        self.assertFalse(create_parking_slots(0))
        self.assertFalse(create_parking_slots(-3))
        self.assertTrue(create_parking_slots(5.678))
        self.assertTrue(create_parking_slots("06"))
        self.assertFalse(create_parking_slots(None))


class TestCoreLogic_park_vehicle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n==== Starting : park_vechile ====")
        create_parking_slots(7)

    def test_park_vehicle(self):
        # Varying drivers age ...
        self.assertTrue(park_vechile("AA-08-BB-9090", 12))
        self.assertTrue(park_vechile("AA-09-BB-0091", "100"))
        self.assertFalse(park_vechile("AA-09-BB-0092", 0))
        self.assertFalse(park_vechile("AA-09-BB-0093", -10))
        self.assertFalse(park_vechile("AA-09-BB-0094", "-10"))
        self.assertFalse(park_vechile("AA-09-BB-0095", None))

        # Vehile id related cases ...
        self.assertTrue(park_vechile("PB-01-HH-1234", 24))
        self.assertTrue(park_vechile("CH-AA-PB-3719", 21))
        # Use same vehicle id should fail and return False ...
        self.assertFalse(park_vechile("CH-AA-PB-3719", 19))
        self.assertTrue(park_vechile("NP-01-HH-1234", 24))
        self.assertTrue(park_vechile("US-AA-PB-3719", 21))
        self.assertTrue(park_vechile("CS-NA-PB-8729", 21))
        # If parking is full, it should not be alloted and should return False ...
        self.assertFalse(park_vechile("NA-09-MK-2903", 57))
        self.assertFalse(park_vechile(None, 100))

    @classmethod
    def tearDownClass(cls):
        print("==== End ====\n")


class TestCoreLogic_get_vehicle_ids_by_drivers_age(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n==== Starting : get_vehicle_ids_by_drivers_age ====")
        create_parking_slots(3)
        park_vechile("A", 24)
        park_vechile("B", 36)
        park_vechile("C", 24)

    def test_get_vehicle_ids_by_drivers_age(self):
        self.assertListEqual(get_vehicle_ids_by_drivers_age(24), ["A", "C"])
        self.assertListEqual(get_vehicle_ids_by_drivers_age(None), [])
        self.assertListEqual(get_vehicle_ids_by_drivers_age("10"), [])
        self.assertListEqual(get_vehicle_ids_by_drivers_age("24"), ["A", "C"])
        self.assertListEqual(get_vehicle_ids_by_drivers_age(-24), [])
        self.assertListEqual(get_vehicle_ids_by_drivers_age(36), ["B"])

    @classmethod
    def tearDownClass(cls):
        print("==== End ==== \n")


class TestCoreLogic_get_slot_number_by_vehicle_id(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n==== Starting : get_slot_number_by_vehicle_id ====")
        create_parking_slots(3)
        park_vechile("A", 24)
        park_vechile("B", 36)

    def test_get_slot_number_by_vehicle_id(self):
        self.assertEqual(get_slot_number_by_vehicle_id("A"), 1)
        self.assertEqual(get_slot_number_by_vehicle_id("B"), 2)
        self.assertIsNone(get_slot_number_by_vehicle_id(None))
        self.assertIsNone(get_slot_number_by_vehicle_id("C"))

    @classmethod
    def tearDownClass(cls):
        print("==== End ==== \n")


class TestCoreLogic_get_slot_number_by_drivers_age(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n==== Starting : get_slot_number_by_drivers_age ====")
        create_parking_slots(3)
        park_vechile("A", 24)
        park_vechile("B", 36)
        park_vechile("C", 24)

    def test_get_slot_number_by_drivers_age(self):
        self.assertListEqual(get_slot_number_by_drivers_age(24), [1, 3])
        self.assertListEqual(get_slot_number_by_drivers_age("24"), [1, 3])
        self.assertListEqual(get_slot_number_by_drivers_age(-32), [])
        self.assertListEqual(get_slot_number_by_drivers_age(None), [])

    @classmethod
    def tearDownClass(cls):
        print("==== End ==== \n")


class TestCoreLogic_clear_parking_space(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("==== Starting : clear_parking_space ====")
        create_parking_slots(5)
        park_vechile("ABCD", 21)
        park_vechile("EFGH", 24)

    def test_clear_parking_space(self):
        self.assertTrue(clear_parking_space(1))
        self.assertFalse(clear_parking_space("1"))

    @classmethod
    def tearDownClass(cls):
        print("==== End ====")
