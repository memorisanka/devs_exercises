import random

values = sorted([random.randint(0, 30) for _ in range(30)])  # tworzy posortowaną listę
print(values)

#values = sorted([x for x in range(15)])


def bin_search(my_list: list, x: int):
    left = 0
    right = len(my_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if my_list[mid] < x:
            left = mid + 1
        elif my_list[mid] > x:
            right = mid - 1
        else:
            break
    if len(my_list) - mid > 10:
        return True
    return False


print(bin_search(values, 20))
