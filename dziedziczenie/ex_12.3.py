class Member:
    def __init__(self, name: str):
        self.full_name = name

    def introduce(self):
        print(f'Hi, I\'m {self.full_name}!')


class Student(Member):
    def __init__(self, name: str, reason: str):
        super().__init__(name)
        self.reason = reason


class Instructor(Member):
    def __init__(self, name: str, bio: str, *skillset):
        super().__init__(name)
        self.bio = bio
        self.skillset = list(skillset)

    def add_skill(self, skill):
        self.skillset.append(skill)


class Workshop:
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []

    def add_participant(self, participant):
        if participant.__class__.__name__ == 'Instructor':
            self.instructors.append(participant)
        if participant.__class__.__name__ == 'Student':
            self.students.append(participant)

    def print_details(self):
        print(f'Workshop - {self.date} - {self.subject}\n')
        print('Students:')
        for num, student in enumerate(self.students, start=1):
            print(f'{num}. {student.full_name} - {student.reason}')
        print("\n")
        print('Instructors:')
        for num, instructor  in enumerate(self.instructors, start=1):
            # for r in i.skillset:
            #     skills += r
            print(f'{num}. {instructor.full_name} - {" ".join(instructor.skillset)}')
            print(f'\t{instructor.bio}')


workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()
