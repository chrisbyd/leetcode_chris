from typing import List
##brutal force solution
from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hmap = defaultdict(int)
        ans = []
        for i in range(len(s) - 10 + 1):
            cur = s[i:i + 10]
            hmap[cur] += 1
            if hmap[cur]  ==  2:
                ans.append(cur)
        return ans
        
        
        