from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        slist = sorted(deck)
        n = len(slist)
        q = deque(range(n))
        ans = [0] * n
        for i in range(len(slist)):
            index = q.popleft()
            if q:
                q.append(q.popleft())
            ans[index] = slist[i]
        return ans
            
         
        
        
        
        