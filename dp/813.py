from typing import List


# dp[k][i] = the largest sum of averages in nums[:i] into K partitions
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        dp = [[0 for j in range(n)] for i in range(k)]
        cumm = 0
        for j in range(len(nums)):
            cumm += nums[j]
            dp[0][j] = cumm / (j+1)
        for i in range(1, k):
            for j in range(i, n):
                ans = 0
                sum = nums[j]
                count = 1
                for m in range(j-1, i -2, -1):
                    ans = max(ans, dp[i-1][m] +sum / count)
                    sum += nums[m]
                    count += 1
                dp[i][j] = ans
            
        return dp[-1][-1]

sol = Solution()
nums = [9,1,2,3,9]
k = 3
res = sol.largestSumOfAverages(nums, k)
print(res)









         






        
        