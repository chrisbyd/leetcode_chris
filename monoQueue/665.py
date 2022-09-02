from typing import List
from collections import deque
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        violation = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                violation += 1
                if i < 2  or nums[i-2]  <= nums[i]:
                    nums[i] = nums[i]
                else:
                    nums[i] = nums[i-1]
            if violation == 2:
                return False
        return True
        
     