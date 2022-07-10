from typing import List


## this dp is correct with only a few changes 
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*3 for _ in range(n+1)]
        
        for i in range(n):
            module = nums[i] % 3
            k = nums[i] // 3
            if module == 0:
                dp[i+1][0] = dp[i][0] + nums[i]
                dp[i+1][1] = dp[i][1] + nums[i] if dp[i][1] !=0 else dp[i][1]
                dp[i+1][2] = dp[i][2] + nums[i] if dp[i][2] !=0 else dp[i][2]
            elif module == 1:
                dp[i+1][1] = max(dp[i][0] + nums[i], dp[i][1]) 
                dp[i+1][2] = max(dp[i][1] + nums[i], dp[i][2]) if dp[i][1] !=0   else  dp[i][2]
                dp[i+1][0] = max(dp[i][0], dp[i][2] + nums[i]) if dp[i][2] != 0  else dp[i][0]
            else:
                dp[i+1][1] = max(dp[i][2] + nums[i], dp[i][1]) if dp[i][2] !=0   else dp[i][1]
                dp[i+1][2] = max(dp[i][0] + nums[i], dp[i][2]) 
                dp[i+1][0] = max(dp[i][0], dp[i][1] + nums[i]) if dp[i][1] !=0   else dp[i][0]
 
        return dp[-1][0]

sol = Solution()
nums = [3,6,5,1,8]
nums = [1,2,3,4,4]
nums = [3,6,5,1,8]
res = sol.maxSumDivThree(nums)
print(res)