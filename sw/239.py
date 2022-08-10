from typing import List

### an answer by myself like long time ago
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans, heap = [], []
        for i in range(k-1):
            heappush(heap, (-nums[i], i))
  
        for i in range(k-1, len(nums)):
            heappush(heap, (-nums[i], i))
     
            while heap[0][1] < i - k + 1:
                heappop(heap)
            val, index = heap[0]
            ans.append(-val)
        return ans


# it is correct! I made it
from heapq import heappop, heappush
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans, heap, n = [], [], len(nums)
        for i in range(k-1):
            heappush(heap, (-nums[i], i))
        for i in range(k-1, n):
            heappush(heap, (-nums[i], i))
            while heap[0][1] <= i - k:
                heappop(heap)
                
            maxnum, idx = heap[0]
            ans.append(-maxnum)
        return ans
        
        
        
       