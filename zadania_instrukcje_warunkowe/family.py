import itertools

family = ["Adam", "Kornelia", "Kacper", "Joanna", "Stanisław"]


greetings = []

for person in family:
    for person2 in family:
        if person != person2:
            greetings.append([person, person2])

for row in greetings:
    for elem in row:
        print(elem, end=' ')
    print()
print("*" * 30)
greetings2 = list(itertools.combinations(family, 2))

for row in greetings2:
    for elem in row:
        print(elem, end=' ')
    print()