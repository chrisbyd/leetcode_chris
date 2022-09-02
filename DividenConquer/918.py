from typing import List

### tle because of the max operation on the ruggt sum
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums) 
        leftsum, rightsum = [0], [0]
        for i in range(n):
            leftsum.append(leftsum[-1] + nums[i])
            rightsum.append(rightsum[-1] + nums[n-i-1] )
        rightsum = rightsum[::-1]
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        ans = max(dp)
        for i in range(n):
            ans = max(ans, leftsum[i+1] + max(rightsum[i+1:]))
        return ans

sol = Solution()
nums = [5, -3, 5]
res = sol.maxSubarraySumCircular(nums)
print(res)


####optimizarion
### tle because of the max operation on the ruggt sum
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums) 
        leftsum, rightsum = [0], [0]* (n+1)
        rightmax = [0] * (n+1)
        for i in range(n):
            leftsum.append(leftsum[-1] + nums[i])
            rightsum[n-i-1] =  rightsum[n - i] + nums[n-i-1] 
            rightmax[n- i -1 ] = max(rightmax[n-i],  rightsum[n-i -1]) 

        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        ans = max(dp)
        for i in range(n):
            ans = max(ans, leftsum[i+1] + rightmax[i+1])
        return ans
sol = Solution()
nums = [5, -3, 5]
res = sol.maxSubarraySumCircular(nums)
print(res)


## prefix sum + monoque





##kadaen algorithm * 2
from collections import deque

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums) 
     
        tsum = sum(nums)
        dp = [0]* (n+1)
        dp1 = [0] * (n + 1)
        for i in range(n):
            dp[i+1] = max(dp[i]+ nums[i], nums[i])
        for i in range(n):
            dp1[i+1] = min(dp1[i]+ nums[i], nums[i])
        ans = max(dp)
        if ans == 0:
            return max(nums)
        ans = max(ans, tsum - min(dp1))
        return ans 
sol = Solution()
nums = [-10,-7,9,-7,6,9,-9,-4,-8,-5]
res = sol.maxSubarraySumCircular(nums)
print(res)




