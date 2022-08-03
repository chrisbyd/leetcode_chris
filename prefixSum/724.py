from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        preSum = [0]
        for num in nums:
            preSum.append(num + preSum[-1])
        for i in range(len(nums)):
            if preSum[i] == preSum[-1] - preSum[i+1]:
                return i
        return -1
            
        