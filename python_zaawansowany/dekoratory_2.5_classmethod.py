"""Przykład użycia @classmethod"""


class Worker:
    education = None

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    @classmethod
    def get_object(cls):
        return cls("Jacob", 30)

    @classmethod
    def print_attributes(cls):
        print(f"Worker Class Attributes: {cls.education}")


def main():
    Worker.print_attributes()
    worker1 = Worker.get_object()
    print(worker1.name)
    print(worker1.age)


if __name__ == "__main__":
    main()