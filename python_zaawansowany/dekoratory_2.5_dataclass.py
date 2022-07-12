from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.price * self.quantity

class ItemNormal:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented

        return (self.name, self.price, self.quantity) == (other.name, other.price, other.quantity)

    def total_cost(self) -> float:
        return self.price * self.quantity


def main():
    item1 = Item("Bottle", 1.20, 20)
    item2 = Item("Bottle", 1.20, 20)
    item_1 = ItemNormal("Bottle", 1.20, 20)
    item_2 = ItemNormal("Bottle", 1.20, 20)
    print(item1==item2)
    print(item_1==item_2)
    print(item1.name)
    print(item1.price)
    print(item1.quantity)


if __name__ == "__main__":
    main()
