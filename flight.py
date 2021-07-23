#Class Flight to Add Passenger to a Flight
#CS50

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

# Tell me how many seats are available 
    def open_seats(self):
        return self.capacity - len(self.passengers)

#Just 3 seats at the class Flight
flight = Flight(3)

#Names from the passengers
people = ["Renato", "Mario", "Andre", "Edson"]

#Will try to add every people to the Flight, if its True will return
#Successfully, if not will return No available seats for that person.
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")    
    else: 
        print(f"No available seats for {person}")
