from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.price * self.quantity


def main():
    item1 = Item("Bottle", 1.20, 20)
    print(item1.name)
    print(item1.price)
    print(item1.quantity)


if __name__ == "__main__":
    main()
