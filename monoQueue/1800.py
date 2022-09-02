from typing import List
from collections import deque
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        q = deque()
        ans = 0
        for num in nums:
            if q and q[-1] >= num:
                q = deque()
            q.append(num)
            ans = max(ans, sum(q))
        return ans