class Rectangle:
    def __init__(self, a: float, h: float) -> None:
        self.a = a
        self.h = h

    def area(self) -> float:
        return self.a * self.h

    def perimeter(self) -> float:
        return 2 * self.a + 2 * self.h


def main():
    rectangle1 = Rectangle(2.0, 4.0)
    rectangle2 = Rectangle(10.0, 12.0)
    print(f"Pole pierwszego prostokąta wynosi: {rectangle1.area()}")
    rectangle1.perimeter()
    rectangle2.area()
    rectangle2.perimeter()


if __name__ == "__main__":
    main()
