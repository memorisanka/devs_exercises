import random
import datetime


def bubble_sort(array: list) -> None:
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def insertion_sort(array: list) -> None:
    for i in range(1, len(array)):
        key = array[i]

        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key


def quick_sort(array: list) -> None:
    array = sorted(array)


def check_time(array: list, sort_function, name_function):
    a1 = datetime.datetime.now()
    sort_function(array)
    b1 = datetime.datetime.now()
    c1 = b1 - a1
    result1 = f"{name_function}: {c1.seconds}s, {c1.microseconds}ms.\n"

    a2 = datetime.datetime.now()
    insertion_sort(array)
    b2 = datetime.datetime.now()
    c2 = b2 - a2
    result2 = f"Insertion sort: {c2.seconds}s, {c2.microseconds}ms.\n"

    a3 = datetime.datetime.now()
    quick_sort(array)
    b3 = datetime.datetime.now()
    c3 = b3 - a3
    result3 = f"Quick sort: {c3.seconds}s, {c3.microseconds}ms.\n"

    with open("result.txt", "a", encoding="UTF-8") as f:
        f.write(f"Dla listy o długości {len(array)} elementów:\n")
        f.write(result1)
        f.write(result2)
        f.write(result3)
        f.write("\n")

def main():
    array1 = [random.randint(0, 1000) for x in range(1000)]
    array2 = [random.randint(0, 10000) for x in range(10000)]
    array3 = [random.randint(0, 100000) for x in range(100000)]
    array4 = [random.randint(0, 1000000) for x in range(1000000)]

    check_time(array1, insertion_sort, "Insertion Sort")
    check_time(array2)


if __name__ == "__main__":
    main()