from typing import List

# brutal force solution
# binpacking problem
#not correct
# class Solution:
#     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
#         ans = []
#         def dfs(nums, cur_sub ,count):
#             if count == 3:
#                 if cur_sub[2] - cur_sub[1] == cur_sub[1] -cur_sub[0]:
#                     ans.append(cur_sub[:])
#             else:
#                 for idx, num in enumerate(nums):
#                     cur_sub.append(num)
#                     dfs(nums[idx+1:], cur_sub, count +1)
#                     cur_sub.remove(num)
#         dfs(nums, [], 0)
#         return ans
    


# nums = [2,4,6,8,10]
# sol = Solution()
# res = sol.numberOfArithmeticSlices(nums)
# print(res)

import collections
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = collections.defaultdict(int)
        if len(nums) < 3:
            return 0
        ans = 0
        for i in range(1,len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i,diff] += dp[j,diff] + 1
                ans += dp[j,diff]
       
        return ans
sol = Solution()
nums = [2,4,6,8,10]
nums = [7,7,7,7,7]
res = sol.numberOfArithmeticSlices(nums)
print(res)










        