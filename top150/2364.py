from typing import List
from collections import defaultdict
#brutal force with tle
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if j -i != nums[j] - nums[i]:
                    ans += 1
        return ans

from typing import List
from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        cmap = defaultdict(int)
        for i in range(n):
            count += cmap[nums[i] - i]
            cmap[nums[i] - i] += 1
        return (n-1) * n // 2 - count
            