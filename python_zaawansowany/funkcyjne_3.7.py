nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = [num for num in nums if num % 2 == 0]
result = list(filter(lambda x: x % 2 == 0, nums))
new_nums = list(map(lambda y: y ** 2, result))


print(new_nums)
print(result)
print(filtered_list)