def nums_val():
    while True:
        try:
            nums = list(map(
                lambda x: int(x),
                input("Enter a list of integers with space: ").split()
            ))
            break
        except:
            print("Invalid input. Please try again.")
    return nums


def min_max(nums):
    min = nums[0]
    max = nums[0]
    for num in nums[1:]:
        if num < min:
            min = num
        if num > max:
            max = num
    return [min, max]


nums = nums_val()

print(min_max(nums))
