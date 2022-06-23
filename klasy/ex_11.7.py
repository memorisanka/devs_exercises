from datetime import datetime, timedelta
from typing import Optional

class Case:

    def __init__(self, name: str, created_task: str, end_task: Optional[str]) -> None:
        self.name = name,
        self.created_task = created_task
        self.end_task = end_task


    def create_case(self, name: str, created_task: str, end_task) -> None:
        self.case = {"name": name,
                     "created_task": created_task,
                     "end_task": end_task}

    def display(self):
        for k, v in self.case.items():
            print(f"{k}, {v}")

    def retrieve_seconds(self):
        time_format = "'%Y-%m-%dT%H:%M:%S+00:00'"
        if self.case["end_task"]:
            self.case["end_task"] = datetime.now()
            end = self.case["end_task"]
            created = datetime.strptime(self.case["created_task"], time_format)
            # print(f"{end - created}")
            duration = end - created
            duration = timedelta.total_seconds(duration)
            print(f"Czas, który upłynął pomiędzy zadaniami w sekundach: {duration}")
        else:
            end = datetime.strptime(self.case["end_task"], time_format)
            created = datetime.strptime(self.case["created_task"], time_format)
            # print(f"{end - created}")
            duration = end - created
            duration = timedelta.total_seconds(duration)
            print(f"Czas, który upłynął pomiędzy zadaniami w sekundach: {duration}")
            return


first_case = {'name"': "first_case",
              "created_task": '2021-09-26T19:48:12+00:00',
              "end_task": None}

def main():
    case_1 = Case(**first_case)
    case_1.create_case(name="first_case", created_task="2021-09-26T19:48:12+00:00", end_task=None)
    case_1.display()
    case_1.retrieve_seconds()
    case_2 = Case()
    case_2.create_case("second_case", "2021-09-26T19:48:12+00:00", "2021-10-26T19:48:12+00:00")
    case_2.display()
    case_2.retrieve_seconds()

if __name__ == "__main__":
    main()