import unittest
from fixed_flight_booking import Flight  # assume the corrected script is named 'fixed_flight_booking.py'

class TestFlightMethods(unittest.TestCase):

    def setUp(self):
        self.flight = Flight('Tokyo')

    def test_add_and_remove_passenger(self):
        self.flight.add_passenger('John')
        self.assertIn('John', self.flight.passengers)
        self.flight.remove_passenger('John')
        self.assertNotIn('John', self.flight.passengers)

    def test_passenger_count(self):
        self.flight.add_passenger('John')
        self.flight.add_passenger('Jane')
        self.assertEqual(self.flight.passenger_count(), 2)

    def test_get_first_passenger(self):
        self.flight.add_passenger('John')
        self.assertEqual(self.flight.get_first_passenger(), 'John')
        self.flight.clear_all_passengers()
        self.assertIsNone(self.flight.get_first_passenger())

    def test_change_destination(self):
        self.flight.change_destination('Osaka')
        self.assertEqual(self.flight.destination, 'Osaka')

    def test_sort_passengers(self):
        self.flight.add_passenger('John')
        self.flight.add_passenger('Jane')
        self.flight.add_passenger('Adam')
        self.flight.sort_passengers()
        self.assertEqual(self.flight.list_passengers(), ['Adam', 'Jane', 'John'])

    def test_is_passenger_on_flight(self):
        self.flight.add_passenger('John')
        self.assertTrue(self.flight.is_passenger_on_flight('John'))
        self.assertFalse(self.flight.is_passenger_on_flight('Jane'))

    def test_clear_all_passengers(self):
        self.flight.add_passenger('John')
        self.flight.clear_all_passengers()
        self.assertEqual(self.flight.passenger_count(), 0)

if __name__ == '__main__':
    unittest.main()