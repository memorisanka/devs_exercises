nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

result = list(map(lambda x: sum(x), zip(nums1, nums2, nums3)))
result2 = list(map(lambda x, y, z: x + y + z, nums1, nums2, nums3))


print(result)
print(result2)