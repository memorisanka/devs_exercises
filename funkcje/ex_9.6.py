def only2digit(nums):
    """W podanej jako argument liście wyszukuje liczby dwucyfrowe"""

    # selected = [num for num in nums if 9 < num < 100]
    two_digits = []
    for num in nums:
        if num > 9:
            two_digits.append(num)
    return two_digits

print(only2digit([2, 4, 12, 3, 15, 28, 56, 9, 10, 67]))