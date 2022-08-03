from heapq import heappop, heappush
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans, heap = [], []
        for x, y in points:
            distance = x ** 2 + y ** 2
            heappush(heap, (distance, [x,y]))
        while k > 0:
            _, point = heappop(heap)
            ans.append(point)
            k -= 1
        return ans
            
        