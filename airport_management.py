class AirportManagement:
    def __init__(self):
        """Initialize an airport management system with an empty list of flights."""
        self.flights = {}

    def add_flight(self, flight_number, airline, destination):
        """Add a flight to the system."""
        if flight_number in self.flights:
            raise ValueError("Flight already exists.")
        self.flights[flight_number] = {
            "airline": airline,
            "destination": destination,
            "passengers": []
        }

    def remove_flight(self, flight_number):
        """Remove a flight from the system."""
        if flight_number not in self.flights:
            raise ValueError("Flight does not exist.")
        del self.flights[flight_number]

    def check_in_passenger(self, flight_number, passenger_name):
        """Check in a passenger for a specific flight."""
        if flight_number not in self.flights:
            raise ValueError("Flight does not exist.")
        self.flights[flight_number]["passengers"].append(passenger_name)

    def get_flight_details(self, flight_number):
        """Get details of a specific flight."""
        if flight_number not in self.flights:
            raise ValueError("Flight does not exist.")
        return self.flights[flight_number]

    def get_all_flights(self):
        """Return all flights in the system."""
        return self.flights

    # Updated comment to test CI/CD workflow
    print("Testing GitHub Actions again")
