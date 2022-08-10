from typing import List

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        presum = [0]
        for num in  nums:
            presum.append(presum[-1] + num)
        minval = min(presum[1:])
        return max(1, 1- minval)
        
        
        
        