from collections import deque
from heapq import heappop, heappush
class Solution:
    def findMaxValueOfEquation(self, ponts: List[List[int]], k: int) -> int:
        heap = []
        ans = -float('inf')
        for xj, yj in ponts:
            while heap and heap[0][1] < xj - k:
                heappop(heap)
            if  heap:
                ans = max(ans, -heap[0][0] + xj + yj)
            heappush(heap, (- (yj - xj), xj))
        return ans
                
            