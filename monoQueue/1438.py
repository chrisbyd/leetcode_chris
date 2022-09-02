from typing import List
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        insq, desq = deque(), deque()
        start, ans = 0, 0
        for end in range(len(nums)):
            while desq and nums[end] >= nums[desq[-1]]:
                desq.pop()
            desq.append(end)
            while insq and nums[end] <= nums[insq[-1]]:
                insq.pop()
            insq.append(end)
            while start < end and insq and desq and nums[desq[0]] - nums[insq[0]] > limit:
                if insq[0] == start:
                    insq.popleft()
                if desq[0] == start: 
                    desq.popleft()
                start += 1
            ans = max(ans, end- start + 1)
        return ans
            
        
