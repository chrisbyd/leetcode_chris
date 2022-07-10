from functools import lru_cache
from typing import List


# this is the same as the longest sub sequence
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        if not s2 :
            res = 0
            for char in s1:
                res += ord(char)
            return res
        elif not s1:
            res = 0
            for char in s2:
                res += ord(char)
            return res
        else:
            if s1[0] == s2[0]:
                return self.minimumDeleteSum(s1[1:], s2[1:])
            else:
                return min(ord(s1[0]) + self.minimumDeleteSum(s1[1:], s2), ord(s2[0]) + self.minimumDeleteSum(s1, s2[1:]))

sol = Solution()
s1 = "sea"
s2 = "eat"
res = sol.minimumDeleteSum(s1, s2)
print(res)


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}
        
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(s2) :
                    res = 0
                    for char in s1[i:]:
                        res += ord(char)
                elif i == len(s1):
                    res = 0
                    for char in s2[j:]:
                        res += ord(char)
                
                else:
                    if s1[i] == s2[j]:
                        res = dp(i+1, j+1)
                    else:
                        res = min(ord(s1[i]) + dp(i+1, j), ord(s2[j]) + dp(i, j+1))
                memo[i, j] = res
                return res
            else:
                return memo[i, j]
        return dp(0, 0)

sol = Solution()
s1 = "sea"
s2 = "eat"
res = sol.minimumDeleteSum(s1, s2)
print(res)
