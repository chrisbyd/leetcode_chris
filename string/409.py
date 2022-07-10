from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        single = False
        s = sorted(s)
        i, n = 0, len(s)
        ans = 0
        while i < n:
            if i + 1 < n and s[i] == s[i+1]:
                ans += 2
                i += 2
            else:
                single = True
                i += 1
        return ans + 1 if single else ans

sol = Solution() 
s = "abc"
res = sol.longestPalindrome(s)
print(res)
        

        