from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length, n = len(s), len(p)
        start, end = 0, n -1
        hmap = Counter(s[:n-1])
        pmap = Counter(p)
        ans = []
        for end in range(n-1, length):
            hmap[s[end]] += 1
            find = True
            print(hmap, pmap)
            for key in pmap.keys():
                if hmap[key] != pmap[key]:
                    find = False
                    break
            if find:
                ans.append(start)
            hmap[s[start]] -=1
            start +=1
        return ans

sol = Solution()

s = "cbaebabacd"
p ="abc"
res = sol.findAnagrams(s, p)
print(res)