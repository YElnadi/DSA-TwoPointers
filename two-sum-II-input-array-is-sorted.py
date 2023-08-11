def twoSum(numbers, target):
    # array is sorted in ascending
    l = 0
    r = len(numbers) - 1

    while l < r:
        curSum = numbers[l] + numbers[r]
        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l + 1, r+1]


print(twoSum([2, 3, 4], 6))
