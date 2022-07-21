import time
from multiprocessing import Pool
from threading import Thread
import random

arrays = [[random.randint(0, 1000) for _ in range(100)] for x in range(1)]
arrays2 = arrays.copy() #[[random.randint(0, 1000) for _ in range(100)] for y in range(30)]


def bubble_sort(array: list) -> list:
    for lst in array:
        for i in range(len(lst)):
            for j in range(len(lst) - i - 1):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return array


if __name__ == "__main__":
    t1 = Thread(target=bubble_sort, args=[arrays])
    t2 = Thread(target=bubble_sort, args=[arrays2])

    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()

    print('(Thread) Time taken in seconds -', end - start)
    print(arrays)
    pool = Pool(processes=2)
    start1 = time.time()
    p1 = pool.apply_async(bubble_sort, [arrays2])
    p2 = pool.apply_async(bubble_sort, [arrays2])
    pool.close()
    pool.join()
    end1 = time.time()
    print('(Pool) Time taken in seconds -', end1 - start1)
    print('>> P1:', p1.get())
    print('>> Dupa2:', p2.get())
