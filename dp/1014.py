
from typing import List


## Time limit exceeded
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        dp = [values[i] for i in range(n)]
        for i in range(1, n):
            ans = -float('inf')
            for j in range(i):
                ans = max(ans, values[j] + values[i] + j - i)
            dp[i] = max(ans, dp[i])
        return max(dp)

sol = Solution()
values = [8, 1, 5, 2, 6]
res = sol.maxScoreSightseeingPair(values)
print(res)


from collections import defaultdict
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        dp = [i for i in range(n)]
        for i in range(1, n):
            pre_index = dp[i-1]
            if values[pre_index] + values[i] + pre_index - i > values[i-1] + values[i] -1:
                dp[i] = pre_index
            else:
                dp[i] = i - 1
        ans = - float('inf')
        for idx, pre in enumerate(dp):
            if idx != 0:
                ans = max(ans, values[pre] + values[idx] + pre - idx)
        return ans

sol = Solution()
values = [8, 1, 5, 2, 6]
res = sol.maxScoreSightseeingPair(values)
print(res)
