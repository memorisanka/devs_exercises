import random
counter = 0
result = [12, 1, 45, 76, 50, 23]

for number in result:
    if 1 <= number <= 49:
        continue
    else:
        print(f"Liczba {number} jest poza zakresem. Dokonuję zmiany.")
        idx = result.index(number)
        result[idx] = random.randint(1, 50)

print(result)
print(counter)