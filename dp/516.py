
from typing import List

# solved by myself
# tle error
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def isPalindrome(s):
            l, r = 0, len(s) -1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        memo = {}
        def dp(s):
            if isPalindrome(s):
                return len(s)
            else:
                if s not in memo:
                    ans = 0
                    for i in range(len(s)):
                        ans = max(ans, dp(s[:i] + s[i+1:]))
                    memo[s] = ans
                    return ans
                else:
                    return memo[s]
            
        return dp(s)

sol = Solution()
s = 'cbbd'
res = sol.longestPalindromeSubseq(s)
print(res)

# with dynamic prohramming
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[1 for j in range(len(s))] for i in range(len(s))]
        for j in range(1,len(s)):
            for i in range(len(s) - j):
                if s[i] == s[i+j] and j == 1:
                    dp[i][i+j] = 2
                elif s[i] == s[i+j] and j != 1:
                    dp[i][i+j] = 2 + dp[i+1][i+j-1]
                else:
                    dp[i][j+i] = max(dp[i+1][i+j], dp[i][i+j-1])
   
        return dp[0][-1]




sol = Solution()
s = "cbbd"
res = sol.longestPalindromeSubseq(s)
print(res)

# # when you come across palindrome questions always remeber two pointer
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         dp = []