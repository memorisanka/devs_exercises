to_sort = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

def sort(l: list):
    l.sort(key = lambda x: x[0])
    return l

print(sort(to_sort))