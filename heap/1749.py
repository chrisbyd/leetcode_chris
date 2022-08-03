from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        dp_max = [nums[0]] * len(nums)
        dp_min = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i], dp_max[i-1] + nums[i])
            dp_min[i] = min(nums[i], dp_min[i-1] + nums[i])
        dp_abs = []
        for i in range(len(nums)):
            dp_abs.append(max(abs(dp_max[i]), abs(dp_min[i])))
        return max(dp_abs)
            
        
        