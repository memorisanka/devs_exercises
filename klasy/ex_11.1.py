array = [1, 2, 3]
class Student:
    def __init__(self, name: str, sex: str, age: int) -> None:
        self.name = name
        self.sex = sex
        self.age = age
        self.grades = []

    def describe(self) -> None:
        print(f"Mam na imię {self.name}, moja płeć to {self.sex}, mam {self.age} lat.")

    # def __str__(self) -> str:
    #     return f"Mam na imię {self.name}, moja płeć to {self.sex}, mam {self.age} lat."


class HyperStudent(Student):
    def __init__(self, name, sex, age):
        super().__init__(name, sex, age)


    # def __str__(self):
    #     return  f"Helo {self.name}"


def main():
    student1 = Student("Jan","mężczyzna",21)
    student_2 = Student("Elwira", "kobieta", 19)
    print(student1)
    print(student_2)
    student1.describe()
    student1.grades.append("5")
    print(student1.grades)
    hyper_student = HyperStudent("Jan", "Men", 38)
    print(hyper_student)

if __name__ == '__main__':
    main()
