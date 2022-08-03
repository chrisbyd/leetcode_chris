from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        nums = ['a'] + nums + ['a']
        i = 1
        res = []
        while i <  n + 1:
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                res.append(nums[i])
            i += 1
        return res