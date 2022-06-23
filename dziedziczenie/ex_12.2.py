from abc import abstractmethod


class Vehicle:
    def __init__(self, max_speed, number):
        self.max_speed = max_speed
        self.number = number
        self.type = None

    def __str__(self):
        return f"Numer Pojazdu: {self.number} Maksymalna prędkość: {self.max_speed} km/h."

class Bus(Vehicle):
    def __init__(self, number, max_speed, fuel_per_month):
        super().__init__(number, max_speed)
        self.fuel_per_month = fuel_per_month
        self.type = "bus"


class Tram(Vehicle):
    def __init__(self, number, max_speed, number_of_wagons):
        super().__init__(number, max_speed)
        self.number_of_wagons = number_of_wagons
        self.type = "tram"


class Barn:
    def __init__(self, name: str, ) -> None:
        self.name = name
        self.vehicles = []
        self.type = None

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Został dodany pojazd o numerze: {vehicle.number}")

    def display_all(self):
        for vehicle in self.vehicles:
            print(f"Numer pojazdu: {vehicle.number}, typ {vehicle.type}.")

    def __str__(self):
        return f"Nazwa zajezdni: {self.name}"


class BusBarn(Barn):
    """Bus barn class representing barn full of the buses"""
    def __init__(self, name):
        super().__init__(name)

    def sum_fuel(self):
        """Return fuel sum of the all buses in the barn"""
        sum_fuel = 0
        for vehicle in self.vehicles:
            sum_fuel += vehicle.fuel_per_month
        return sum_fuel


class TramBarn(Barn):
    def __init__(self, name):
        super().__init__(name)

    def sum_wagons(self):
        sum_wagons = 0
        for vehicle in self.vehicles:
            sum_wagons += vehicle.number_of_wagons
        return sum_wagons


def main():
    bus_1 = Bus("ABD12554", 150, 1000)
    tram_1 = Tram("47756", 120, 3)
    bus_barn = BusBarn("Zajezdnia tramwajowa")
    bus_barn.add_vehicle(bus_1)

if __name__ == "__main__":
    main()
