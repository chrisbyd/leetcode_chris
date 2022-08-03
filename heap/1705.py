from heapq import heappush, heappop
from typing import List

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []
        max_day = 0
        for i in range(len(days)):
            max_day = max(max_day, i + days[i])
        ans = 0
        for i in range(max_day + 1):
            if i < len(days):
                heappush(heap, (i + days[i], apples[i]))
            while heap and heap[0][0] == i:
                heappop(heap)
            if heap:
                expire, applenum = heappop(heap)
                if applenum > 1:
                    heappush(heap, (expire, applenum - 1))
                    
                ans += 1
        return ans
                
                