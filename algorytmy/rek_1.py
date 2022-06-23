# def print_list(l1: list, n):
#     if n < len(l1):
#         print(l1[n])
#         return print_list(l1, n + 1)
#
# print_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 0)

def print_list(l1: list):
    if not l1:
        return
    item = l1[0]
    print(item)
    return print_list(l1[1:])

print_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
