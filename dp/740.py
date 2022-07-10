from cmath import cos
from functools import lru_cache
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        new_nums, cost = [], {}
        for num in nums:
            if num in cost:
                cost[num] += num
            else:
                new_nums.append(num)
                cost[num] = num
        dp = [0 for _ in range(len(new_nums) + 1)]
        dp[1] = cost[nums[0]]
        for i in range(1, len(new_nums)):
            if new_nums[i] -1 == new_nums[i-1]:
                dp[i+1] = max(dp[i], dp[i-1] + cost[new_nums[i]])
            else:
                dp[i+1] = cost[new_nums[i]] + dp[i]
        return dp[-1]

sol = Solution()
nums = [3, 4, 2]
nums = [2,2,3,3,3,4]
#nums = [3,1]
res = sol.deleteAndEarn(nums)
print(res) 
        
## a top down solution
from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cost = defaultdict(int)
        for num in nums:
            cost[num] += num
        nums = list(cost.keys())
        nums.sort()
        @lru_cache(None)
        def dp(i):
            if i == 0:
                return cost[nums[i]]
            elif i == -1:
                return 0
            elif nums[i] - nums[i-1] == 1:
                return max(dp(i-1), cost[nums[i]] + dp(i-2))
            else:
                return cost[nums[i]] + dp(i-1)
        return dp(len(nums)-1)

sol = Solution()
nums = [3, 4, 2]
nums = [2,2,3,3,3,4]
#nums = [3,1]
res = sol.deleteAndEarn(nums)
print(res) 