from typing import List
from heapq import heappush, heappop

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start, ans = 0, 0
        prev = nums[0]
        minheap, maxheap = [], [] 
        for end, num in enumerate(nums):
            while minheap:
                val, idx = minheap[0]
                if idx < start:
                    heappop(minheap)
                elif abs(num - val) > limit:
                    start = idx + 1
                    heappop(minheap)
                else:
                    break
                    
            while maxheap:
                val , idx = maxheap[0]
                if idx < start:
                    heappop(maxheap)
                elif abs(num+ val) > limit:
                    start = idx + 1
                    heappop(maxheap)
                else:
                    break
                
            ans = max(ans, end - start + 1)
            heappush(minheap, (num, end))
            heappush(maxheap, (-num, end))
        return ans
                
                
                    
sol = Solution()
nums= [8,2,4,7]
k = 4
res  = sol.longestSubarray(nums, k)
print(res)

### another solution with monotonic queue and sliding window
from typing import List
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        insq, desq = deque(), deque()
        start, ans = 0, 0
        
        for end in range(len(nums)):
            while desq and nums[desq[-1]] <= nums[end]:
                desq.pop()
            desq.append(end)
            while insq and nums[insq[-1]] >= nums[end]:
                insq.pop()
            insq.append(end)
            print(end, start, insq, desq)
            while start < end and insq and desq and nums[desq[0]] - nums[insq[0]] > limit:
                if desq and desq[0] == start:
                    desq.popleft()
                if insq and insq[0] == start:
                    insq.popleft()
                start += 1

            print(end, start, insq, desq)
            if nums[desq[0]] - nums[insq[0]] <= limit:
                ans = max(ans, end - start + 1)
        return ans



sol = Solution()
nums= [8,2,4,7]
k = 4
res  = sol.longestSubarray(nums, k)
print(res)