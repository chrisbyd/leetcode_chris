from functools import lru_cache
from tkinter.tix import Tree
from typing import List

# accepted weired 
# did not exceeds time
# using recursion
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def recursive(nums, player, sum0, sum1):
            print(nums, player, sum0, sum1)
            if len(nums) == 1 and player == 0 and sum0 + nums[0] >= sum1:
                return True
            elif len(nums) == 1 and player == 1 and sum1 + nums[0] <= sum0:
                return True
            elif len(nums) == 1:
                return False
                
            else:
                if player == 0:
                    return recursive(nums[1:], 1- player, sum0 + nums[0], sum1) or recursive(nums[:-1], 1- player, sum0 + nums[-1], sum1)
                else:
                    return recursive(nums[1:], 1- player, sum0 , sum1 + nums[0]) and recursive(nums[:-1], 1- player, sum0, sum1+ nums[-1])


        return recursive(nums, 0, 0, 0)

sol  = Solution()
nums = [1,1]
res = sol.PredictTheWinner(nums)
print(res)
# using dynamic programming to solve this problem
# this is totally by me
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return nums[i]
            else:
                res = max(nums[i] - dp(i+1, j), nums[j] - dp(i, j-1))
                return res
        if dp(0, len(nums) -1) >= 0:
            return True
        return False

sol  = Solution()
nums = [1,5,233, 7]
res = sol.PredictTheWinner(nums)
print(res)