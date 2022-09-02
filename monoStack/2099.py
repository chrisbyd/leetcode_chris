from typing import List
from heapq import heappop, heappush, heapify
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ans = []
        heap = nums.copy()
        heapify(heap)
        remove = len(nums) - k
        to_remove = []
        while remove != 0:
            value = heappop(heap)
            to_remove.append(value)
            remove -= 1
        for value in nums:
            if value not in to_remove:
                ans.append(value)
            else:
                to_remove.remove(value)
        
        return ans