class Vehicle:
    def __init__(self, max_speed: int, mileage: float) -> None:
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_mileage(self, km: float) -> None:
        print(f"Stary przebieg: {self.mileage} km. \n"
              f"Po dodaniu {km} km, obecny przebieg to {self.mileage + km} km.")
        self.mileage += km



def main():
    vehicle1 = Vehicle(240, 10.0)
    vehicle1.increase_mileage(20.0)
    vehicle1.increase_mileage(30.0)


if __name__ == "__main__":
    main()