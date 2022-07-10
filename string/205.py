
# although accepted but i dont understand
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_tmap = {}
        tmap = {}
        for i in range(len(s)):
            if s[i] not in s_tmap and t[i] not in tmap:
                tmap[t[i]] = True
                s_tmap[s[i]] = t[i]
            elif s[i] in s_tmap and s_tmap[s[i]] != t[i]:
                return False
            elif s[i] not in s_tmap and t[i] in tmap :
                return False
            
        return True

sol = Solution()

s = "egcd"
t = "adfd"
res = sol.isIsomorphic(s,t)
print(res)


