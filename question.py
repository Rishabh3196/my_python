class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_details(self):
        return f"{self.make} {self.model} {self.year}"
class Bus(Vehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.capacity = capacity

    def calculate_fare(self, distance, fare_per_km):
        total_fare = distance * fare_per_km
        return total_fare

    def calculate_maintainance_charge(self, maintainance_cost_per_year):
        maintanance_charge = maintainance_cost_per_year / 12
        return maintanance_charge


my_bus = Bus("volvo", "qw12", 2012, 75,)
print(my_bus.get_details())

price = my_bus.calculate_fare(100, 5)
print(price)







