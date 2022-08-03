from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                ans.append(nums[i])
                break
        nums = list(set(nums))
        for i in range(len(nums)):
            if nums[i] != 1+ i:
                return ans + [1+i]
        return ans + [n]
            
        