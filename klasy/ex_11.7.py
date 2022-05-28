from datetime import datetime
from datetime import timedelta


class Case:

    def __init__(self):
        self.case = {}

    def create_case(self, name: str, created_task: str, end_task):
        self.case = {"name": name,
                     "created_task": created_task,
                     "end_task": end_task}

    def display(self):
        for k, v in self.case.items():
            print(f"{k}, {v}")

    def retrieve_seconds(self):
        if self.case["end_task"] is None:
            self.case["end_task"] = datetime.now()
            end = self.case["end_task"]
            created = datetime.strptime(self.case["created_task"], '%Y-%m-%dT%H:%M:%S+00:00')
            # print(f"{end - created}")
            duration = end - created
            duration = timedelta.total_seconds(duration)
            print(f"Czas, który upłynął pomiędzy zadaniami w sekundach: {duration}")
        else:
            end = datetime.strptime(self.case["end_task"], '%Y-%m-%dT%H:%M:%S+00:00')
            created = datetime.strptime(self.case["created_task"], '%Y-%m-%dT%H:%M:%S+00:00')
            # print(f"{end - created}")
            duration = end - created
            duration = timedelta.total_seconds(duration)
            print(f"Czas, który upłynął pomiędzy zadaniami w sekundach: {duration}")



def main():
    case_1 = Case()
    case_1.create_case("first_case", "2021-09-26T19:48:12+00:00", None)
    case_1.display()
    case_1.retrieve_seconds()
    case_2 = Case()
    case_2.create_case("second_case", "2021-09-26T19:48:12+00:00", "2021-10-26T19:48:12+00:00")
    case_2.display()
    case_2.retrieve_seconds()

if __name__ == "__main__":
    main()