from typing import List

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a, b, c = [-1], [-1], [-1]
        for i, char in enumerate(s):
            if char == 'a': a.append(i)
            else: a.append(a[-1])
            if char == 'b': b.append(i)
            else: b.append(b[-1])
            if char == 'c': c.append(i)
            else:  c.append(c[-1])
        ans = 0
        print(a,b,c)
        for i in range(len(s)):
            index = min(a[i+1], b[i+1], c[i+1])
            ans += (index + 1)
        return ans
            

sol = Solution()
s = "abcabc"
res = sol.numberOfSubstrings(s)
print(res)