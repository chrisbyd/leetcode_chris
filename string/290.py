

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hmap = {}
        hmap1 = {}
        s = s.split()
        pattern = list(pattern)

        if len(pattern) != len(s):
            return False
        for p1, s1 in zip(pattern, s):

            if p1 not in hmap and s1 not in hmap1:
                hmap[p1] = s1
                hmap1[s1] = p1
            elif p1 in hmap and hmap[p1] != s1:
                return False
            elif p1 not in hmap and s1 in hmap1:     
                return False
        return True

sol = Solution() 
pattern = "abba"
s = "dog cat cat dog"
res = sol.wordPattern(pattern, s)
print(res)

        