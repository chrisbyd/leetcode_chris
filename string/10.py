import re
from sqlite3 import paramstyle
from typing import List

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        firs_match = bool(s) and p[0] in {s[0], '.'}
        
        if len(p) >= 2 and p[1] == '*':
            return (firs_match and self.isMatch(s[1:], p)) or  self.isMatch(s, p[2:])
        else:
            return firs_match and  self.isMatch(s[1:], p[1:])



# class Solution(object):
#     def isMatch(self, text, pattern):
#         if not pattern:
#             return not text

#         first_match = bool(text) and pattern[0] in {text[0], '.'}

#         if len(pattern) >= 2 and pattern[1] == '*':
#             return (self.isMatch(text, pattern[2:]) or 
#                     first_match and self.isMatch(text[1:], pattern))
#         else:
#             return first_match and self.isMatch(text[1:], pattern[1:])
sol = Solution()
s = "aa"
p = "a*"
res = sol.isMatch(s, p)
print(res)

# Dynamic programming
class Solution1:
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], "."}
                    if j + 1 < len(pattern) and pattern[j] == '*':
                        ans = dp(i, j+ 2) or (first_match and dp(i+1, j)) 
                    else:
                        ans = dp(i+1, j+1)
                return ans
            else:
                return memo[i,j]
        return dp(0, 0)

sol = Solution1()
s = "aa"
p = "a*"
res = sol.isMatch(s, p)
print(res)