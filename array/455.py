from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m, n = len(g), len(s)
        i, j = 0, 0
        g.sort()
        s.sort()
        ans = 0
        while i < m and j < n:
            if g[i] <= s[j]:
                i += 1
                j += 1
                ans += 1
            else:
                j += 1
        return ans

sol = Solution()
g = [1,2]
s = [1,2,3]
res = sol.findContentChildren(g, s)
print(res)

            


        