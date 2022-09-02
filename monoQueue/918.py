##kadaen algorithm * 2
from collections import deque
from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        dp1 = [0] * (len(nums) + 1)
        dp2 = [0] * (len(nums) + 1)
        tsum = sum(nums)
        for i, num in enumerate(nums):
            dp1[i+1] = max(num, dp1[i] + num)
        for i, num in enumerate(nums):
            dp2[i+1] = min(num , dp2[i] + num)
        print(dp1)
        ans = max(dp1[1:])
        print(ans)
        print(dp2[1:])
        ans = max(ans, tsum - min(dp2[1:]))
        return ans
        
sol = Solution()
nums = [-3,-2,-3]
res = sol.maxSubarraySumCircular(nums)
print(res)