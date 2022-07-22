# tutorial z yt

arr = [89, 4, 57, 3, 2, 0]


def divide(tab: list, start: int, end: int) -> int:
    pivot = tab[end]
    low = start
    high = end - 1

    while True:
        while low <= high and tab[low] <= pivot:
            low += 1

        while low <= high and tab[high] >= pivot:
            high -= 1

        if low <= high:
            tab[low], tab[high] = tab[high], tab[low]
        else:
            break

    tab[end], tab[low] = tab[low], tab[end]
    return low


def quicksort(tab: list, start=0, end=None) -> list:
    if end is None:
        end = len(tab) - 1
    if start < end:
        pivot = divide(tab, start, end)
        quicksort(tab, start, pivot - 1)
        quicksort(tab, pivot + 1, end)
    return tab

quicksort(arr)
print(arr)