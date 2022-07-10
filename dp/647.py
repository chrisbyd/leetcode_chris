from typing import List

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = {}
        for i in range(len(s)):
            dp[i,i] = 1
        for j in range(1, len(s)):
            for i in range(len(s) - j):
                if s[i] == s[i+j] and j == 1:
                    dp[i,i+j] = 1
                elif s[i] == s[i+j]:
                    dp[i, i+j] = dp[i+1, i+j-1]
                else:
                    dp[i, i+ j] =0
        ans = sum(dp.values())
        return ans

sol = Solution()
s= 'aaa'
res = sol.countSubstrings(s)
print(res)
            