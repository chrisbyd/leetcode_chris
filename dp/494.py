from functools import lru_cache
from textwrap import indent
from typing import List


# time 
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(index, target):
            if index < 0 :
                if target == 0:
                    return 1
                return 0
            else:
                return dp(index-1, target + nums[index]) + dp(index -1, target - nums[index])
        return dp(len(nums) -1, target)

sol =  Solution()
nums = [0,1,1]
target = 2
res = sol.findTargetSumWays(nums, target)
print(res)