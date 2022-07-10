
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tem = t
        for char in s:
            if char not in tem:
                return False
            index = tem.index(char)
            tem = tem[index +1:]
        return True

sol  = Solution()
s = "abc"
t = "ahgdcb"
res = sol.isSubsequence(s, t)
print(res)
