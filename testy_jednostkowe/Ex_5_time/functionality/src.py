from datetime import datetime, timezone


def calc_diff(case: dict) -> float:
    end_time = case['end_time']
    start_time = case['start_time']

    start_time_obj = datetime.fromisoformat(start_time)

    if end_time is None:
        end_time_obj = datetime.now(timezone.utc)
    else:
        end_time_obj = datetime.fromisoformat(end_time)

    return (end_time_obj - start_time_obj).total_seconds()


def main():
    case = {
        'start_time': '2021-11-03T09:22:28+00:00',
        'end_time': None  # None means that case is currently going on
    }
    print(calc_diff(case))
    print(datetime.now(timezone.utc))

if __name__ == "__main__":
    main()
