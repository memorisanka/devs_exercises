from functionality.src import *
from freezegun import freeze_time


@freeze_time("2021-11-04T09:22:28+00:00")
def test_should_return_time_diff_in_seconds():
    expected = 86400.0
    case = {
        'start_time': '2021-11-03T09:22:28+00:00',
        'end_time': None
    }
    assert calc_diff(case) == expected



