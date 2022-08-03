from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if len(nums) == 1: return nums[0]
        nums = ['a' ] + nums + ['a']
        for i in range(1, n+1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]
        return False
                
            