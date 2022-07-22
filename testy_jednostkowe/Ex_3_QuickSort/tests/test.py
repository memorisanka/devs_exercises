from functionality.quick_sort import *


def test_if_quicksort_returns_sorted_list():
    assert quicksort([4, 50, 20, 34]) == [4, 20, 34, 50]
    assert quicksort([6, -3, 126, 0, 46]) == [-3, 0, 6, 46, 126]
    assert quicksort([]) == []
    assert quicksort([2, 0]) == [0, 2]
    assert quicksort([20]) == [20]
