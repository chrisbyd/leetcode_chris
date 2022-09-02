from typing import List
from heapq import heappush, heappop
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        heap = []
        for i in range(m):
            heappush(heap, (sum(mat[i]), i))
        ans = []
        while k:
            _, idx = heappop(heap)
            ans.append(idx)
            k -= 1
        return ans