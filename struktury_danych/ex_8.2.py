import random


def not_even(x):
    if x % 2 != 0:
        return x
    return

x = random.sample((range(1, 100)), 99)
print(x)
# jeśli liczby się powtarzają to zwraca mniej liczb
# set1 = {random.randint(5, 120) for s in range(1, 16)}
# print(set1)

set2 = set()
while len(set2) < 15:
    set2.update({random.randint(5, 120)})
print(set2)
result = list(map(not_even, set2))
s_result = set()
for num in result:
    if type(num) is int:
        s_result.update({num})
print(f"Liczby nieparzyste: {s_result}")

set3 = set2.copy()


for num in set3:
    if num % 2 == 0:
        set3.discard()

