from collections import defaultdict
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letter2range = defaultdict(lambda : [float("inf"), -float('inf')])
        for idx, char in enumerate(s):
            letter2range[char][0] = min(idx, letter2range[char][0])
            letter2range[char][1] = max(idx, letter2range[char][1])
        res = [letter2range[key] for key in letter2range.keys()]
        res = sorted(res, key= lambda x: x[0])
        ans = []
        left, right = res[0]
        for i, j in res[1:]:
            if i > right:
                ans.append(right - left +1)
                left = i
            right = max(right, j)
        ans.append(right - left + 1)
        return ans
                
        
            
            
        
# using greedy algorithm
from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {char: idx for idx, char in enumerate(s)}
        j = anchor = 0
        ans = []
        for i,  c in enumerate(s):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor +1)
                anchor = i+1
        return ans
        
                
        
            
            