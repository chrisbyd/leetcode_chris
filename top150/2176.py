from typing import List
from collections import defaultdict
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cmap = defaultdict(int)
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if (i* j) % k != 0:
                    continue
                if nums[i] == nums[j]:
                    ans += 1
        return ans