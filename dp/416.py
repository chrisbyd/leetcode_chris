import re
from typing import List

# with memorization
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        mask = 0
        nums.sort()
        memo = {}
        def dp(index, curr):
            if (index, curr) not in memo:
                if index == len(nums):
                    if curr == target:
                        res = True
                    else:
                        res = False
                elif curr + nums[index] <= target:
                    res= dp(index + 1, curr + nums[index]) or dp(index + 1, curr)
                else:
                    res = False
                memo[index, curr] = res
                return res
            else:
                return memo[index, curr]
                
        return dp(0, 0)

sol = Solution()
nums = [1,5,11,5]
res = sol.canPartition(nums)
print(res)
                
                


