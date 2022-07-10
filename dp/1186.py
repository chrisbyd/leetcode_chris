from typing import List
### maximum subarray without deletion
##kadane's algorithm
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [arr[i] for i in range(n)]
        for i in range(1, n):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + arr[i]
        return max(dp)

sol = Solution()
arr = [5, -2, -2, 3]
res = sol.maximumSum(arr)
print(res)



class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp1 = [arr[i] for i in range(n)]
        dp2 = [arr[i] for i in range(n)]
        for i in range(1, n):
            dp1[i] = max(dp1[i-1] + arr[i], arr[i])
        for i in range(n-2, -1, -1):
            dp2[i] = max(dp2[i+1] + arr[i], arr[i])
        if len(arr) == 1:
            return arr[0]
        ans = -float('inf')
        for i in range(n):
            if i == 0:
                ans = max(ans, dp2[1])
            elif i == n-1:
                ans = max(ans, dp1[n-2])
            else:
                ans = max(ans, dp1[i-1] + dp2[i+1])
        ans = max(max(dp1), ans)
        return ans
                