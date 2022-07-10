from typing import List



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        return True if s == t else False

sol = Solution()
s = "rat"
t = "nagaram"
res = sol.isAnagram(s, t)
print(res)