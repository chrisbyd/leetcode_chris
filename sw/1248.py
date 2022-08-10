from typing import List
from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        start = 0
        count, ans, d  = 0, 0, defaultdict(int)
        d[0] = 1
        for end, num in enumerate(nums):
            count += 1 if num % 2 != 0 else 0
            d[count] += 1
            ans += d[count - k]
        return ans
            
            
            