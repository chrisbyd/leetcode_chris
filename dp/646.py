import re
from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key= lambda x: x[0])
        dp = [1 for i in range(len(pairs))]
        for i in range(1, len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1] and dp[i] < 1 +dp[j]:
                    dp[i] = 1 + dp[j]
        return max(dp)


sol = Solution()

pairs = [[1,2],[7,8],[4,5]]
res = sol.findLongestChain(pairs)
print(res)    