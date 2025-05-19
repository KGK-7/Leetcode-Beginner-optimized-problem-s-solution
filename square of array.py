def sortedSquares(nums):
    n = len(nums)
    res = [0] * n
    left, right = 0, n - 1
    pos = n - 1  # Start filling from the end

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            res[pos] = nums[left] ** 2
            left += 1
        else:
            res[pos] = nums[right] ** 2
            right -= 1
        pos -= 1

    return res


nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))
