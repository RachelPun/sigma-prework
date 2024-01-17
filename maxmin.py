nums = []  # list of int


def min_max(nums):
    min = nums[0]
    max = nums[0]
    for num in nums[1:]:
        if num < min:
            min = num
        if num > max:
            max = num
    return [min, max]


print(min_max(nums))
