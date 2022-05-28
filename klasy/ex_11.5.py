class Order:
    def __init__(self, order_id: int, order_name: str, order_price: float) -> None:
        self.id = order_id
        self.name = order_name
        self.price = order_price

    def display(self):
        print(f"Nazwa: {self.name}, ID: {self.id}, cena: {self.price}")

    def __repr__(self) -> str:
        return f"Nazwa: {self.name}, ID: {self.id}, cena: {self.price}"


class Manager:
    def __init__(self) -> None:
        self.orders = {}

    def add_order(self, new_order: Order) -> None:
        if not self.orders:
            self.orders[new_order] = 1
            print(f'Added new order. There is {self.orders.get(new_order)} ordrers no. {new_order.id} now')
            return
        for order in self.orders:
            if order.id == new_order.id:
                self.orders[order] += 1
            else:
                self.orders[new_order] = 1
        print(f'Added new order. There is {self.orders.get(new_order)} ordrers no. {new_order.id} now')
    #
    # def sell(self, id_to_sell: int) -> None:
    #     for order in self.orders:
    #         if order.id == id_to_sell:
    #             self.orders[order] -= 1
    #
    # def display(self):
    #     print(self.orders)

def main():
    order1 = Order(1, "Ogórek", 1.60)
    order2 = Order(1, "Ogórek", 1.60)
    manager = Manager()
    manager.add_order(order1)
    manager.add_order(order2)

    print(manager.orders)


if __name__ == "__main__":
    main()
