import unittest
from airport_management import AirportManagement


class TestAirportManagement(unittest.TestCase):
    def setUp(self):
        """Initialize an AirportManagement instance before each test."""
        self.airport = AirportManagement()
        self.airport.add_flight("AI101", "Air India", "New York")

    def test_add_flight(self):
        """Test adding a new flight."""
        self.airport.add_flight("BA202", "British Airways", "London")
        self.assertIn("BA202", self.airport.flights)

    def test_add_existing_flight(self):
        """Test adding an existing flight raises an error."""
        with self.assertRaises(ValueError):
            self.airport.add_flight("AI101", "Air India", "New York")

    def test_remove_flight(self):
        """Test removing a flight."""
        self.airport.remove_flight("AI101")
        self.assertNotIn("AI101", self.airport.flights)

    def test_remove_non_existent_flight(self):
        """Test removing a non-existent flight raises an error."""
        with self.assertRaises(ValueError):
            self.airport.remove_flight("XX999")

    def test_check_in_passenger(self):
        """Test checking in a passenger."""
        self.airport.check_in_passenger("AI101", "John Doe")
        self.assertIn("John Doe", self.airport.flights["AI101"]["passengers"])

    def test_check_in_multiple_passengers(self):
        """Test checking in multiple passengers."""
        self.airport.check_in_passenger("AI101", "Alice")
        self.airport.check_in_passenger("AI101", "Bob")
        self.assertIn("Alice", self.airport.flights["AI101"]["passengers"])
        self.assertIn("Bob", self.airport.flights["AI101"]["passengers"])
        self.assertEqual(len(self.airport.flights["AI101"]["passengers"]), 2)

    def test_check_in_same_passenger_twice(self):
        """Test checking in the same passenger twice (should allow but count)."""
        self.airport.check_in_passenger("AI101", "Charlie")
        self.airport.check_in_passenger("AI101", "Charlie")
        self.assertEqual(
            self.airport.flights["AI101"]["passengers"].count("Charlie"), 2)

    def test_check_in_passenger_invalid_flight(self):
        """Test checking in a passenger for a non-existent flight."""
        with self.assertRaises(ValueError):
            self.airport.check_in_passenger("XX999", "Jane Doe")

    def test_get_flight_details(self):
        """Test retrieving flight details."""
        details = self.airport.get_flight_details("AI101")
        self.assertEqual(details["airline"], "Air India")
        self.assertEqual(details["destination"], "New York")

    def test_get_flight_details_with_passenger_count(self):
        """Test retrieving flight details with passengers checked in."""
        self.airport.check_in_passenger("AI101", "David")
        details = self.airport.get_flight_details("AI101")
        self.assertEqual(len(details["passengers"]), 1)

    def test_get_flight_details_invalid_flight(self):
        """Test retrieving details of a non-existent flight."""
        with self.assertRaises(ValueError):
            self.airport.get_flight_details("XX999")

    def test_get_all_flights(self):
        """Test retrieving all flights."""
        flights = self.airport.get_all_flights()
        self.assertEqual(len(flights), 1)

    def test_get_all_flights_after_multiple_additions(self):
        """Test adding multiple flights and retrieving them."""
        self.airport.add_flight("EK303", "Emirates", "Dubai")
        self.airport.add_flight("LH404", "Lufthansa", "Frankfurt")
        flights = self.airport.get_all_flights()
        self.assertEqual(len(flights), 3)

    def test_remove_all_flights(self):
        """Test removing all flights and checking if system is empty."""
        self.airport.remove_flight("AI101")
        self.assertEqual(len(self.airport.get_all_flights()), 0)

    def test_empty_flight_list(self):
        """Test if the system starts empty before adding flights."""
        empty_airport = AirportManagement()
        self.assertEqual(len(empty_airport.get_all_flights()), 0)


if __name__ == '__main__':
    unittest.main()
