## this should be easy
from heapq import heappush, heappop
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                heappush(heap, (arr[i]/ arr[j], [arr[i], arr[j]]))
        ans = None
        while k > 0:
            _, ans = heappop(heap)
        return ans
        
        
        
        