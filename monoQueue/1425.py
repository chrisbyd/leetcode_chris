from typing import List
from collections import deque

## tle
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [-1] * len(nums) 
        for j, num in enumerate(nums):
            if j == 0:
                dp[j] = num
            else:
                ans = 0
                for i in range(j-k,  j):
                    if i >= 0 and dp[i] >=0:
                        ans = max(ans, dp[i])
                dp[j] = ans + nums[j]
        return max(dp)

## dynamic programming + monotonic queue
from typing import List
from collections import deque
from heapq import heappush, heappop
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [-1] * len(nums)
        heap = []
        for j, num in enumerate(nums):
            if j == 0:
                dp[j] = num
            else:
                while heap and heap[0][1] < j - k:
                    heappop(heap)
                res = 0 
                if heap:
                    res = max(res, -heap[0][0])
                print(num, res)
                dp[j] = num + res
            print(heap)
            heappush(heap, (-dp[j], j))
        return max(dp)
sol = Solution()
nums = [-5266,4019,7336,-3681,-5767]
k = 2
res = sol.constrainedSubsetSum(nums, k)
print(res)