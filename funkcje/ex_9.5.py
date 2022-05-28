def mix_list(**kwargs):
    print(f"Liczba przekazanych elementów to: ", len(kwargs))
    print(kwargs)

    (x, y) = kwargs.values()
    new_list = []
    for num1, num2 in zip(x, y):
        new_list.append(num2)
        new_list.append(num1)
    print(new_list)



mix_list(even=[2, 4, 6, 8, 12, 16], odd=[3, 5, 7, 15, 21, 23])

