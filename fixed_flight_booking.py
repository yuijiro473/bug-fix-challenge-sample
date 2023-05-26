# fixed_flight_booking.py

class Flight:
    def __init__(self, destination='Default', passengers=None):
        self.destination = destination
        self.passengers = passengers if passengers is not None else []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def passenger_count(self):
        return len(self.passengers)

    def get_first_passenger(self):
        return self.passengers[0] if self.passengers else None

    def remove_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)

    def change_destination(self, new_destination):
        self.destination = new_destination

    def sort_passengers(self):
        self.passengers.sort()

    def list_passengers(self):
        return self.passengers

    def is_passenger_on_flight(self, passenger):
        return passenger in self.passengers

    def clear_all_passengers(self):
        self.passengers.clear()