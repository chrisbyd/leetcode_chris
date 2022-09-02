from typing import List
from collections import deque
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        monoq = deque()
        ans1 = set()
        ans2 =  set()
        for i, guards in enumerate(security):
            if monoq and guards > monoq[-1]:
                monoq = deque()
            if i >= time and len(monoq) >= time:
                ans1.add(i)
            monoq.append(guards)
        monoq = deque()
        for i in range(len(security) -1, -1, -1):
                if monoq and security[i] > monoq[-1]:
                    monoq = deque()
                if i <= len(security) - time - 1 and len(monoq) >= time:
                    ans2.add(i)
                monoq.append(security[i])
        return ans1 & ans2
                    
        