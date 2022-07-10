from typing import List
# accepted 
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        dp_len = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    dp_len[i] = dp_len[j]
                elif nums[i] > nums[j] and 1 + dp[j] == dp[i]:
                    dp_len[i] +=  dp_len[j]
   
        largest = max(dp)
        ans = 0
        for i in range(len(dp)):
            if dp[i] == largest:
                ans += dp_len[i]
        return ans

sol = Solution()
nums = [1,3,5,4,7]
nums = [1,2,4,3,5,4,7,2]
res = sol.findNumberOfLIS(nums)
print(res)
        