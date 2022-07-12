"""Przykład użycia @classmethod"""
from datetime import date

class Worker:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    @classmethod
    def from_birthday(cls, name, year):
        return cls(name, date.today().year - year)

class Student:
    school_name = "ABC school"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, name):
        print(Student.school_name)
        Student.school_name = name



def main():
    student = Student("Robert", 19)
    student.change_school("ABCY School")
    worker = Worker("Robert", 15)
    worker_1 = Worker.from_birthday("Mike", 1984)
    print(worker.age)
    print(worker_1.age)

if __name__ == "__main__":
    main()