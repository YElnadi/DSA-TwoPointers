class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i = 0
        # j = 1
        # while j < len(nums):
        #     if nums[j]> nums[i]:
        #         nums[j], nums[i] = nums[i], nums[j]
        #     if nums[j] == nums[i]:
        #         j += 1
        #         if nums[j] > nums[i]:
        #             nums[j], nums[i] = nums[i], nums[j]
        #     i += 1
        #     j += 1

        i, j = 0, 0

        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                print(nums)
            j += 1


