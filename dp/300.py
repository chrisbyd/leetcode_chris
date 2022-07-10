from typing import List
#
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] - nums[j] > 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)

sol = Solution()
nums = [10,9,2,5,3,7,101,18]
nums = [7,7,7,7,7,7,7]
res = sol.lengthOfLIS(nums)
print(res)

                    
        