from functools import lru_cache
from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i > len(text1) -1 or j > len(text2) - 1:
                return 0
            else:
                if text1[i] == text2[j]:
                    return 1 + dp(i+1, j+1)
                else:
                    return max(dp(i+1, j), dp(i, j+1))
        return dp(0, 0)

# bottom up dp is too easy

sol = Solution()
text1 = "abc"
text2 = "ace"
res = sol.longestCommonSubsequence(text1, text2)
print(res)

            