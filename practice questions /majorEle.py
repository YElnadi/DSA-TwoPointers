class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = {}
        for num in nums:
            if num not in majority:
                majority[num] = 1
            else:
                majority[num] += 1

        max_value = max(majority.values());  
        res = list(key for key, value in majority.items() if value == max_value)
        return max(res)