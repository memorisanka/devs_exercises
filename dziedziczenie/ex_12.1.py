from abc import abstractmethod


class Shape:
    def __init__(self, lenght) -> None:
        self.lenght = lenght

    @abstractmethod
    def area(self) -> None:
        raise NotImplementedError


class Square(Shape):
    def __init__(self, lenght: int) -> None:
        super().__init__(lenght)

    def area(self) -> str:
        area = self.lenght**2
        return f"Pole prostokąta jest równe: {area} j2."




def main():
    square_1 = Square(4)
    print(square_1.area())
    square_2 = Square(10)
    print(square_2.area())


if __name__ == "__main__":
    main()
