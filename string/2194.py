from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1, c2 = ord(s[0]), ord(s[3])
        r1, r2 = int(s[1]), int(s[-1])
        ans = []
        for i in range(c1, c2+1):
            for j in range(r1, r2+1):
                res = chr(i) + str(j)
                ans.append(res)
        return ans

sol = Solution()
s = "A1:F1"
res = sol.cellsInRange(s)
print(res)



        