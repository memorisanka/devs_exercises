import time
import random


def time_this(func):
    def inner(*args):
        start = time.time()
        func(*args)
        end = time.time()
        tm = end - start
        print(tm)
    return inner


@time_this
def fun1(l1: list) -> None:
    sort_l = sorted(l1)


fun1([random.randint(0,1000) for x in range(10000000)])
