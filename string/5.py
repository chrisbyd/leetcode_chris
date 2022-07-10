from typing import List

import collections
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0 for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        ans = s[0]
        for j in range(1, len(s)):
            for i in range(0,len(s) - j):
                if j == 1 and s[i] == s[i+1]:
                    dp[i][i+1] = 1
                elif j == 1 and s[i] != s[i+1]:
                    dp[i][i+1] = 0
                elif s[i] == s[i + j]:
                    dp[i][i+j] = dp[i+1][i+j-1]
                
                if dp[i][i+j] == 1 and j + 1 > len(ans):
                    ans = s[i:i+j+1]
        return ans

sol = Solution()
s = "aaaa"
res = sol.longestPalindrome(s)
print(res)
            




       
   

        